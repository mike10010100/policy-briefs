#!/usr/bin/env python3
"""Verify 1 + 6 Hub-and-Spoke tri-format parity, WP:AISIGNS discipline, PDF page counts, and headless Chromium CDP UX."""

import base64
import html as html_lib
import json
import os
import re
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import series_data as data  # noqa: E402

REPO = Path("/home/mike10010100/.gemini/antigravity-cli/scratch/policy-briefs")
AI_DIR = REPO / "ai-governance"
ASSETS_DIR = REPO / "assets"
CHROME_BIN = "/home/mike10010100/.cache/ms-playwright/chromium-1248/chrome-linux64/chrome"

BANNED_WORDS = [
    "delve", "delves", "delving",
    "underscore", "underscores", "underscoring",
    "showcase", "showcases", "showcasing",
    "tapestry", "pivotal", "landscape", "transformative", "robust",
    "foster", "fosters", "fostering",
    "navigate", "navigates", "navigating",
    "highlight", "highlights", "highlighting",
    "rather than", "not just",
    "graywater",
]


def clean_inline_html(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = html_lib.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def clean_md_prose(s: str) -> str:
    # Strip markdown *italic* spans while leaving literal '*' inside math/quotes alone.
    s = re.sub(r"\*([^*\n]+)\*", r"\1", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def count_pdf_pages(pdf_path: Path) -> int:
    pdf_bytes = pdf_path.read_bytes()
    pages = re.findall(rb"/Type\s*/Page(?!s)\b", pdf_bytes)
    assert pages, f"Zero pages in {pdf_path}"
    return len(pages)


# ---------------------------------------------------------------------------
# 1. Tri-format verbatim parity (Hub + 6 Spokes)
# ---------------------------------------------------------------------------

def parse_hub_md() -> dict:
    md_path = AI_DIR / data.HUB["md_filename"]
    lines = md_path.read_text(encoding="utf-8").splitlines()
    bluf: list[str] = []
    pillars: list[dict] = []
    tradeoffs: list[str] = []
    refs: list[str] = []

    mode = None
    cur_pillar: dict | None = None
    for raw in lines:
        line = raw.strip()
        if line == "### Bottom line up front":
            mode = "bluf"
            continue
        m_pil = re.match(r"^###\s+(\d+)\.\s+", line)
        if m_pil:
            mode = "pillar"
            cur_pillar = {"lead": [], "bullets": []}
            pillars.append(cur_pillar)
            continue
        if line == "### Trade-offs to weigh in policy design":
            mode = "tradeoffs"
            cur_pillar = None
            continue
        if line == "Key references for staff follow-up:":
            mode = "refs"
            continue
        if not line or line == "---":
            continue

        if mode == "bluf":
            bluf.append(clean_md_prose(line))
        elif mode == "pillar" and cur_pillar is not None:
            if line.startswith("* "):
                cur_pillar["bullets"].append(clean_md_prose(line[2:]))
            elif line.startswith("Full issue brief "):
                continue
            else:
                cur_pillar["lead"].append(clean_md_prose(line))
        elif mode == "tradeoffs":
            if line.startswith("**") and line.endswith("**"):
                continue
            tradeoffs.append(clean_md_prose(line))
        elif mode == "refs":
            if line.startswith("* "):
                refs.append(clean_md_prose(line[2:]))
    return {"bluf": bluf, "pillars": pillars, "tradeoffs": tradeoffs, "refs": refs}


def parse_hub_print() -> dict:
    html = (AI_DIR / "brief.html").read_text(encoding="utf-8")
    m_bluf = re.search(r'<section class="bluf-box">(.*?)</section>', html, re.S)
    assert m_bluf
    bluf = [clean_inline_html(p) for p in re.findall(r"<p>(.*?)</p>", m_bluf.group(1), re.S)]

    pillars = []
    for block in re.findall(r'<section class="pillar-block">(.*?)</section>', html, re.S):
        no_ul = re.sub(r"<ul.*?</ul>", "", block, flags=re.S)
        # Exclude deep-dive-note line matched by class="deep-dive-note"
        lead = [
            clean_inline_html(p[1])
            for p in re.findall(r'<p(?:\s+class="([^"]+)")?>(.*?)</p>', no_ul, re.S)
            if p[0] != "deep-dive-note"
        ]
        bullets = [clean_inline_html(li) for li in re.findall(r"<li>(.*?)</li>", block, re.S)]
        pillars.append({"lead": lead, "bullets": bullets})

    m_tr = re.search(r'<section class="tradeoffs-section">(.*?)</section>', html, re.S)
    assert m_tr
    tradeoffs = [clean_inline_html(p) for p in re.findall(r"<p>(.*?)</p>", m_tr.group(1), re.S)]

    m_ref = re.search(r'<section class="references-block">(.*?)</section>', html, re.S)
    assert m_ref
    refs = [clean_inline_html(li) for li in re.findall(r"<li>(.*?)</li>", m_ref.group(1), re.S)]
    return {"bluf": bluf, "pillars": pillars, "tradeoffs": tradeoffs, "refs": refs}


def parse_hub_web() -> dict:
    html = (AI_DIR / "index.html").read_text(encoding="utf-8")
    m_bluf = re.search(r'<section id="bluf" class="bluf-card">(.*?)</section>', html, re.S)
    assert m_bluf
    bluf = [clean_inline_html(p) for p in re.findall(r"<p data-verbatim>(.*?)</p>", m_bluf.group(1), re.S)]

    pillars = []
    for pil in data.HUB["pillars"]:
        m_sec = re.search(rf'<section id="{re.escape(pil["id"])}" class="brief-section">(.*?)</section>', html, re.S)
        assert m_sec, f"Missing hub section {pil['id']}"
        blk = m_sec.group(1)
        lead = [clean_inline_html(p) for p in re.findall(r"<p data-verbatim>(.*?)</p>", blk, re.S)]
        m_ul = re.search(r'<ul class="pillar-bullets" data-verbatim>(.*?)</ul>', blk, re.S)
        assert m_ul
        bullets = [clean_inline_html(li) for li in re.findall(r"<li>(.*?)</li>", m_ul.group(1), re.S)]
        pillars.append({"lead": lead, "bullets": bullets})

    m_tr = re.search(r'<section id="trade-offs" class="brief-section">(.*?)</section>', html, re.S)
    assert m_tr
    tradeoffs = [clean_inline_html(p) for p in re.findall(r"<p data-verbatim>(.*?)</p>", m_tr.group(1), re.S)]

    m_ref = re.search(r'<section id="references" class="brief-section references-card">(.*?)</section>', html, re.S)
    assert m_ref
    refs = [clean_inline_html(li) for li in re.findall(r"<li>(.*?)</li>", m_ref.group(1), re.S)]
    return {"bluf": bluf, "pillars": pillars, "tradeoffs": tradeoffs, "refs": refs}


def parse_spoke_md(sp: dict) -> dict:
    md_path = AI_DIR / sp["slug"] / sp["md_filename"]
    lines = md_path.read_text(encoding="utf-8").splitlines()
    bluf: list[str] = []
    sections: list[list[str]] = []
    tradeoffs: list[str] = []
    refs: list[str] = []
    glossary: list[tuple[str, str]] = []

    mode = None
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line == "### Bottom line up front":
            mode = "bluf"
        elif re.match(r"^###\s+\d+\.\s+", line):
            mode = "sec"
            sections.append([])
        elif line == "### Trade-offs to weigh in policy design":
            mode = "tradeoffs"
        elif line == "Key references for staff follow-up:":
            mode = "refs"
        elif line == "### Appendix: Plain-English technical and policy glossary":
            mode = "glossary"
        elif not line or line == "---":
            pass
        elif mode == "bluf":
            bluf.append(clean_md_prose(line))
        elif mode == "sec":
            sections[-1].append(clean_md_prose(line))
        elif mode == "tradeoffs":
            if not (line.startswith("**") and line.endswith("**")):
                tradeoffs.append(clean_md_prose(line))
        elif mode == "refs":
            if line.startswith("* "):
                refs.append(clean_md_prose(line[2:]))
        elif mode == "glossary":
            if line.startswith("**") and line.endswith("**"):
                dt = clean_md_prose(line[2:-2].strip())
                dd = clean_md_prose(lines[i + 1].strip())
                glossary.append((dt, dd))
                i += 1
        i += 1
    return {"bluf": bluf, "sections": sections, "tradeoffs": tradeoffs, "refs": refs, "glossary": glossary}


def parse_spoke_print(sp: dict) -> dict:
    html = (AI_DIR / sp["slug"] / "brief.html").read_text(encoding="utf-8")
    m_bluf = re.search(r'<section class="bluf-box">(.*?)</section>', html, re.S)
    assert m_bluf
    bluf = [clean_inline_html(p) for p in re.findall(r"<p>(.*?)</p>", m_bluf.group(1), re.S)]

    # Split body after </section> (bluf-box) up to <section class="tradeoffs-print-section">
    m_mid = re.search(r'</section>\s*(<h3>.*?)<section class="tradeoffs-print-section">', html, re.S)
    assert m_mid
    sec_chunks = re.split(r"<h3>.*?</h3>", m_mid.group(1), flags=re.S)[1:]
    sections = [[clean_inline_html(p) for p in re.findall(r"<p>(.*?)</p>", ch, re.S)] for ch in sec_chunks]

    m_tr = re.search(r'<section class="tradeoffs-print-section">(.*?)</section>', html, re.S)
    assert m_tr
    tradeoffs = [clean_inline_html(p) for p in re.findall(r"<p>(.*?)</p>", m_tr.group(1), re.S)]

    m_ref = re.search(r'<section class="references-block">(.*?)</section>', html, re.S)
    assert m_ref
    refs = [clean_inline_html(li) for li in re.findall(r"<li>(.*?)</li>", m_ref.group(1), re.S)]

    m_gl = re.search(r'<section class="glossary-appendix">(.*?)</section>', html, re.S)
    assert m_gl
    dts = [clean_inline_html(x) for x in re.findall(r"<dt>(.*?)</dt>", m_gl.group(1), re.S)]
    dds = [clean_inline_html(x) for x in re.findall(r"<dd>(.*?)</dd>", m_gl.group(1), re.S)]
    assert len(dts) == len(dds)
    return {"bluf": bluf, "sections": sections, "tradeoffs": tradeoffs, "refs": refs, "glossary": list(zip(dts, dds))}


def parse_spoke_web(sp: dict) -> dict:
    html = (AI_DIR / sp["slug"] / "index.html").read_text(encoding="utf-8")
    m_bluf = re.search(r'<section id="bluf" class="bluf-card">(.*?)</section>', html, re.S)
    assert m_bluf
    bluf = [clean_inline_html(p) for p in re.findall(r"<p data-verbatim>(.*?)</p>", m_bluf.group(1), re.S)]

    sections = []
    for sec in sp["sections"]:
        m_sec = re.search(rf'<section id="{re.escape(sec["id"])}" class="brief-section">(.*?)</section>', html, re.S)
        assert m_sec, f"Missing spoke {sp['slug']} section {sec['id']}"
        sections.append([clean_inline_html(p) for p in re.findall(r"<p data-verbatim>(.*?)</p>", m_sec.group(1), re.S)])

    m_tr = re.search(r'<section id="trade-offs" class="brief-section">(.*?)</section>', html, re.S)
    assert m_tr
    tradeoffs = [clean_inline_html(p) for p in re.findall(r"<p data-verbatim>(.*?)</p>", m_tr.group(1), re.S)]

    m_ref = re.search(r'<section id="references" class="brief-section references-card">(.*?)</section>', html, re.S)
    assert m_ref
    refs = [clean_inline_html(li) for li in re.findall(r"<li>(.*?)</li>", m_ref.group(1), re.S)]

    m_gl = re.search(r'<section id="glossary" class="brief-section wide-section glossary-section">(.*?)</section>', html, re.S)
    assert m_gl
    dts = [clean_inline_html(x) for x in re.findall(r"<dt>(.*?)</dt>", m_gl.group(1), re.S)]
    dds = [clean_inline_html(x) for x in re.findall(r"<dd>(.*?)</dd>", m_gl.group(1), re.S)]
    assert len(dts) == len(dds)
    return {"bluf": bluf, "sections": sections, "tradeoffs": tradeoffs, "refs": refs, "glossary": list(zip(dts, dds))}


def check_parity():
    # Hub parity
    h_md = parse_hub_md()
    h_pr = parse_hub_print()
    h_wb = parse_hub_web()
    assert h_md == h_pr == h_wb, f"Hub tri-format parity mismatch:\nMD={h_md}\nPR={h_pr}\nWB={h_wb}"
    assert len(h_md["pillars"]) == 6 and len(h_md["tradeoffs"]) == 6 and len(h_md["refs"]) == 6

    # Spokes parity
    total_gl = 0
    for sp in data.SPOKES:
        s_md = parse_spoke_md(sp)
        s_pr = parse_spoke_print(sp)
        s_wb = parse_spoke_web(sp)
        assert s_md == s_pr == s_wb, (
            f"Spoke {sp['slug']} tri-format parity mismatch:\nMD={s_md}\nPR={s_pr}\nWB={s_wb}"
        )
        assert len(s_md["glossary"]) == len(sp["glossary"])
        total_gl += len(s_md["glossary"])

    print(
        f"[PASS] 100% verbatim tri-format parity verified across Hub (6 pillars, 6 tradeoffs, 6 refs) "
        f"and all 6 Spokes ({total_gl} total scoped glossary entries)."
    )


# ---------------------------------------------------------------------------
# 2. WP:AISIGNS discipline & inline-term wiring across all 23 text/HTML files
# ---------------------------------------------------------------------------

def check_wp_aisigns_and_terms():
    files_to_scan = [
        REPO / "index.html",
        REPO / "README.md",
        AI_DIR / data.HUB["md_filename"],
        AI_DIR / "brief.html",
        AI_DIR / "index.html",
    ]
    for sp in data.SPOKES:
        files_to_scan.extend([
            AI_DIR / sp["slug"] / sp["md_filename"],
            AI_DIR / sp["slug"] / "brief.html",
            AI_DIR / sp["slug"] / "index.html",
        ])

    for path in files_to_scan:
        raw = path.read_text(encoding="utf-8")
        if path.suffix == ".md":
            cleaned = re.sub(r"```.*?```", "", raw, flags=re.S)
            lines = [ln for ln in cleaned.splitlines() if ln.strip() != "---"]
            prose = "\n".join(lines)
        else:
            no_code = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
            no_code = re.sub(r"<style.*?</style>", " ", no_code, flags=re.S)
            no_code = re.sub(r"<script.*?</script>", " ", no_code, flags=re.S)
            popover_attrs = " ".join(
                html_lib.unescape(m)
                for m in re.findall(r'data-popover-(?:title|body)="([^"]*)"', no_code)
            )
            meta_desc = " ".join(
                html_lib.unescape(m)
                for m in re.findall(r'<meta[^>]+content="([^"]*)"', no_code)
            )
            visible = clean_inline_html(no_code)
            prose = f"{visible} {popover_attrs} {meta_desc}"

        assert "\u2014" not in prose, f"Em dash found in {path}"
        assert "--" not in prose, f"Double hyphen found in {path}"
        for q in ["\u201c", "\u201d", "\u2018", "\u2019"]:
            assert q not in prose, f"Curly quote {repr(q)} found in {path}"
        low = prose.lower()
        for bw in BANNED_WORDS:
            assert not re.search(rf"\b{re.escape(bw)}\b", low), f"Banned word/phrase '{bw}' found in {path}"

    # Verify inline-term targets, sequential DOM glossary IDs, zero orphans & ARIA attributes in every Spoke index.html
    total_inline = 0
    for sp in data.SPOKES:
        web = (AI_DIR / sp["slug"] / "index.html").read_text(encoding="utf-8")
        dom_ids = re.findall(r'<dl id="(term-\d+)"', web)
        assert dom_ids == [f"term-{i}" for i in range(1, len(sp["glossary"]) + 1)], (sp["slug"], dom_ids)
        ids_defined = set(dom_ids)
        expected_ids = {g["id"] for g in sp["glossary"]}
        assert ids_defined == expected_ids, (sp["slug"], ids_defined, expected_ids)
        inline_spans = re.findall(r'<span class="inline-term"([^>]*)>(.*?)</span>', web, re.S)
        assert inline_spans, f"No inline terms found in {sp['slug']}"
        referenced_ids: set[str] = set()
        for attrs, label in inline_spans:
            m = re.search(r'data-glossary-target="([^"]+)"', attrs)
            assert m and m.group(1) in ids_defined, (sp["slug"], attrs, label)
            referenced_ids.add(m.group(1))
            assert 'aria-expanded="false"' in attrs, f"Missing aria-expanded in {sp['slug']} on {label}"
            assert 'aria-controls="term-popover"' in attrs, f"Missing aria-controls in {sp['slug']} on {label}"
        assert referenced_ids == ids_defined, f"Orphaned glossary IDs in {sp['slug']}: {ids_defined - referenced_ids}"
        total_inline += len(inline_spans)

    print(
        f"[PASS] WP:AISIGNS discipline clean across all {len(files_to_scan)} files "
        f"(zero em dashes, '--', curly quotes, or banned AI words); {total_inline} inline terms verified across 6 Spokes."
    )


# ---------------------------------------------------------------------------
# 3. PDF page bands, synced page labels, and OG image verification
# ---------------------------------------------------------------------------

def check_pdfs_and_labels():
    hub_pdf = AI_DIR / data.HUB["pdf_filename"]
    hub_pages = count_pdf_pages(hub_pdf)
    assert 2 <= hub_pages <= 3, f"Hub PDF page count {hub_pages} outside 2-3 range"

    spoke_pages: dict[str, int] = {}
    for sp in data.SPOKES:
        pdf_path = AI_DIR / sp["slug"] / sp["pdf_filename"]
        pages = count_pdf_pages(pdf_path)
        assert 2 <= pages <= 4, f"Spoke {sp['slug']} PDF page count {pages} outside 2-4 range"
        spoke_pages[sp["slug"]] = pages
        spoke_web = (AI_DIR / sp["slug"] / "index.html").read_text(encoding="utf-8")
        assert f"Download PDF ({pages} pp.)" in spoke_web, f"Missing/stale page label in {sp['slug']}/index.html"

    root_html = (REPO / "index.html").read_text(encoding="utf-8")
    hub_web = (AI_DIR / "index.html").read_text(encoding="utf-8")
    readme = (REPO / "README.md").read_text(encoding="utf-8")

    assert f"Overview PDF ({hub_pages} pp.)" in root_html
    assert f"Executive overview ({hub_pages} pp.)" in root_html
    assert f"Download Overview PDF ({hub_pages} pp.)" in hub_web
    assert f"Executive Overview PDF ({hub_pages} pages)" in readme

    for sp in data.SPOKES:
        p = spoke_pages[sp["slug"]]
        assert f"PDF ({p} pp.)" in hub_web, f"Missing PDF ({p} pp.) for {sp['slug']} in Hub web"
        assert f"PDF ({p}p)" in root_html, f"Missing PDF ({p}p) for {sp['slug']} in Root archive"
        assert f"({p} pp.)" in readme, f"Missing ({p} pp.) for {sp['slug']} in README"

    expected_ogs = [ASSETS_DIR / "og-index.png", ASSETS_DIR / data.HUB["og_filename"]] + [
        ASSETS_DIR / sp["og_filename"] for sp in data.SPOKES
    ]
    for og in expected_ogs:
        assert og.is_file() and og.stat().st_size > 100_000, f"Invalid OG asset {og}"

    summary = ", ".join(f"{sp['num']}:{spoke_pages[sp['slug']]}p" for sp in data.SPOKES)
    print(f"[PASS] PDFs & OG assets verified: Hub={hub_pages}p, Spokes=[{summary}], {len(expected_ogs)} OG PNGs (>100KB).")


# ---------------------------------------------------------------------------
# 4. Headless Chromium CDP behavioral checks (via file://)
# ---------------------------------------------------------------------------

def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class SimpleWS:
    """Minimal RFC 6455 text-frame client over stdlib socket for local CDP."""

    def __init__(self, url: str):
        parsed = urllib.parse.urlparse(url)
        host = parsed.hostname or "127.0.0.1"
        port = parsed.port or 80
        path = parsed.path or "/"
        self.sock = socket.create_connection((host, port), timeout=15)
        key = base64.b64encode(os.urandom(16)).decode("ascii")
        req = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {host}:{port}\r\n"
            f"Upgrade: websocket\r\n"
            f"Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            f"Sec-WebSocket-Version: 13\r\n\r\n"
        )
        self.sock.sendall(req.encode("ascii"))
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.sock.recv(4096)
        assert b"101 " in buf.split(b"\r\n", 1)[0], buf

    def _recv_exact(self, n: int) -> bytes:
        out = bytearray()
        while len(out) < n:
            chunk = self.sock.recv(n - len(out))
            if not chunk:
                raise EOFError("WebSocket closed")
            out.extend(chunk)
        return bytes(out)

    def send(self, text: str) -> None:
        payload = text.encode("utf-8")
        mask = os.urandom(4)
        header = bytearray([0x81])
        length = len(payload)
        if length < 126:
            header.append(0x80 | length)
        elif length < 65536:
            header.append(0x80 | 126)
            header.extend(struct.pack("!H", length))
        else:
            header.append(0x80 | 127)
            header.extend(struct.pack("!Q", length))
        header.extend(mask)
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        self.sock.sendall(bytes(header) + masked)

    def recv(self) -> str:
        chunks = []
        while True:
            b1, b2 = self._recv_exact(2)
            fin = (b1 & 0x80) != 0
            opcode = b1 & 0x0F
            length = b2 & 0x7F
            if length == 126:
                length = struct.unpack("!H", self._recv_exact(2))[0]
            elif length == 127:
                length = struct.unpack("!Q", self._recv_exact(8))[0]
            if b2 & 0x80:
                mask = self._recv_exact(4)
                data_bytes = bytes(b ^ mask[i % 4] for i, b in enumerate(self._recv_exact(length)))
            else:
                data_bytes = self._recv_exact(length)
            if opcode == 0x8:
                raise EOFError("Close frame")
            if opcode == 0x9:
                continue
            chunks.append(data_bytes)
            if fin:
                return b"".join(chunks).decode("utf-8")

    def close(self) -> None:
        self.sock.close()


def cdp_eval(ws: SimpleWS, msg_counter: list[int], expr: str, console_errors: list) -> object:
    msg_counter[0] += 1
    cid = msg_counter[0]
    ws.send(json.dumps({
        "id": cid,
        "method": "Runtime.evaluate",
        "params": {"expression": expr, "returnByValue": True, "awaitPromise": True},
    }))
    while True:
        raw = ws.recv()
        msg = json.loads(raw)
        if msg.get("method") == "Runtime.consoleAPICalled":
            params = msg.get("params", {})
            if params.get("type") == "error":
                console_errors.append(params.get("args"))
        elif msg.get("method") == "Runtime.exceptionThrown":
            console_errors.append(msg.get("params"))
        if msg.get("id") == cid:
            if "error" in msg:
                raise RuntimeError(msg["error"])
            res = msg["result"]
            if "exceptionDetails" in res:
                raise RuntimeError(res["exceptionDetails"])
            return res.get("result", {}).get("value")


def check_browser():
    cdp_port = free_port()
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmpdir:
        proc = subprocess.Popen(
            [
                CHROME_BIN,
                "--headless",
                "--no-sandbox",
                "--disable-gpu",
                "--host-resolver-rules=MAP fonts.googleapis.com ~NOTFOUND, MAP fonts.gstatic.com ~NOTFOUND",
                f"--user-data-dir={tmpdir}",
                f"--remote-debugging-port={cdp_port}",
                "about:blank",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            targets = None
            for _ in range(40):
                try:
                    with urllib.request.urlopen(f"http://127.0.0.1:{cdp_port}/json/list", timeout=1) as resp:
                        all_t = json.loads(resp.read().decode())
                        pages = [t for t in all_t if t.get("type") == "page"]
                        if pages:
                            targets = pages
                            break
                except Exception:
                    time.sleep(0.15)
            assert targets, "No CDP page target appeared"
            ws = SimpleWS(targets[0]["webSocketDebuggerUrl"])
            cnt = [0]
            console_errors: list = []

            def send_wait(method: str, params=None):
                cnt[0] += 1
                cid = cnt[0]
                ws.send(json.dumps({"id": cid, "method": method, "params": params or {}}))
                while True:
                    d = json.loads(ws.recv())
                    if d.get("id") == cid:
                        return d

            def nav(url: str, expected_path_substr: str, require_theme_btn: bool = True):
                send_wait("Page.enable")
                send_wait("Runtime.enable")
                nav_res = send_wait("Page.navigate", {"url": url})
                last_state = None
                for _ in range(120):
                    try:
                        last_state = cdp_eval(
                            ws,
                            cnt,
                            "({href: window.location.href, rs: document.readyState, ready: !!document.getElementById('theme-toggle-btn')})",
                            console_errors,
                        )
                    except RuntimeError:
                        # Context can be briefly unavailable mid-redirect
                        time.sleep(0.05)
                        continue
                    if (
                        last_state["rs"] in ("interactive", "complete")
                        and expected_path_substr in last_state["href"]
                        and (last_state["ready"] or not require_theme_btn)
                    ):
                        return last_state["href"]
                    time.sleep(0.08)
                raise TimeoutError(f"Page never finished loading ({url} -> {expected_path_substr}); nav_res={nav_res}; last_state={last_state}")

            # 1. Root index.html: .archive-controls hidden at 1 entry, flex at 2
            nav(f"file://{REPO / 'index.html'}", "/policy-briefs/index.html")
            root_state = cdp_eval(ws, cnt, """(() => {
              const ctrl = document.querySelector('.archive-controls');
              const firstDisp = getComputedStyle(ctrl).display;
              const firstHidden = ctrl.hidden;
              const spokes = document.querySelectorAll('.series-spoke-item').length;
              const entry = document.querySelector('.archive-entry');
              entry.parentNode.appendChild(entry.cloneNode(true));
              ctrl.hidden = document.querySelectorAll('.archive-entry').length <= 1;
              return {
                firstDisp,
                firstHidden,
                secondDisp: getComputedStyle(ctrl).display,
                spokes,
              };
            })()""", console_errors)
            assert root_state == {"firstDisp": "none", "firstHidden": True, "secondDisp": "flex", "spokes": 6}, root_state

            # 2. Legacy hash redirects (navigate via about:blank so same-file fragments do a fresh load)
            send_wait("Page.navigate", {"url": "about:blank"})
            r1 = nav(f"file://{REPO / 'index.html'}#term-8", "/ai-governance/power-water/#term-3", require_theme_btn=False)
            send_wait("Page.navigate", {"url": "about:blank"})
            r2 = nav(f"file://{AI_DIR / 'index.html'}#term-8", "/ai-governance/power-water/#term-3", require_theme_btn=False)
            send_wait("Page.navigate", {"url": "about:blank"})
            r3 = nav(f"file://{REPO / 'index.html'}#safety-youth-pace", "/ai-governance/#safety-youth-pace", require_theme_btn=False)
            assert r1.endswith("/ai-governance/power-water/#term-3"), r1
            assert r2.endswith("/ai-governance/power-water/#term-3"), r2
            assert r3.endswith("/ai-governance/#safety-youth-pace"), r3
            assert 'id="term-3"' in (AI_DIR / "power-water" / "index.html").read_text(encoding="utf-8")
            assert 'id="safety-youth-pace"' in (AI_DIR / "index.html").read_text(encoding="utf-8")

            # 3. Hub page check
            nav(f"file://{AI_DIR / 'index.html'}", "/ai-governance/index.html")
            hub_check = cdp_eval(ws, cnt, """(() => {
              const active = document.querySelector('.series-pill[aria-current="page"]');
              return {
                activeHref: active ? active.getAttribute('href') : null,
                pillars: document.querySelectorAll('section.brief-section .spoke-callout').length,
                tradeoffs: document.querySelectorAll('#trade-offs .tradeoff-card').length,
              };
            })()""", console_errors)
            assert hub_check == {"activeHref": "./", "pillars": 6, "tradeoffs": 6}, hub_check

            # 4. All 6 Spokes: popovers, keyboard Enter/Escape, glossary category pills + search, series nav highlight
            tested_popovers = 0
            for sp in data.SPOKES:
                slug = sp["slug"]
                expected_total = len(sp["glossary"])
                nav(f"file://{AI_DIR / slug / 'index.html'}", f"/ai-governance/{slug}/index.html")

                # Series nav active state + popover clicks + keyboard focus/restore + filters
                sp_res = cdp_eval(ws, cnt, f"""(() => {{
                  const active = document.querySelector('.series-pill[aria-current="page"]');
                  const terms = Array.from(document.querySelectorAll('.inline-term'));
                  const pop = document.getElementById('term-popover');
                  const results = [];
                  for (const t of terms) {{
                    t.click();
                    results.push({{
                      text: t.textContent.trim(),
                      target: t.getAttribute('data-glossary-target'),
                      expanded: t.getAttribute('aria-expanded'),
                      hidden: pop.hidden,
                      title: document.getElementById('term-popover-title').textContent.trim(),
                      bodyLen: document.getElementById('term-popover-body').textContent.trim().length,
                      linkHref: document.getElementById('term-popover-link').getAttribute('href'),
                    }});
                  }}

                  // Keyboard Enter opens & focuses #term-popover; Escape closes & restores focus
                  document.dispatchEvent(new KeyboardEvent('keydown', {{key: 'Escape'}}));
                  const first = terms[0];
                  first.focus();
                  first.dispatchEvent(new KeyboardEvent('keydown', {{key: 'Enter', bubbles: true}}));
                  const openedFocus = document.activeElement && document.activeElement.id;
                  document.dispatchEvent(new KeyboardEvent('keydown', {{key: 'Escape', bubbles: true}}));
                  const restoredFocus = document.activeElement === first;
                  const anyOpen = terms.some(t => t.getAttribute('aria-expanded') === 'true');

                  // Category pills & search
                  const catCounts = {{}};
                  for (const pill of document.querySelectorAll('.filter-pill')) {{
                    pill.click();
                    catCounts[pill.getAttribute('data-cat')] = document.getElementById('glossary-count').textContent;
                  }}
                  document.querySelector('.filter-pill[data-cat="all"]').click();
                  const search = document.getElementById('glossary-filter');
                  search.value = 'zzzzunlikelyterm99';
                  search.dispatchEvent(new Event('input', {{bubbles: true}}));
                  const emptyDisp = getComputedStyle(document.getElementById('glossary-empty')).display;
                  search.value = '';
                  search.dispatchEvent(new Event('input', {{bubbles: true}}));
                  const resetCount = document.getElementById('glossary-count').textContent;

                  return {{
                    activeHref: active ? active.getAttribute('href') : null,
                    activeText: active ? active.textContent.trim() : null,
                    termCount: terms.length,
                    results,
                    kb: {{openedFocus, restoredFocus, closed: pop.hidden && !anyOpen}},
                    catCounts,
                    emptyDisp,
                    resetCount,
                  }};
                }})()""", console_errors)

                assert sp_res["activeHref"] == "./" and sp["nav_label"] in (sp_res["activeText"] or ""), (slug, sp_res)
                assert sp_res["termCount"] > 0, slug
                for r in sp_res["results"]:
                    assert r["expanded"] == "true" and r["hidden"] is False, (slug, r)
                    assert r["title"] and r["bodyLen"] > 20, (slug, r)
                    assert r["linkHref"] == f"#{r['target']}", (slug, r)
                tested_popovers += len(sp_res["results"])

                assert sp_res["kb"] == {"openedFocus": "term-popover", "restoredFocus": True, "closed": True}, (slug, sp_res["kb"])
                assert sp_res["catCounts"]["all"] == f"Showing {expected_total} of {expected_total} entries", (slug, sp_res["catCounts"])
                for cat, _ in sp["glossary_groups"]:
                    cat_total = sum(1 for g in sp["glossary"] if g["cat"] == cat)
                    assert sp_res["catCounts"][cat] == f"Showing {cat_total} of {expected_total} entries", (slug, cat, sp_res["catCounts"])
                assert sp_res["emptyDisp"] == "block", (slug, sp_res["emptyDisp"])
                assert sp_res["resetCount"] == f"Showing {expected_total} of {expected_total} entries", (slug, sp_res["resetCount"])

            assert not console_errors, f"Console errors observed: {console_errors}"
            ws.close()
            print(
                f"[PASS] Headless Chromium CDP verified root index controls, 3 legacy hash redirects, "
                f"Hub layout, all 6 Spokes, {tested_popovers} inline-term popovers, keyboard Enter/Escape, "
                f"all scoped category filters/search, and zero console errors."
            )
        finally:
            proc.terminate()
            proc.wait(timeout=5)


def main() -> int:
    check_parity()
    check_wp_aisigns_and_terms()
    check_pdfs_and_labels()
    check_browser()
    print("[ALL PASS] 1 + 6 Hub-and-Spoke verification succeeded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
