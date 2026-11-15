#!/usr/bin/env python3
"""Generate all Markdown sources, print HTML, PDFs, web readers, OG PNGs, root index, and README from series_data.py."""

from __future__ import annotations

import html as html_lib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import series_data as data  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
AI_DIR = REPO / "ai-governance"
ASSETS_DIR = REPO / "assets"
CHROME_BIN = Path("/home/mike10010100/.cache/ms-playwright/chromium-1248/chrome-linux64/chrome")
LEGACY_CHROME = Path("/usr/bin/google-chrome")

TOKEN_RE = re.compile(r"\[\[([^\]]+)\]\]")
ITALIC_RE = re.compile(r"\*([^*]+)\*")


def chrome_executable() -> str:
    if CHROME_BIN.exists():
        return str(CHROME_BIN)
    if LEGACY_CHROME.exists():
        return str(LEGACY_CHROME)
    raise FileNotFoundError(f"Chromium binary not found at {CHROME_BIN}")


def count_pdf_pages(pdf_path: Path) -> int:
    raw = pdf_path.read_bytes()
    pages = re.findall(rb"/Type\s*/Page(?!s)\b", raw)
    if not pages:
        raise RuntimeError(f"Zero pages detected in {pdf_path}")
    return len(pages)


def parse_token(raw_token: str, glossary_map: dict[str, dict]) -> tuple[str, str, str | None, str | None]:
    parts = raw_token.split("|")
    if len(parts) == 2:
        tid, label = parts
        assert tid in glossary_map, f"Unknown glossary token target {tid!r}"
        return tid, label, None, None
    if len(parts) == 3:
        tid, label, body = parts
        assert tid in glossary_map, f"Unknown glossary token target {tid!r}"
        title = label[0].upper() + label[1:] if label and label[0].islower() else label
        return tid, label, title, body
    if len(parts) == 4:
        tid, label, title, body = parts
        assert tid in glossary_map, f"Unknown glossary token target {tid!r}"
        return tid, label, title, body
    raise ValueError(f"Invalid inline token syntax: {raw_token!r}")


def render_md_inline(text: str, glossary_map: dict[str, dict] | None = None) -> str:
    def _sub(match: re.Match[str]) -> str:
        raw_tok = match.group(1)
        if glossary_map is not None:
            _, label, _, _ = parse_token(raw_tok, glossary_map)
            return label
        return raw_tok.split("|")[1]

    return TOKEN_RE.sub(_sub, text)


def _format_italics_and_escape(segment: str) -> str:
    out: list[str] = []
    pos = 0
    for m in ITALIC_RE.finditer(segment):
        if m.start() > pos:
            out.append(html_lib.escape(segment[pos : m.start()], quote=False))
        out.append(f"<em>{html_lib.escape(m.group(1), quote=False)}</em>")
        pos = m.end()
    if pos < len(segment):
        out.append(html_lib.escape(segment[pos:], quote=False))
    return "".join(out)


def render_print_inline(text: str, glossary_map: dict[str, dict] | None = None) -> str:
    return _format_italics_and_escape(render_md_inline(text, glossary_map))


def render_web_inline(text: str, glossary_map: dict[str, dict]) -> str:
    out: list[str] = []
    pos = 0
    for m in TOKEN_RE.finditer(text):
        if m.start() > pos:
            out.append(_format_italics_and_escape(text[pos : m.start()]))
        tid, label, override_title, override_body = parse_token(m.group(1), glossary_map)
        attrs = [
            'class="inline-term"',
            'tabindex="0"',
            'role="button"',
            'aria-expanded="false"',
            'aria-controls="term-popover"',
            f'data-glossary-target="{html_lib.escape(tid, quote=True)}"',
        ]
        if override_title:
            attrs.append(f'data-popover-title="{html_lib.escape(override_title, quote=True)}"')
        if override_body:
            attrs.append(f'data-popover-body="{html_lib.escape(override_body, quote=True)}"')
        out.append(f"<span {' '.join(attrs)}>{_format_italics_and_escape(label)}</span>")
        pos = m.end()
    if pos < len(text):
        out.append(_format_italics_and_escape(text[pos:]))
    return "".join(out)


def h(s: str) -> str:
    return html_lib.escape(s, quote=True)


def h_text(s: str) -> str:
    return html_lib.escape(s, quote=False)


SVG_DOWNLOAD = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />'
    '<polyline points="7 10 12 15 17 10" />'
    '<line x1="12" y1="15" x2="12" y2="3" />'
    "</svg>"
)

SVG_BOOK = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />'
    '<path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />'
    "</svg>"
)

SVG_MD = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />'
    '<polyline points="14 2 14 8 20 8" />'
    '<line x1="16" y1="13" x2="8" y2="13" />'
    '<line x1="16" y1="17" x2="8" y2="17" />'
    "</svg>"
)

SVG_GH = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 '
    '6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 '
    '0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 '
    '5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" />'
    "</svg>"
)

THEME_BOOT_SCRIPT = """  <script>
    (function () {
      try {
        var params = new URLSearchParams(window.location.search);
        var queryTheme = params.get("theme");
        var saved = localStorage.getItem("ai-brief-theme");
        var theme = (queryTheme === "dark" || queryTheme === "light")
          ? queryTheme
          : (saved === "dark" || saved === "light"
            ? saved
            : (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"));
        document.documentElement.setAttribute("data-theme", theme);
      } catch (e) {}
    })();
  </script>"""

COMMON_READER_JS = """  <script>
    (function () {
      var root = document.documentElement;
      var themeBtn = document.getElementById("theme-toggle-btn");
      var copyPageBtn = document.getElementById("copy-page-btn");
      var toast = document.getElementById("copy-toast");
      var progressBar = document.getElementById("reading-progress");
      var toastTimer = null;

      function syncThemeButton() {
        var current = root.getAttribute("data-theme") || "light";
        themeBtn.textContent = current === "dark" ? "Light Mode" : "Dark Mode";
      }

      syncThemeButton();

      themeBtn.addEventListener("click", function () {
        var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        try {
          localStorage.setItem("ai-brief-theme", next);
        } catch (e) {}
        syncThemeButton();
      });

      function updateProgressBar() {
        if (!progressBar) return;
        var scrollTop = window.scrollY || document.documentElement.scrollTop || 0;
        var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        var pct = docHeight > 0 ? Math.min(100, Math.max(0, (scrollTop / docHeight) * 100)) : 0;
        progressBar.style.width = pct.toFixed(1) + "%";
      }

      updateProgressBar();
      window.addEventListener("scroll", updateProgressBar, { passive: true });
      window.addEventListener("resize", updateProgressBar, { passive: true });

      function showToast(msg) {
        toast.textContent = msg;
        toast.classList.add("visible");
        clearTimeout(toastTimer);
        toastTimer = setTimeout(function () {
          toast.classList.remove("visible");
        }, 1800);
      }

      function copyText(text, label) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(function () {
            showToast(label || "Link copied");
          }).catch(function () {
            showToast("Link ready in address bar");
          });
        } else {
          var temp = document.createElement("input");
          temp.value = text;
          document.body.appendChild(temp);
          temp.select();
          try {
            document.execCommand("copy");
            showToast(label || "Link copied");
          } catch (e) {
            showToast("Copy unavailable");
          }
          document.body.removeChild(temp);
        }
      }

      copyPageBtn.addEventListener("click", function () {
        var cleanUrl = window.location.origin + window.location.pathname;
        if (window.location.protocol === "file:") {
          cleanUrl = window.location.href.split("#")[0].split("?")[0];
        }
        copyText(cleanUrl, "Page link copied");
      });

      document.querySelectorAll(".copy-anchor-btn").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var anchor = btn.getAttribute("data-anchor");
          var base = window.location.href.split("#")[0];
          history.replaceState(null, "", anchor);
          copyText(base + anchor, "Link copied");
        });
      });

      var mobileDetails = document.querySelector(".mobile-toc details");
      if (mobileDetails) {
        mobileDetails.querySelectorAll("a").forEach(function (link) {
          link.addEventListener("click", function () {
            mobileDetails.removeAttribute("open");
          });
        });
      }

      var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc-link"));
      var sections = tocLinks.map(function (link) {
        return document.querySelector(link.getAttribute("href"));
      }).filter(Boolean);

      if ("IntersectionObserver" in window && sections.length) {
        var observer = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              var id = "#" + entry.target.id;
              tocLinks.forEach(function (link) {
                link.classList.toggle("active", link.getAttribute("href") === id);
              });
            }
          });
        }, { rootMargin: "-15% 0px -70% 0px" });

        sections.forEach(function (sec) {
          observer.observe(sec);
        });
      }

      var filterInput = document.getElementById("glossary-filter");
      var countEl = document.getElementById("glossary-count");
      var emptyEl = document.getElementById("glossary-empty");
      var categoryBtns = Array.prototype.slice.call(document.querySelectorAll(".filter-pill"));
      var groups = Array.prototype.slice.call(document.querySelectorAll("[data-group]"));
      var entries = Array.prototype.slice.call(document.querySelectorAll("[data-entry]"));
      var activeCategory = "all";

      function setActiveCategory(cat) {
        activeCategory = cat;
        categoryBtns.forEach(function (btn) {
          btn.classList.toggle("active", btn.getAttribute("data-cat") === cat);
        });
      }

      function applyGlossaryFilters() {
        var q = filterInput ? filterInput.value.trim().toLowerCase() : "";
        var visibleCount = 0;

        entries.forEach(function (entry) {
          var matchesCat = activeCategory === "all" || entry.getAttribute("data-category") === activeCategory;
          var matchesSearch = !q || entry.textContent.toLowerCase().indexOf(q) !== -1;
          var show = matchesCat && matchesSearch;
          entry.style.display = show ? "" : "none";
          if (show) visibleCount += 1;
        });

        groups.forEach(function (group) {
          var hasVisible = Array.prototype.some.call(
            group.querySelectorAll("[data-entry]"),
            function (card) { return card.style.display !== "none"; }
          );
          group.style.display = hasVisible ? "" : "none";
        });

        if (countEl) {
          countEl.textContent = "Showing " + visibleCount + " of " + entries.length + " entries";
        }
        if (emptyEl) {
          emptyEl.style.display = visibleCount === 0 ? "block" : "none";
        }
      }

      categoryBtns.forEach(function (btn) {
        btn.addEventListener("click", function () {
          setActiveCategory(btn.getAttribute("data-cat") || "all");
          applyGlossaryFilters();
        });
      });

      if (filterInput) {
        filterInput.addEventListener("input", applyGlossaryFilters);
      }

      var popover = document.getElementById("term-popover");
      var popoverTitle = document.getElementById("term-popover-title");
      var popoverBody = document.getElementById("term-popover-body");
      var popoverClose = document.getElementById("term-popover-close");
      var popoverLink = document.getElementById("term-popover-link");
      var activeTermEl = null;
      var openedViaKeyboard = false;
      var pulseTimer = null;
      var openScrollY = 0;
      var openTimestamp = 0;

      function closePopover(restoreFocus) {
        if (!popover) return;
        popover.classList.remove("visible");
        popover.hidden = true;
        if (activeTermEl) {
          var prevTermEl = activeTermEl;
          prevTermEl.classList.remove("is-open");
          prevTermEl.setAttribute("aria-expanded", "false");
          activeTermEl = null;
          if (restoreFocus && openedViaKeyboard) {
            prevTermEl.focus({ preventScroll: true });
          }
        }
        openedViaKeyboard = false;
      }

      function positionPopover(termEl) {
        var rect = termEl.getBoundingClientRect();
        var popWidth = popover.offsetWidth || 340;
        var popHeight = popover.offsetHeight || 160;
        var left = rect.left + (rect.width / 2) - (popWidth / 2);
        left = Math.max(12, Math.min(left, window.innerWidth - popWidth - 12));
        var top = rect.bottom + 8;
        if (top + popHeight > window.innerHeight - 12) {
          top = Math.max(12, rect.top - popHeight - 8);
        }
        popover.style.left = Math.round(left) + "px";
        popover.style.top = Math.round(top) + "px";
      }

      function openPopover(termEl, viaKeyboard) {
        if (!popover) return;
        if (activeTermEl === termEl && !popover.hidden) {
          closePopover(!!viaKeyboard);
          return;
        }
        var targetId = termEl.getAttribute("data-glossary-target");
        var card = targetId ? document.getElementById(targetId) : null;
        if (!card) return;
        var dt = card.querySelector("dt");
        var dd = card.querySelector("dd");
        if (!dt || !dd) return;

        if (activeTermEl) {
          activeTermEl.classList.remove("is-open");
          activeTermEl.setAttribute("aria-expanded", "false");
        }
        activeTermEl = termEl;
        openedViaKeyboard = !!viaKeyboard;
        activeTermEl.classList.add("is-open");
        activeTermEl.setAttribute("aria-expanded", "true");
        popoverTitle.textContent = termEl.getAttribute("data-popover-title") || dt.textContent;
        popoverBody.textContent = termEl.getAttribute("data-popover-body") || dd.textContent;
        popoverLink.setAttribute("href", "#" + targetId);

        openScrollY = window.scrollY || document.documentElement.scrollTop || 0;
        openTimestamp = Date.now();
        popover.hidden = false;
        positionPopover(termEl);
        popover.classList.add("visible");
        if (openedViaKeyboard) {
          popover.focus({ preventScroll: true });
        }
      }

      document.querySelectorAll(".inline-term").forEach(function (termEl) {
        termEl.addEventListener("click", function (e) {
          e.stopPropagation();
          openPopover(termEl, false);
        });
        termEl.addEventListener("keydown", function (e) {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            openPopover(termEl, true);
          }
        });
      });

      if (popoverClose) {
        popoverClose.addEventListener("click", function () {
          closePopover(true);
        });
      }

      if (popoverLink) {
        popoverLink.addEventListener("click", function (e) {
          e.preventDefault();
          var href = popoverLink.getAttribute("href");
          var targetId = href ? href.replace(/^#/, "") : "";
          var targetCard = targetId ? document.getElementById(targetId) : null;
          closePopover(false);
          if (!targetCard) return;
          if (targetCard.style.display === "none") {
            setActiveCategory("all");
            if (filterInput) filterInput.value = "";
            applyGlossaryFilters();
          }
          targetCard.scrollIntoView({ behavior: "smooth", block: "center" });
          document.querySelectorAll(".glossary-card.highlight-pulse").forEach(function (el) {
            el.classList.remove("highlight-pulse");
          });
          targetCard.classList.add("highlight-pulse");
          clearTimeout(pulseTimer);
          pulseTimer = setTimeout(function () {
            targetCard.classList.remove("highlight-pulse");
          }, 2200);
        });
      }

      document.addEventListener("click", function (e) {
        if (!popover || popover.hidden) return;
        if (!popover.contains(e.target) && !e.target.classList.contains("inline-term")) {
          closePopover(false);
        }
      });

      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") {
          closePopover(true);
        }
      });

      window.addEventListener("scroll", function () {
        if (!popover || popover.hidden) return;
        if (Date.now() - openTimestamp < 180) return;
        var curScrollY = window.scrollY || document.documentElement.scrollTop || 0;
        if (Math.abs(curScrollY - openScrollY) > 80) {
          closePopover(false);
        }
      }, { passive: true });
    })();
  </script>"""


def build_series_nav_html(active_slug: str | None) -> str:
    prefix = "./" if active_slug is None else "../"
    items: list[str] = []
    ov_cls = "series-pill active" if active_slug is None else "series-pill"
    ov_aria = ' aria-current="page"' if active_slug is None else ""
    items.append(f'<a class="{ov_cls}" href="{prefix}"{ov_aria}>Overview</a>')
    for sp in data.SPOKES:
        is_cur = active_slug == sp["slug"]
        cls = "series-pill active" if is_cur else "series-pill"
        aria = ' aria-current="page"' if is_cur else ""
        href = "./" if is_cur else f"{prefix}{sp['slug']}/"
        items.append(
            f'<a class="{cls}" href="{href}"{aria}>'
            f'<span class="series-pill-num">{sp["num"]}</span>'
            f'<span>{h_text(sp["nav_label"])}</span></a>'
        )
    return (
        '  <nav class="series-nav-strip" aria-label="Series 2026-01 issue briefs">\n'
        '    <div class="series-nav-inner">\n'
        '      <span class="series-nav-label">Series 2026-01:</span>\n'
        f'      {"\n      ".join(items)}\n'
        "    </div>\n"
        "  </nav>"
    )


def build_hub_md() -> str:
    hub = data.HUB
    lines = [
        "**POLICY BRIEF SERIES · EXECUTIVE OVERVIEW**",
        f"Series: {hub['code']} · {hub['title']}",
        f"Prepared by: {data.SITE['author']}",
        f"Date: {data.SITE['date']}",
        f"Subject: {hub['subtitle']} across six federal AI pillars",
        "",
        "### Bottom line up front",
        "",
    ]
    for p in hub["bluf_paragraphs"]:
        lines.extend([render_md_inline(p), ""])
    lines.extend([render_md_inline(hub["bluf_goal"]), ""])

    spoke_by_slug = {sp["slug"]: sp for sp in data.SPOKES}
    for pil in hub["pillars"]:
        sp = spoke_by_slug[pil["spoke_slug"]]
        lines.extend([f"### {pil['heading']}", "", render_md_inline(pil["lead"]), ""])
        for b in pil["bullets"]:
            lines.append(f"* {render_md_inline(b)}")
        lines.extend(
            [
                "",
                f"Full issue brief ({sp['code']}): [{sp['title']}](./{sp['slug']}/{sp['md_filename']})",
                "",
            ]
        )

    lines.extend(["### Trade-offs to weigh in policy design", ""])
    for tr in hub["tradeoffs"]:
        lines.extend([f"**{tr['eyebrow']}**", render_md_inline(tr["body"]), ""])

    lines.extend(["---", "Key references for staff follow-up:"])
    for ref in hub["references"]:
        lines.append(f"* {render_md_inline(ref)}")
    lines.append("")
    return "\n".join(lines)


def build_hub_print_html() -> str:
    hub = data.HUB
    spoke_by_slug = {sp["slug"]: sp for sp in data.SPOKES}

    bluf_html = "\n".join(
        [f"      <p>{render_print_inline(p)}</p>" for p in hub["bluf_paragraphs"]]
        + [f"      <p>{render_print_inline(hub['bluf_goal'])}</p>"]
    )

    sec_blocks: list[str] = []
    for pil in hub["pillars"]:
        sp = spoke_by_slug[pil["spoke_slug"]]
        bullets_html = "\n".join(f"        <li>{render_print_inline(b)}</li>" for b in pil["bullets"])
        sec_blocks.append(
            f"    <section class=\"pillar-block\">\n"
            f"      <h3>{h_text(pil['heading'])}</h3>\n"
            f"      <p>{render_print_inline(pil['lead'])}</p>\n"
            f"      <ul class=\"pillar-bullets\">\n{bullets_html}\n      </ul>\n"
            f'      <p class="deep-dive-note">Full issue brief ({sp["code"]}): {h_text(sp["title"])} ({h_text(sp["slug"])}/{h_text(sp["pdf_filename"])})</p>\n'
            f"    </section>"
        )

    tr_blocks = "\n".join(
        f'      <div class="tradeoff-print-item">\n'
        f'        <div class="tradeoff-print-eyebrow">{h_text(tr["eyebrow"])}</div>\n'
        f"        <p>{render_print_inline(tr['body'])}</p>\n"
        f"      </div>"
        for tr in hub["tradeoffs"]
    )
    refs_html = "\n".join(f"        <li>{render_print_inline(r)}</li>" for r in hub["references"])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Policy Brief Series Overview - {h_text(hub['title'])}</title>
  <style>
    @page {{
      size: letter;
      margin: 0.46in 0.6in 0.54in 0.6in;
      @bottom-left {{
        content: "POLICY BRIEF SERIES 2026-01  |  MICHAEL PAULAUSKI  |  {data.SITE['date_upper']}";
        font-family: 'Liberation Sans', sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        letter-spacing: 0.03em;
      }}
      @bottom-right {{
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Liberation Sans', sans-serif;
        font-size: 7.5pt;
        color: #64748b;
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 0;
      font-family: 'Noto Serif', 'Liberation Serif', Georgia, serif;
      font-size: 9.2pt;
      line-height: 1.33;
      color: #111827;
      background: #ffffff;
    }}
    .header-block {{
      border-top: 2.5pt solid #0f172a;
      border-bottom: 0.75pt solid #cbd5e1;
      padding: 6pt 0 5pt 0;
      margin-bottom: 7pt;
    }}
    .doc-label {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 9.6pt;
      font-weight: 700;
      letter-spacing: 0.11em;
      text-transform: uppercase;
      color: #0f172a;
      margin: 0 0 4pt 0;
    }}
    .meta-table {{
      border-collapse: collapse;
      width: 100%;
      font-family: 'Liberation Sans', sans-serif;
      font-size: 8.6pt;
      line-height: 1.28;
      color: #1e293b;
    }}
    .meta-table td {{ padding: 0.8pt 0; vertical-align: top; }}
    .meta-label {{ width: 88pt; font-weight: 700; color: #334155; }}
    .bluf-box {{
      background: #f8fafc;
      border-left: 3pt solid #1e3a5f;
      padding: 6.5pt 10pt;
      margin: 0 0 7.5pt 0;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
    .bluf-box h3 {{ margin: 0 0 3pt 0; color: #1e3a5f; }}
    .bluf-box p:last-child {{ margin-bottom: 0; }}
    .pillar-block {{
      margin-bottom: 6.5pt;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    h3 {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 9.8pt;
      font-weight: 700;
      color: #0f172a;
      margin: 7pt 0 2.5pt 0;
      line-height: 1.22;
      break-after: avoid;
      page-break-after: avoid;
    }}
    .pillar-block h3 {{ margin-top: 0; }}
    p {{ margin: 0 0 3.5pt 0; orphans: 3; widows: 3; text-align: left; }}
    ul.pillar-bullets {{
      margin: 0 0 3pt 0;
      padding-left: 13pt;
    }}
    ul.pillar-bullets li {{
      margin-bottom: 1.5pt;
    }}
    ul.pillar-bullets li:last-child {{ margin-bottom: 0; }}
    .deep-dive-note {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 7.9pt;
      color: #334155;
      margin: 0;
    }}
    .tradeoffs-section {{ margin-top: 7.5pt; }}
    .tradeoffs-print-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 5pt 10pt;
    }}
    .tradeoff-print-item {{
      border-top: 1pt solid #cbd5e1;
      padding-top: 3pt;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    .tradeoff-print-eyebrow {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 7.8pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #1e3a5f;
      margin-bottom: 1.5pt;
    }}
    .tradeoff-print-item p {{
      font-size: 8.35pt;
      line-height: 1.28;
      margin: 0;
    }}
    .references-block {{
      margin-top: 7.5pt;
      padding-top: 5.5pt;
      border-top: 0.75pt solid #cbd5e1;
      font-size: 7.9pt;
      line-height: 1.27;
      color: #334155;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    .references-title {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 8.3pt;
      font-weight: 700;
      color: #0f172a;
      margin: 0 0 2.5pt 0;
    }}
    .references-block ul {{ margin: 0; padding-left: 12pt; }}
    .references-block li {{ margin-bottom: 1.5pt; }}
  </style>
</head>
<body>
  <header class="header-block">
    <div class="doc-label">Policy Brief Series · Executive Overview</div>
    <table class="meta-table">
      <tr><td class="meta-label">Series:</td><td>{h_text(hub['code'])} · {h_text(hub['title'])}</td></tr>
      <tr><td class="meta-label">Prepared by:</td><td>{h_text(data.SITE['author'])}</td></tr>
      <tr><td class="meta-label">Date:</td><td>{h_text(data.SITE['date'])}</td></tr>
      <tr><td class="meta-label">Subject:</td><td>{h_text(hub['subtitle'])} across six federal AI pillars</td></tr>
    </table>
  </header>

  <section class="bluf-box">
    <h3>Bottom line up front</h3>
{bluf_html}
  </section>

{chr(10).join(sec_blocks)}

  <section class="tradeoffs-section">
    <h3>Trade-offs to weigh in policy design</h3>
    <div class="tradeoffs-print-grid">
{tr_blocks}
    </div>
  </section>

  <section class="references-block">
    <div class="references-title">Key references for staff follow-up:</div>
    <ul>
{refs_html}
    </ul>
  </section>
</body>
</html>
"""


def build_hub_web_html(pdf_pages: int, spoke_pdf_pages: dict[str, int]) -> str:
    hub = data.HUB
    spoke_by_slug = {sp["slug"]: sp for sp in data.SPOKES}

    legacy_redirect_js = (
        "      var termRedirects = "
        + json.dumps(data.LEGACY_TERM_REDIRECTS)
        + ";\n"
        "      var h = window.location.hash || \"\";\n"
        "      if (termRedirects[h]) {\n"
        "        window.location.replace(\"./\" + termRedirects[h]);\n"
        "        return;\n"
        "      }"
    )

    metrics_html = "\n".join(
        f'          <div class="stat-card">\n'
        f'            <div class="stat-figure">{h_text(m["figure"])}</div>\n'
        f'            <div class="stat-label">{h_text(m["label"])}</div>\n'
        f'            <div class="stat-cite">{h_text(m["cite"])}</div>\n'
        f"          </div>"
        for m in hub["metrics"]
    )

    mobile_links = [
        '        <li><a href="#bluf">Bottom line up front</a></li>',
        *[f'        <li><a href="#{pil["id"]}">{pil["toc_num"]}. {h_text(pil["toc_label"])}</a></li>' for pil in hub["pillars"]],
        '        <li><a href="#trade-offs">Trade-offs to weigh in policy design</a></li>',
        '        <li><a href="#references">Key references for staff follow-up</a></li>',
    ]

    toc_links = [
        '        <li><a class="toc-link" href="#bluf"><span class="toc-num">&bull;</span><span>Bottom line up front</span></a></li>',
        *[
            f'        <li><a class="toc-link" href="#{pil["id"]}"><span class="toc-num">{pil["toc_num"]}</span><span>{h_text(pil["toc_label"])}</span></a></li>'
            for pil in hub["pillars"]
        ],
        '        <li><a class="toc-link" href="#trade-offs"><span class="toc-num">&bull;</span><span>Policy trade-offs</span></a></li>',
        '        <li><a class="toc-link" href="#references"><span class="toc-num">&bull;</span><span>Key references</span></a></li>',
    ]

    bluf_ps = "\n".join(
        f'        <p data-verbatim>{render_print_inline(p)}</p>' for p in hub["bluf_paragraphs"]
    )

    pillar_sections: list[str] = []
    for pil in hub["pillars"]:
        sp = spoke_by_slug[pil["spoke_slug"]]
        sp_pages = spoke_pdf_pages[sp["slug"]]
        bullets_html = "\n".join(f"          <li>{render_print_inline(b)}</li>" for b in pil["bullets"])
        pillar_sections.append(
            f'      <section id="{pil["id"]}" class="brief-section">\n'
            f'        <div class="section-kicker">{h_text(pil["kicker"])}</div>\n'
            f'        <div class="section-head">\n'
            f'          <h2>{h_text(pil["heading"])}</h2>\n'
            f'          <button class="copy-anchor-btn" type="button" data-anchor="#{pil["id"]}" aria-label="Copy link to Pillar {pil["toc_num"]}"># Link</button>\n'
            f"        </div>\n"
            f'        <p data-verbatim>{render_print_inline(pil["lead"])}</p>\n'
            f'        <ul class="pillar-bullets" data-verbatim>\n{bullets_html}\n        </ul>\n'
            f'        <div class="spoke-callout">\n'
            f'          <div class="spoke-callout-meta">\n'
            f'            <span class="spoke-callout-kicker">{h_text(sp["code"])} · {h_text(sp["read_time"])} + {len(sp["glossary"])}-entry glossary</span>\n'
            f'            <span class="spoke-callout-title">{h_text(sp["title"])}</span>\n'
            f"          </div>\n"
            f'          <div class="spoke-callout-actions">\n'
            f'            <a class="btn btn-compact btn-primary" href="./{sp["slug"]}/">Read Issue Brief</a>\n'
            f'            <a class="btn btn-compact" href="./{sp["slug"]}/{sp["pdf_filename"]}">PDF ({sp_pages} pp.)</a>\n'
            f"          </div>\n"
            f"        </div>\n"
            f"      </section>"
        )

    tradeoff_cards = "\n".join(
        f'          <article class="tradeoff-card">\n'
        f'            <div class="tradeoff-eyebrow">{h_text(tr["eyebrow"])}</div>\n'
        f'            <p data-verbatim>{render_print_inline(tr["body"])}</p>\n'
        f"          </article>"
        for tr in hub["tradeoffs"]
    )

    refs_html = "\n".join(f"          <li>{render_print_inline(r)}</li>" for r in hub["references"])

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{h_text(hub['title'])} | Executive Overview by {h_text(data.SITE['author'])}</title>
  <meta name="description" content="{h(hub['meta_description'])}" />
  <link rel="canonical" href="{data.SITE['base_url']}/ai-governance/" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{h(hub['title'])} | {h(hub['subtitle'])}" />
  <meta property="og:description" content="{h(hub['og_description'])}" />
  <meta property="og:url" content="{data.SITE['base_url']}/ai-governance/" />
  <meta property="og:image" content="{data.SITE['base_url']}/assets/{hub['og_filename']}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{h(hub['title'])} | {h(hub['subtitle'])}" />
  <meta name="twitter:description" content="{h(hub['og_description'])}" />
  <meta name="twitter:image" content="{data.SITE['base_url']}/assets/{hub['og_filename']}" />

  <script>
    (function () {{
      try {{
{legacy_redirect_js}
        var params = new URLSearchParams(window.location.search);
        var queryTheme = params.get("theme");
        var saved = localStorage.getItem("ai-brief-theme");
        var theme = (queryTheme === "dark" || queryTheme === "light")
          ? queryTheme
          : (saved === "dark" || saved === "light"
            ? saved
            : (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"));
        document.documentElement.setAttribute("data-theme", theme);
      }} catch (e) {{}}
    }})();
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" /></noscript>
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
  <div id="reading-progress" class="reading-progress" aria-hidden="true"></div>

  <header id="top" class="site-header">
    <div class="header-inner">
      <div class="header-top-row">
        <div class="header-crumb-group">
          <a class="back-index-link" href="../">&larr; All Policy Briefs</a>
          <span class="doc-badge">{h_text(hub['code'])} &middot; Executive Overview</span>
        </div>
        <div class="utility-controls">
          <button id="copy-page-btn" class="btn btn-compact" type="button">Copy Page Link</button>
          <button id="theme-toggle-btn" class="btn btn-compact" type="button" aria-label="Toggle color theme">Dark Mode</button>
        </div>
      </div>

      <h1 class="site-title">{h_text(hub['title'])}</h1>

      <div class="meta-bar">
        <span class="meta-item">Prepared by <strong>{h_text(data.SITE['author'])}</strong></span>
        <span class="meta-sep" aria-hidden="true">&middot;</span>
        <span class="meta-item">{h_text(data.SITE['date'])}</span>
        <span class="meta-sep" aria-hidden="true">&middot;</span>
        <span class="meta-item">{h_text(hub['read_time'])} &middot; 6 Talking-Point Pillars + 6 Issue Briefs</span>
      </div>

      <div class="action-bar">
        <a class="btn btn-primary" href="./{hub['pdf_filename']}">
          {SVG_DOWNLOAD}
          Download Overview PDF ({pdf_pages} pp.)
        </a>
        <a class="btn" href="./{hub['md_filename']}">
          {SVG_MD}
          Markdown Source
        </a>
        <a class="btn" href="./{data.SPOKES[0]['slug']}/">
          {SVG_BOOK}
          Start Brief 01: Power &amp; Water
        </a>
        <a class="btn" href="{data.SITE['repo_url']}">
          {SVG_GH}
          GitHub Repo
        </a>
      </div>
    </div>
  </header>

{build_series_nav_html(None)}

  <nav class="mobile-toc" aria-label="Jump to section">
    <details>
      <summary>Jump to section</summary>
      <ul>
{chr(10).join(mobile_links)}
      </ul>
    </details>
  </nav>

  <div class="layout-shell">
    <aside class="toc-sidebar" aria-label="Table of contents">
      <div class="toc-heading">Contents</div>
      <ul class="toc-list">
{chr(10).join(toc_links)}
      </ul>
      <a class="toc-back-top" href="#top">&uarr; Back to top</a>
    </aside>

    <main class="brief-article">
      <section id="bluf" class="bluf-card">
        <div class="section-head">
          <h2>Bottom line up front</h2>
          <button class="copy-anchor-btn" type="button" data-anchor="#bluf" aria-label="Copy link to Bottom line up front"># Link</button>
        </div>
{bluf_ps}
        <div class="bluf-goal">
          <div class="goal-kicker">Core Federal Principle</div>
          <p data-verbatim>{render_print_inline(hub['bluf_goal'])}</p>
        </div>
      </section>

      <aside class="metrics-strip" aria-label="Key figures cited in this overview">
        <div class="metrics-heading">Key figures cited in this overview</div>
        <div class="metrics-grid">
{metrics_html}
        </div>
      </aside>

{chr(10).join(pillar_sections)}

      <section id="trade-offs" class="brief-section">
        <div class="section-kicker">Implementation Design</div>
        <div class="section-head">
          <h2>Trade-offs to weigh in policy design</h2>
          <button class="copy-anchor-btn" type="button" data-anchor="#trade-offs" aria-label="Copy link to Trade-offs"># Link</button>
        </div>
        <div class="tradeoffs-grid">
{tradeoff_cards}
        </div>
      </section>

      <section id="references" class="brief-section references-card">
        <div class="section-head">
          <h2>Key references for staff follow-up</h2>
          <button class="copy-anchor-btn" type="button" data-anchor="#references" aria-label="Copy link to Key references"># Link</button>
        </div>
        <ul class="references-list">
{refs_html}
        </ul>
      </section>
    </main>
  </div>

  <footer class="site-footer">
    <div class="footer-inner">
      <div>Series 2026-01 by {h_text(data.SITE['author'])} &middot; {h_text(data.SITE['date'])}</div>
      <div class="footer-links">
        <a href="../">All Policy Briefs</a>
        <a href="./{hub['pdf_filename']}">Overview PDF</a>
        <a href="./{hub['md_filename']}">Markdown Source</a>
        <a href="{data.SITE['repo_url']}">GitHub Repository</a>
      </div>
    </div>
  </footer>

  <div id="copy-toast" class="copy-toast" role="status" aria-live="polite">Link copied</div>

{COMMON_READER_JS}
</body>
</html>
"""


def build_spoke_md(sp: dict) -> str:
    gmap = {g["id"]: g for g in sp["glossary"]}
    lines = [
        "**ISSUE BRIEF**",
        f"Series: Practical AI Governance Framework ({sp['code']})",
        f"Prepared by: {data.SITE['author']}",
        f"Date: {data.SITE['date']}",
        f"Subject: {sp['title']}",
        "",
        "### Bottom line up front",
        "",
    ]
    for p in sp["bluf_paragraphs"]:
        lines.extend([render_md_inline(p, gmap), ""])

    for sec in sp["sections"]:
        lines.extend([f"### {sec['heading']}", ""])
        for p in sec["paragraphs"]:
            lines.extend([render_md_inline(p, gmap), ""])

    lines.extend(["### Trade-offs to weigh in policy design", ""])
    for tr in sp["tradeoffs"]:
        lines.extend([f"**{tr['eyebrow']}**", render_md_inline(tr["body"], gmap), ""])

    lines.extend(["---", "Key references for staff follow-up:"])
    for ref in sp["references"]:
        lines.append(f"* {render_md_inline(ref, gmap)}")
    lines.extend(["", "---", "", "### Appendix: Plain-English technical and policy glossary", ""])

    by_cat = {cat: [] for cat, _ in sp["glossary_groups"]}
    for g in sp["glossary"]:
        by_cat[g["cat"]].append(g)

    for cat, heading in sp["glossary_groups"]:
        lines.extend([f"#### {heading}", ""])
        for g in by_cat[cat]:
            lines.extend([f"**{g['dt']}**", render_md_inline(g["dd"], gmap), ""])
    return "\n".join(lines)


def build_spoke_print_html(sp: dict) -> str:
    gmap = {g["id"]: g for g in sp["glossary"]}
    bluf_html = "\n".join(f"      <p>{render_print_inline(p, gmap)}</p>" for p in sp["bluf_paragraphs"])

    sec_html: list[str] = []
    for sec in sp["sections"]:
        sec_html.append(f"    <h3>{h_text(sec['heading'])}</h3>")
        for p in sec["paragraphs"]:
            sec_html.append(f"    <p>{render_print_inline(p, gmap)}</p>")

    tr_html = "\n".join(
        f'    <div class="tradeoff-print-box">\n'
        f'      <div class="tradeoff-print-eyebrow">{h_text(tr["eyebrow"])}</div>\n'
        f"      <p>{render_print_inline(tr['body'], gmap)}</p>\n"
        f"    </div>"
        for tr in sp["tradeoffs"]
    )
    refs_html = "\n".join(f"        <li>{render_print_inline(r, gmap)}</li>" for r in sp["references"])

    by_cat = {cat: [] for cat, _ in sp["glossary_groups"]}
    for g in sp["glossary"]:
        by_cat[g["cat"]].append(g)

    gl_items_html: list[str] = []
    for cat, _ in sp["glossary_groups"]:
        for g in by_cat[cat]:
            gl_items_html.append(
                f'      <div class="glossary-item">\n'
                f"        <dt>{h_text(g['dt'])}</dt>\n"
                f"        <dd>{render_print_inline(g['dd'], gmap)}</dd>\n"
                f"      </div>"
            )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{h_text(sp['code'])} - {h_text(sp['title'])}</title>
  <style>
    @page {{
      size: letter;
      margin: 0.58in 0.7in 0.66in 0.7in;
      @bottom-left {{
        content: "{h_text(sp['code'].upper())}  |  MICHAEL PAULAUSKI  |  {data.SITE['date_upper']}";
        font-family: 'Liberation Sans', sans-serif;
        font-size: 8pt;
        color: #64748b;
        letter-spacing: 0.03em;
      }}
      @bottom-right {{
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Liberation Sans', sans-serif;
        font-size: 8pt;
        color: #64748b;
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 0;
      font-family: 'Noto Serif', 'Liberation Serif', Georgia, serif;
      font-size: 10pt;
      line-height: 1.44;
      color: #111827;
      background: #ffffff;
    }}
    .header-block {{
      border-top: 2.5pt solid #0f172a;
      border-bottom: 0.75pt solid #cbd5e1;
      padding: 9pt 0 8pt 0;
      margin-bottom: 12pt;
    }}
    .doc-label {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 10pt;
      font-weight: 700;
      letter-spacing: 0.11em;
      text-transform: uppercase;
      color: #0f172a;
      margin: 0 0 6pt 0;
    }}
    .meta-table {{
      border-collapse: collapse;
      width: 100%;
      font-family: 'Liberation Sans', sans-serif;
      font-size: 9.2pt;
      line-height: 1.34;
      color: #1e293b;
    }}
    .meta-table td {{ padding: 1.5pt 0; vertical-align: top; }}
    .meta-label {{ width: 88pt; font-weight: 700; color: #334155; }}
    .bluf-box {{
      background: #f8fafc;
      border-left: 3pt solid #1e3a5f;
      padding: 9pt 12pt;
      margin: 0 0 12pt 0;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
    .bluf-box h3 {{ margin: 0 0 5pt 0; color: #1e3a5f; }}
    .bluf-box p:last-child {{ margin-bottom: 0; }}
    h3 {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 10.9pt;
      font-weight: 700;
      color: #0f172a;
      margin: 13pt 0 5pt 0;
      line-height: 1.25;
      break-after: avoid;
      page-break-after: avoid;
    }}
    p {{ margin: 0 0 7.5pt 0; orphans: 3; widows: 3; text-align: left; }}
    .tradeoff-print-box {{
      border-left: 2pt solid #cbd5e1;
      padding-left: 9pt;
      margin: 0 0 8pt 0;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    .tradeoff-print-eyebrow {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 8.6pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #1e3a5f;
      margin-bottom: 2.5pt;
    }}
    .tradeoff-print-box p {{ margin: 0; }}
    .references-block {{
      margin-top: 12pt;
      padding-top: 8pt;
      border-top: 0.75pt solid #cbd5e1;
      font-size: 8.7pt;
      line-height: 1.36;
      color: #334155;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    .references-title {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 8.9pt;
      font-weight: 700;
      color: #0f172a;
      margin: 0 0 4pt 0;
    }}
    .references-block ul {{ margin: 0; padding-left: 14pt; }}
    .references-block li {{ margin-bottom: 2.5pt; }}
    .glossary-appendix {{
      margin-top: 14pt;
      padding-top: 8pt;
      border-top: 2pt solid #0f172a;
    }}
    .glossary-header {{
      margin-bottom: 8pt;
      break-after: avoid;
      page-break-after: avoid;
    }}
    .glossary-header h3 {{ margin: 0 0 2pt 0; color: #0f172a; }}
    .glossary-subtitle {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 8.6pt;
      color: #475569;
      margin: 0;
    }}
    .glossary-list {{
      margin: 0;
      padding: 0;
      column-count: 2;
      column-gap: 18pt;
    }}
    .glossary-item {{
      break-inside: avoid;
      page-break-inside: avoid;
      margin: 0 0 8pt 0;
    }}
    .glossary-item dt {{
      font-family: 'Liberation Sans', sans-serif;
      font-size: 9.1pt;
      font-weight: 700;
      color: #0f172a;
      margin: 0 0 2pt 0;
    }}
    .glossary-item dd {{
      margin: 0;
      font-size: 8.85pt;
      line-height: 1.36;
      color: #1f2937;
    }}
  </style>
</head>
<body>
  <header class="header-block">
    <div class="doc-label">Issue Brief · {h_text(sp['code'])}</div>
    <table class="meta-table">
      <tr><td class="meta-label">Series:</td><td>Practical AI Governance Framework</td></tr>
      <tr><td class="meta-label">Prepared by:</td><td>{h_text(data.SITE['author'])}</td></tr>
      <tr><td class="meta-label">Date:</td><td>{h_text(data.SITE['date'])}</td></tr>
      <tr><td class="meta-label">Subject:</td><td>{h_text(sp['title'])}</td></tr>
    </table>
  </header>

  <section class="bluf-box">
    <h3>Bottom line up front</h3>
{bluf_html}
  </section>

{chr(10).join(sec_html)}

  <section class="tradeoffs-print-section">
    <h3>Trade-offs to weigh in policy design</h3>
{tr_html}
  </section>

  <section class="references-block">
    <div class="references-title">Key references for staff follow-up:</div>
    <ul>
{refs_html}
    </ul>
  </section>

  <section class="glossary-appendix">
    <div class="glossary-header">
      <h3>Appendix: Plain-English technical and policy glossary</h3>
      <p class="glossary-subtitle">{len(sp['glossary'])} plain-language definitions for statutory, technical, and institutional terms used in {h_text(sp['code'])}.</p>
    </div>
    <dl class="glossary-list">
{chr(10).join(gl_items_html)}
    </dl>
  </section>
</body>
</html>
"""


def build_spoke_web_html(sp: dict, idx: int, pdf_pages: int) -> str:
    gmap = {g["id"]: g for g in sp["glossary"]}
    metrics_html = "\n".join(
        f'          <div class="stat-card">\n'
        f'            <div class="stat-figure">{h_text(m["figure"])}</div>\n'
        f'            <div class="stat-label">{h_text(m["label"])}</div>\n'
        f'            <div class="stat-cite">{h_text(m["cite"])}</div>\n'
        f"          </div>"
        for m in sp["metrics"]
    )

    mobile_links = [
        '        <li><a href="#bluf">Bottom line up front</a></li>',
        *[f'        <li><a href="#{sec["id"]}">{sec["toc_num"]}. {h_text(sec["toc_label"])}</a></li>' for sec in sp["sections"]],
        '        <li><a href="#trade-offs">Trade-offs to weigh in policy design</a></li>',
        '        <li><a href="#references">Key references for staff follow-up</a></li>',
        '        <li><a href="#glossary">Appendix: Plain-English glossary</a></li>',
    ]

    toc_links = [
        '        <li><a class="toc-link" href="#bluf"><span class="toc-num">&bull;</span><span>Bottom line up front</span></a></li>',
        *[
            f'        <li><a class="toc-link" href="#{sec["id"]}"><span class="toc-num">{sec["toc_num"]}</span><span>{h_text(sec["toc_label"])}</span></a></li>'
            for sec in sp["sections"]
        ],
        '        <li><a class="toc-link" href="#trade-offs"><span class="toc-num">&bull;</span><span>Policy trade-offs</span></a></li>',
        '        <li><a class="toc-link" href="#references"><span class="toc-num">&bull;</span><span>Key references</span></a></li>',
        '        <li><a class="toc-link" href="#glossary"><span class="toc-num">&bull;</span><span>Plain-English glossary</span></a></li>',
    ]

    bluf_html = "\n".join(
        f'        <p data-verbatim>{render_web_inline(p, gmap)}</p>' for p in sp["bluf_paragraphs"]
    )

    sec_blocks: list[str] = []
    for sec in sp["sections"]:
        ps = "\n".join(f'        <p data-verbatim>{render_web_inline(p, gmap)}</p>' for p in sec["paragraphs"])
        sec_blocks.append(
            f'      <section id="{sec["id"]}" class="brief-section">\n'
            f'        <div class="section-kicker">{h_text(sec["kicker"])}</div>\n'
            f'        <div class="section-head">\n'
            f'          <h2>{h_text(sec["heading"])}</h2>\n'
            f'          <button class="copy-anchor-btn" type="button" data-anchor="#{sec["id"]}" aria-label="Copy link to Section {sec["toc_num"]}"># Link</button>\n'
            f"        </div>\n"
            f"{ps}\n"
            f"      </section>"
        )

    tr_grid_cls = "tradeoffs-grid" if len(sp["tradeoffs"]) > 1 else "tradeoffs-single"
    tradeoff_cards = "\n".join(
        f'          <article class="tradeoff-card">\n'
        f'            <div class="tradeoff-eyebrow">{h_text(tr["eyebrow"])}</div>\n'
        f'            <p data-verbatim>{render_web_inline(tr["body"], gmap)}</p>\n'
        f"          </article>"
        for tr in sp["tradeoffs"]
    )

    refs_html = "\n".join(f"          <li>{render_print_inline(r, gmap)}</li>" for r in sp["references"])

    total_gl = len(sp["glossary"])
    by_cat = {cat: [] for cat, _ in sp["glossary_groups"]}
    for g in sp["glossary"]:
        by_cat[g["cat"]].append(g)

    filter_pills = [f'          <button class="filter-pill active" type="button" data-cat="all">All ({total_gl})</button>']
    for cat, label in sp["glossary_groups"]:
        filter_pills.append(
            f'          <button class="filter-pill" type="button" data-cat="{cat}">{h_text(label)} ({len(by_cat[cat])})</button>'
        )

    gl_groups_html: list[str] = []
    for cat, group_heading in sp["glossary_groups"]:
        cards = "\n".join(
            f'            <dl id="{g["id"]}" class="glossary-card" data-entry data-category="{cat}">\n'
            f"              <dt>{h_text(g['dt'])}</dt>\n"
            f"              <dd>{render_print_inline(g['dd'], gmap)}</dd>\n"
            f"            </dl>"
            for g in by_cat[cat]
        )
        gl_groups_html.append(
            f'        <div class="glossary-group" data-group="{cat}">\n'
            f'          <h3 class="glossary-group-title">{h_text(group_heading)}</h3>\n'
            f'          <div class="glossary-grid">\n{cards}\n          </div>\n'
            f"        </div>"
        )

    prev_card = (
        f'        <a class="pager-card" href="../{data.SPOKES[idx - 1]["slug"]}/">'
        f'<span class="pager-eyebrow">&larr; Previous Brief ({data.SPOKES[idx - 1]["code"]})</span>'
        f'<span class="pager-title">{h_text(data.SPOKES[idx - 1]["title"])}</span></a>'
        if idx > 0
        else '        <a class="pager-card" href="../../">'
        '<span class="pager-eyebrow">&larr; Repository Home</span>'
        '<span class="pager-title">All Policy Briefs &amp; Archive Index</span></a>'
    )
    center_card = (
        '        <a class="pager-card pager-card-center" href="../">'
        '<span class="pager-eyebrow">Series 2026-01</span>'
        '<span class="pager-title">Back to Executive Overview</span></a>'
    )
    next_card = (
        f'        <a class="pager-card pager-card-next" href="../{data.SPOKES[idx + 1]["slug"]}/">'
        f'<span class="pager-eyebrow">Next Brief ({data.SPOKES[idx + 1]["code"]}) &rarr;</span>'
        f'<span class="pager-title">{h_text(data.SPOKES[idx + 1]["title"])}</span></a>'
        if idx < len(data.SPOKES) - 1
        else '        <a class="pager-card pager-card-next" href="../">'
        '<span class="pager-eyebrow">Complete Series &rarr;</span>'
        '<span class="pager-title">Review Full 6-Pillar Executive Overview</span></a>'
    )

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{h_text(sp['title'])} | {h_text(sp['code'])} by {h_text(data.SITE['author'])}</title>
  <meta name="description" content="{h(sp['meta_description'])}" />
  <link rel="canonical" href="{data.SITE['base_url']}/ai-governance/{sp['slug']}/" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{h(sp['title'])} | {h(sp['code'])}" />
  <meta property="og:description" content="{h(sp['og_description'])}" />
  <meta property="og:url" content="{data.SITE['base_url']}/ai-governance/{sp['slug']}/" />
  <meta property="og:image" content="{data.SITE['base_url']}/assets/{sp['og_filename']}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{h(sp['title'])} | {h(sp['code'])}" />
  <meta name="twitter:description" content="{h(sp['og_description'])}" />
  <meta name="twitter:image" content="{data.SITE['base_url']}/assets/{sp['og_filename']}" />

{THEME_BOOT_SCRIPT}

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" /></noscript>
  <link rel="stylesheet" href="../../styles.css" />
</head>
<body>
  <div id="reading-progress" class="reading-progress" aria-hidden="true"></div>

  <header id="top" class="site-header">
    <div class="header-inner">
      <div class="header-top-row">
        <div class="header-crumb-group">
          <a class="back-index-link" href="../">&larr; Executive Overview</a>
          <a class="back-index-link" href="../../">All Briefs</a>
          <span class="doc-badge">{h_text(sp['code'])} &middot; Pillar {sp['num']} of 06</span>
        </div>
        <div class="utility-controls">
          <button id="copy-page-btn" class="btn btn-compact" type="button">Copy Page Link</button>
          <button id="theme-toggle-btn" class="btn btn-compact" type="button" aria-label="Toggle color theme">Dark Mode</button>
        </div>
      </div>

      <h1 class="site-title">{h_text(sp['title'])}</h1>

      <div class="meta-bar">
        <span class="meta-item">Prepared by <strong>{h_text(data.SITE['author'])}</strong></span>
        <span class="meta-sep" aria-hidden="true">&middot;</span>
        <span class="meta-item">{h_text(data.SITE['date'])}</span>
        <span class="meta-sep" aria-hidden="true">&middot;</span>
        <span class="meta-item">{h_text(sp['read_time'])} &middot; {total_gl}-Entry Scoped Glossary</span>
      </div>

      <div class="action-bar">
        <a class="btn btn-primary" href="./{sp['pdf_filename']}">
          {SVG_DOWNLOAD}
          Download PDF ({pdf_pages} pp.)
        </a>
        <a class="btn" href="./{sp['md_filename']}">
          {SVG_MD}
          Markdown Source
        </a>
        <a class="btn" href="../">
          {SVG_BOOK}
          Executive Overview
        </a>
        <a class="btn" href="{data.SITE['repo_url']}">
          {SVG_GH}
          GitHub Repo
        </a>
      </div>
    </div>
  </header>

{build_series_nav_html(sp['slug'])}

  <nav class="mobile-toc" aria-label="Jump to section">
    <details>
      <summary>Jump to section</summary>
      <ul>
{chr(10).join(mobile_links)}
      </ul>
    </details>
  </nav>

  <div class="layout-shell">
    <aside class="toc-sidebar" aria-label="Table of contents">
      <div class="toc-heading">Contents</div>
      <ul class="toc-list">
{chr(10).join(toc_links)}
      </ul>
      <a class="toc-back-top" href="#top">&uarr; Back to top</a>
    </aside>

    <main class="brief-article">
      <section id="bluf" class="bluf-card">
        <div class="section-head">
          <h2>Bottom line up front</h2>
          <button class="copy-anchor-btn" type="button" data-anchor="#bluf" aria-label="Copy link to Bottom line up front"># Link</button>
        </div>
{bluf_html}
      </section>

      <aside class="metrics-strip" aria-label="Key figures cited in this issue brief">
        <div class="metrics-heading">Key figures cited in this issue brief</div>
        <div class="metrics-grid">
{metrics_html}
        </div>
      </aside>

{chr(10).join(sec_blocks)}

      <section id="trade-offs" class="brief-section">
        <div class="section-kicker">Implementation Design</div>
        <div class="section-head">
          <h2>Trade-offs to weigh in policy design</h2>
          <button class="copy-anchor-btn" type="button" data-anchor="#trade-offs" aria-label="Copy link to Trade-offs"># Link</button>
        </div>
        <div class="{tr_grid_cls}">
{tradeoff_cards}
        </div>
      </section>

      <section id="references" class="brief-section references-card">
        <div class="section-head">
          <h2>Key references for staff follow-up</h2>
          <button class="copy-anchor-btn" type="button" data-anchor="#references" aria-label="Copy link to Key references"># Link</button>
        </div>
        <ul class="references-list">
{refs_html}
        </ul>
      </section>

      <section id="glossary" class="brief-section wide-section glossary-section">
        <div class="section-head">
          <h2>Appendix: Plain-English technical and policy glossary</h2>
          <button class="copy-anchor-btn" type="button" data-anchor="#glossary" aria-label="Copy link to Glossary"># Link</button>
        </div>
        <p class="glossary-intro">Scoped plain-English definitions for technical, statutory, and institutional terms used in {h_text(sp['code'])}. Click any dotted term in the text above to preview its definition.</p>

        <div class="glossary-filters" role="group" aria-label="Filter glossary by category">
{chr(10).join(filter_pills)}
        </div>

        <div class="glossary-toolbar">
          <input id="glossary-filter" class="glossary-search" type="search" placeholder="Filter glossary terms..." aria-label="Filter glossary terms" />
          <span id="glossary-count" class="glossary-count">Showing {total_gl} of {total_gl} entries</span>
        </div>

        <div id="glossary-empty" class="glossary-empty">No matching terms found. Clear the search box or switch categories to view all {total_gl} glossary entries.</div>

{chr(10).join(gl_groups_html)}
      </section>

      <nav class="brief-pager" aria-label="Issue brief navigation">
{prev_card}
{center_card}
{next_card}
      </nav>
    </main>
  </div>

  <footer class="site-footer">
    <div class="footer-inner">
      <div>{h_text(sp['code'])} by {h_text(data.SITE['author'])} &middot; {h_text(data.SITE['date'])}</div>
      <div class="footer-links">
        <a href="../">Series Overview</a>
        <a href="../../">All Briefs</a>
        <a href="./{sp['pdf_filename']}">PDF Edition</a>
        <a href="./{sp['md_filename']}">Markdown Source</a>
        <a href="{data.SITE['repo_url']}">GitHub Repository</a>
      </div>
    </div>
  </footer>

  <div id="term-popover" class="term-popover" role="dialog" aria-modal="false" aria-labelledby="term-popover-title" tabindex="-1" hidden>
    <div class="term-popover-head">
      <h4 id="term-popover-title" class="term-popover-title"></h4>
      <button id="term-popover-close" class="term-popover-close" type="button" aria-label="Close definition">&times;</button>
    </div>
    <p id="term-popover-body" class="term-popover-body"></p>
    <a id="term-popover-link" class="term-popover-link" href="#glossary">View in Glossary &darr;</a>
  </div>

  <div id="copy-toast" class="copy-toast" role="status" aria-live="polite">Link copied</div>

{COMMON_READER_JS}
</body>
</html>
"""


def build_root_index_html(hub_pages: int, spoke_pdf_pages: dict[str, int]) -> str:
    hub = data.HUB
    redirect_map = dict(data.LEGACY_HASH_REDIRECTS)
    for k, v in data.LEGACY_TERM_REDIRECTS.items():
        redirect_map[k] = f"./ai-governance/{v}"

    spokes_grid_items = "\n".join(
        f'            <div class="series-spoke-item">\n'
        f'              <div class="series-spoke-main">\n'
        f'                <span class="series-spoke-num">{sp["num"]}</span>\n'
        f'                <a class="series-spoke-link" href="./ai-governance/{sp["slug"]}/">{h_text(sp["nav_label"])}</a>\n'
        f"              </div>\n"
        f'              <a class="series-spoke-pdf" href="./ai-governance/{sp["slug"]}/{sp["pdf_filename"]}">PDF ({spoke_pdf_pages[sp["slug"]]}p)</a>\n'
        f"            </div>"
        for sp in data.SPOKES
    )

    total_glossary = sum(len(sp["glossary"]) for sp in data.SPOKES)

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Policy Briefs &amp; Working Papers | {h_text(data.SITE['author'])}</title>
  <meta name="description" content="Policy briefs and working papers by {h(data.SITE['author'])}, starting with the six-pillar Practical AI Governance Framework series featuring a readable executive overview, six statutory issue briefs, printable PDFs, and plain-English glossaries." />
  <link rel="canonical" href="{data.SITE['base_url']}/" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="Policy Briefs &amp; Working Papers | {h(data.SITE['author'])}" />
  <meta property="og:description" content="Cited federal and civic policy briefs with executive overviews, statutory issue briefs, printable PDFs, Markdown sources, and plain-English glossaries." />
  <meta property="og:url" content="{data.SITE['base_url']}/" />
  <meta property="og:image" content="{data.SITE['base_url']}/assets/og-index.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Policy Briefs &amp; Working Papers | {h(data.SITE['author'])}" />
  <meta name="twitter:description" content="Cited federal and civic policy briefs with executive overviews, statutory issue briefs, printable PDFs, Markdown sources, and plain-English glossaries." />
  <meta name="twitter:image" content="{data.SITE['base_url']}/assets/og-index.png" />

  <script>
    (function () {{
      try {{
        var h = window.location.hash || "";
        var legacyRedirects = {json.dumps(redirect_map)};
        if (legacyRedirects[h]) {{
          window.location.replace(legacyRedirects[h]);
          return;
        }}
        var params = new URLSearchParams(window.location.search);
        var queryTheme = params.get("theme");
        var saved = localStorage.getItem("ai-brief-theme");
        var theme = (queryTheme === "dark" || queryTheme === "light")
          ? queryTheme
          : (saved === "dark" || saved === "light"
            ? saved
            : (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"));
        document.documentElement.setAttribute("data-theme", theme);
      }} catch (e) {{}}
    }})();
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" /></noscript>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header class="archive-header">
    <div class="archive-shell">
      <div class="archive-topbar">
        <div class="archive-brand">
          <span>{h_text(data.SITE['author'])}</span>
          <span class="archive-brand-sub">&middot; Policy Archive</span>
        </div>
        <div class="utility-controls">
          <button id="copy-page-btn" class="btn btn-compact" type="button">Copy Link</button>
          <a class="btn btn-compact" href="{data.SITE['repo_url']}">GitHub</a>
          <button id="theme-toggle-btn" class="btn btn-compact" type="button" aria-label="Toggle color theme">Dark Mode</button>
        </div>
      </div>

      <h1 class="archive-title">Policy briefs and working papers</h1>
      <p class="archive-lede">Cited policy series formatted for rapid staff review and public sharing. Each publication includes a scannable executive overview, standalone statutory issue briefs, printable PDFs, and plain Markdown sources.</p>
    </div>
  </header>

  <main class="archive-main archive-shell">
    <section class="archive-controls" aria-label="Filter publications" hidden>
      <div class="archive-search-row">
        <input id="archive-search" class="glossary-search" type="search" placeholder="Filter briefs by title, topic, or summary..." aria-label="Filter policy briefs" />
        <span id="archive-count" class="archive-count">Showing 1 of 1 series</span>
      </div>
      <div class="archive-filters" role="group" aria-label="Filter briefs by topic">
        <button class="filter-pill active" type="button" data-topic="all">All</button>
        <button class="filter-pill" type="button" data-topic="ai-compute">AI &amp; compute</button>
        <button class="filter-pill" type="button" data-topic="energy-water">Energy &amp; water</button>
        <button class="filter-pill" type="button" data-topic="labor-taxes">Labor &amp; taxes</button>
        <button class="filter-pill" type="button" data-topic="civil-liberties">Civil liberties &amp; courts</button>
        <button class="filter-pill" type="button" data-topic="deepfakes">Deepfakes &amp; creator rights</button>
        <button class="filter-pill" type="button" data-topic="safety-youth">Safety, youth &amp; pace</button>
      </div>
    </section>

    <div id="archive-empty" class="archive-empty">No matching briefs found. Clear the filter or search box to view all publications.</div>

    <section class="archive-year-group" data-year-group aria-label="Publications from 2026">
      <h2 class="archive-year">2026</h2>

      <article class="archive-entry" data-entry data-topics="ai-compute energy-water labor-taxes civil-liberties deepfakes safety-youth">
        <div class="entry-meta">
          <span class="entry-code">{h_text(hub['code'])}</span>
          <span>{h_text(data.SITE['date'])}</span>
          <span class="entry-meta-sep" aria-hidden="true">&middot;</span>
          <span>Executive overview ({hub_pages} pp.) + 6 issue briefs ({total_glossary} glossary entries)</span>
        </div>

        <h3 class="entry-title">
          <a href="./ai-governance/">{h_text(hub['title'])}</a>
        </h3>

        <p class="entry-summary">A hub-and-spoke federal AI governance agenda separating open research speed from accountable commercial and government deployment: 100% cost-causation grid tariffs, water conservation, and gas-turbine air limits; public compute and algorithmic antitrust; statutory civil-liberties and health-care guardrails; worker tax parity and wage insurance; deepfake and creator rights; and frontier bio-cyber safety plus bans on manipulative chatbot design without government-ID dragnets.</p>

        <div class="entry-tags" aria-label="Topics">
          <span class="entry-tag">executive overview</span>
          <span class="entry-tag">energy &amp; water</span>
          <span class="entry-tag">public compute</span>
          <span class="entry-tag">civil liberties</span>
          <span class="entry-tag">labor &amp; taxes</span>
          <span class="entry-tag">deepfakes &amp; creators</span>
          <span class="entry-tag">safety &amp; youth</span>
        </div>

        <div class="action-bar entry-actions">
          <a class="btn btn-primary" href="./ai-governance/">
            {SVG_BOOK}
            Read Executive Overview
          </a>
          <a class="btn" href="./ai-governance/{hub['pdf_filename']}">
            {SVG_DOWNLOAD}
            Overview PDF ({hub_pages} pp.)
          </a>
          <a class="btn" href="./ai-governance/{hub['md_filename']}">
            {SVG_MD}
            Markdown Source
          </a>
        </div>

        <div class="series-spokes-block">
          <div class="series-spokes-heading">Six standalone issue briefs (web reader, PDF &amp; scoped glossary)</div>
          <div class="series-spokes-grid">
{spokes_grid_items}
          </div>
        </div>
      </article>
    </section>
  </main>

  <footer class="site-footer">
    <div class="archive-shell">
      <div class="footer-inner">
        <div>Policy Briefs by {h_text(data.SITE['author'])} &middot; Archive Index</div>
        <div class="footer-links">
          <a href="./ai-governance/">Series 2026-01: AI Governance</a>
          <a href="./ai-governance/{hub['pdf_filename']}">Overview PDF</a>
          <a href="{data.SITE['repo_url']}">GitHub Repository</a>
        </div>
      </div>
    </div>
  </footer>

  <div id="copy-toast" class="copy-toast" role="status" aria-live="polite">Link copied</div>

  <script>
    (function () {{
      var root = document.documentElement;
      var themeBtn = document.getElementById("theme-toggle-btn");
      var copyPageBtn = document.getElementById("copy-page-btn");
      var toast = document.getElementById("copy-toast");
      var toastTimer = null;

      function syncThemeButton() {{
        var current = root.getAttribute("data-theme") || "light";
        themeBtn.textContent = current === "dark" ? "Light Mode" : "Dark Mode";
      }}

      syncThemeButton();

      themeBtn.addEventListener("click", function () {{
        var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        try {{
          localStorage.setItem("ai-brief-theme", next);
        }} catch (e) {{}}
        syncThemeButton();
      }});

      function showToast(msg) {{
        toast.textContent = msg;
        toast.classList.add("visible");
        clearTimeout(toastTimer);
        toastTimer = setTimeout(function () {{
          toast.classList.remove("visible");
        }}, 1800);
      }}

      copyPageBtn.addEventListener("click", function () {{
        var cleanUrl = window.location.origin + window.location.pathname;
        if (window.location.protocol === "file:") {{
          cleanUrl = window.location.href.split("#")[0].split("?")[0];
        }}
        if (navigator.clipboard && navigator.clipboard.writeText) {{
          navigator.clipboard.writeText(cleanUrl).then(function () {{
            showToast("Archive link copied");
          }}).catch(function () {{
            showToast("Link ready in address bar");
          }});
        }} else {{
          showToast("Link ready in address bar");
        }}
      }});

      var controlsEl = document.querySelector(".archive-controls");
      var searchInput = document.getElementById("archive-search");
      var countEl = document.getElementById("archive-count");
      var emptyEl = document.getElementById("archive-empty");
      var topicBtns = Array.prototype.slice.call(document.querySelectorAll("[data-topic]"));
      var yearGroups = Array.prototype.slice.call(document.querySelectorAll("[data-year-group]"));
      var entries = Array.prototype.slice.call(document.querySelectorAll(".archive-entry"));
      var activeTopic = "all";

      if (controlsEl) {{
        controlsEl.hidden = entries.length <= 1;
      }}

      function applyArchiveFilters() {{
        var q = searchInput ? searchInput.value.trim().toLowerCase() : "";
        var visibleCount = 0;

        entries.forEach(function (entry) {{
          var topics = (entry.getAttribute("data-topics") || "").split(/\\s+/);
          var matchesTopic = activeTopic === "all" || topics.indexOf(activeTopic) !== -1;
          var matchesSearch = !q || entry.textContent.toLowerCase().indexOf(q) !== -1;
          var show = matchesTopic && matchesSearch;
          entry.style.display = show ? "" : "none";
          if (show) visibleCount += 1;
        }});

        yearGroups.forEach(function (group) {{
          var hasVisible = Array.prototype.some.call(
            group.querySelectorAll(".archive-entry"),
            function (card) {{ return card.style.display !== "none"; }}
          );
          group.style.display = hasVisible ? "" : "none";
        }});

        if (countEl) {{
          var unit = entries.length === 1 ? "series" : "publications";
          countEl.textContent = "Showing " + visibleCount + " of " + entries.length + " " + unit;
        }}
        if (emptyEl) {{
          emptyEl.style.display = visibleCount === 0 ? "block" : "none";
        }}
      }}

      topicBtns.forEach(function (btn) {{
        btn.addEventListener("click", function () {{
          activeTopic = btn.getAttribute("data-topic") || "all";
          topicBtns.forEach(function (b) {{
            b.classList.toggle("active", b === btn);
          }});
          applyArchiveFilters();
        }});
      }});

      if (searchInput) {{
        searchInput.addEventListener("input", applyArchiveFilters);
      }}
    }})();
  </script>
</body>
</html>
"""


def build_readme_md(hub_pages: int, spoke_pdf_pages: dict[str, int]) -> str:
    hub = data.HUB
    spoke_lines = "\n".join(
        f"{int(sp['num'])}. **[{sp['code']}: {sp['title']}](./ai-governance/{sp['slug']}/{sp['md_filename']})** "
        f"([Web]({data.SITE['base_url']}/ai-governance/{sp['slug']}/) · "
        f"[PDF ({spoke_pdf_pages[sp['slug']]} pp.)](./ai-governance/{sp['slug']}/{sp['pdf_filename']}) · "
        f"{len(sp['glossary'])} glossary entries)"
        for sp in data.SPOKES
    )
    return f"""# Policy Briefs and Working Papers

Archive of policy briefs, statutory issue briefs, and plain-English technical glossaries prepared by {data.SITE['author']}.

* **Archive Index (GitHub Pages):** {data.SITE['base_url']}/
* **Repository:** {data.SITE['repo_url']}

## Published Series

### {hub['code']}: {hub['title']} ({data.SITE['date']})

Six-pillar federal AI governance agenda separating open research speed from accountable commercial and government deployment across power, water, and air rules, public compute and antitrust, civil liberties and health care, worker tax parity and wage insurance, deepfakes and creator rights, and frontier bio-cyber safety plus youth protections without government-ID dragnets.

* **Executive Overview Web Edition:** {data.SITE['base_url']}/ai-governance/
* **Executive Overview PDF ({hub_pages} pages):** [{hub['pdf_filename']}](./ai-governance/{hub['pdf_filename']})
* **Executive Overview Markdown:** [{hub['md_filename']}](./ai-governance/{hub['md_filename']})

Six standalone issue briefs under the overview:

{spoke_lines}

## Repository Structure

* `index.html`: Top-level policy archive landing page keeping future non-AI topics cleanly separated from Series 2026-01.
* `styles.css`: Shared warm Flexoki-inspired light/dark stylesheet across the index, executive overview, and all issue briefs.
* `scripts/series_data.py` and `scripts/build_site.py`: Single-source content definitions and deterministic generator for Markdown sources, print HTML, US Letter PDFs, web readers, and Open Graph cards.
* `scripts/verify_site.py`: Tri-format verbatim parity, `WP:AISIGNS`, PDF page-count, and headless Chromium CDP verification suite.
* `assets/`: `1200x630` Open Graph preview cards (`og-index.png`, `og-ai-governance.png`, `og-spoke-01.png` to `og-spoke-06.png`).
* `ai-governance/`: Flagship executive overview and six standalone `<slug>/` issue-brief subdirectories.

## Rebuild & Verify Locally

```bash
python3 scripts/build_site.py
python3 scripts/verify_site.py
```
"""


def build_og_html(eyebrow: str, title: str, subtitle: str, pills: list[str], footer_url: str, footer_meta: str) -> str:
    pills_html = "\n".join(f'        <span class="pill">{h_text(p)}</span>' for p in pills)
    title_size = "52px" if len(title) > 54 else "58px" if len(title) > 40 else "64px"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <style>
    * {{ box-sizing: border-box; }}
    html, body {{
      margin: 0;
      padding: 0;
      width: 1200px;
      height: 630px;
      overflow: hidden;
      background: #1c1b1a;
      color: #c2c0b6;
      font-family: 'Liberation Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    .card {{
      position: relative;
      width: 1200px;
      height: 630px;
      padding: 50px 70px 44px 70px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background:
        radial-gradient(circle at 92% 14%, rgba(91, 148, 198, 0.14), transparent 45%),
        radial-gradient(circle at 12% 88%, rgba(208, 162, 21, 0.08), transparent 42%),
        linear-gradient(155deg, #1c1b1a 0%, #22201e 58%, #181716 100%);
    }}
    .top-accent {{
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 7px;
      background: linear-gradient(90deg, #4a7eab 0%, #5b94c6 60%, #d0a215 100%);
    }}
    .eyebrow {{
      font-size: 16px;
      font-weight: 700;
      letter-spacing: 0.13em;
      text-transform: uppercase;
      color: #5b94c6;
      margin: 0 0 18px 0;
    }}
    h1 {{
      font-family: 'Noto Serif', 'Liberation Serif', Georgia, serif;
      font-size: {title_size};
      line-height: 1.12;
      font-weight: 700;
      color: #d6d4ca;
      margin: 0 0 20px 0;
      max-width: 1020px;
      letter-spacing: -0.015em;
    }}
    .subtitle {{
      font-size: 24px;
      line-height: 1.42;
      color: #c2c0b6;
      margin: 0;
      max-width: 980px;
    }}
    .bottom {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .pills {{
      display: flex;
      flex-wrap: wrap;
      max-width: 1020px;
      gap: 10px;
    }}
    .pill {{
      display: inline-flex;
      align-items: center;
      padding: 8px 15px;
      border-radius: 999px;
      background: #242321;
      border: 1px solid #3e3c39;
      color: #c2c0b6;
      font-size: 15px;
      font-weight: 600;
      white-space: nowrap;
    }}
    .footer-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 16px;
      border-top: 1px solid #2f2e2c;
      font-size: 17px;
      color: #96948d;
    }}
    .footer-url {{ color: #5b94c6; font-weight: 700; }}
    .footer-meta {{ font-weight: 500; color: #c2c0b6; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="top-accent"></div>
    <div class="main">
      <div class="eyebrow">{h_text(eyebrow)}</div>
      <h1>{h_text(title)}</h1>
      <p class="subtitle">{h_text(subtitle)}</p>
    </div>
    <div class="bottom">
      <div class="pills">
{pills_html}
      </div>
      <div class="footer-row">
        <span class="footer-url">{h_text(footer_url)}</span>
        <span class="footer-meta">{h_text(footer_meta)}</span>
      </div>
    </div>
  </div>
</body>
</html>
"""


def render_pdf(chrome: str, html_path: Path, pdf_path: Path) -> int:
    subprocess.run(
        [
            chrome,
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            f"file://{html_path}",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return count_pdf_pages(pdf_path)


def render_png(chrome: str, html_path: Path, png_path: Path) -> None:
    subprocess.run(
        [
            chrome,
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1200,630",
            f"--screenshot={png_path}",
            f"file://{html_path}",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main() -> int:
    chrome = chrome_executable()
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    AI_DIR.mkdir(parents=True, exist_ok=True)

    # Pass 1: Write canonical .md, print brief.html, and render all 7 PDFs
    hub_md_path = AI_DIR / data.HUB["md_filename"]
    hub_brief_html_path = AI_DIR / "brief.html"
    hub_pdf_path = AI_DIR / data.HUB["pdf_filename"]

    hub_md_path.write_text(build_hub_md(), encoding="utf-8")
    hub_brief_html_path.write_text(build_hub_print_html(), encoding="utf-8")
    hub_pages = render_pdf(chrome, hub_brief_html_path, hub_pdf_path)
    print(f"[pdf] Hub {hub_pdf_path.name}: {hub_pages} pages ({hub_pdf_path.stat().st_size} bytes)")

    spoke_pdf_pages: dict[str, int] = {}
    for sp in data.SPOKES:
        sdir = AI_DIR / sp["slug"]
        sdir.mkdir(parents=True, exist_ok=True)
        (sdir / sp["md_filename"]).write_text(build_spoke_md(sp), encoding="utf-8")
        br_path = sdir / "brief.html"
        pdf_path = sdir / sp["pdf_filename"]
        br_path.write_text(build_spoke_print_html(sp), encoding="utf-8")
        pages = render_pdf(chrome, br_path, pdf_path)
        spoke_pdf_pages[sp["slug"]] = pages
        print(f"[pdf] Spoke {sp['num']} ({sp['slug']}): {pages} pages ({pdf_path.stat().st_size} bytes)")

    # Pass 2: Write web readers, root index, README, and 8 OG preview PNGs with exact PDF page counts
    (AI_DIR / "index.html").write_text(build_hub_web_html(hub_pages, spoke_pdf_pages), encoding="utf-8")
    for idx, sp in enumerate(data.SPOKES):
        (AI_DIR / sp["slug"] / "index.html").write_text(
            build_spoke_web_html(sp, idx, spoke_pdf_pages[sp["slug"]]), encoding="utf-8"
        )

    (REPO / "index.html").write_text(build_root_index_html(hub_pages, spoke_pdf_pages), encoding="utf-8")
    (REPO / "README.md").write_text(build_readme_md(hub_pages, spoke_pdf_pages), encoding="utf-8")

    with tempfile.TemporaryDirectory() as tmp:
        tdir = Path(tmp)
        og_jobs = [
            (
                ASSETS_DIR / "og-index.png",
                build_og_html(
                    "Michael Paulauski · Policy Archive",
                    "Policy Briefs and Working Papers",
                    "Cited policy series formatted for staff review and public sharing: executive overview, six statutory issue briefs, printable PDFs, and glossaries.",
                    ["Series 2026-01 AI Governance", "01 Power & Water", "02 Compute & Antitrust", "03 Civil Liberties", "04 Workers & Taxes", "05 Deepfakes", "06 Safety & Youth"],
                    "mike10010100.github.io/policy-briefs",
                    "Executive Overview · 6 Issue Briefs · PDFs",
                ),
            ),
            (
                ASSETS_DIR / data.HUB["og_filename"],
                build_og_html(
                    "Series 2026-01 · Michael Paulauski · November 2026",
                    "Practical AI Governance Framework",
                    "Six-pillar federal agenda separating open research speed from accountable commercial and government deployment, with standalone statutory issue briefs.",
                    [f"{sp['num']}. {sp['nav_label']}" for sp in data.SPOKES],
                    "mike10010100.github.io/policy-briefs/ai-governance",
                    f"Executive Overview ({hub_pages} pp.) + 6 Issue Briefs",
                ),
            ),
        ]
        for sp in data.SPOKES:
            og_jobs.append(
                (
                    ASSETS_DIR / sp["og_filename"],
                    build_og_html(
                        sp["og_eyebrow"],
                        sp["title"],
                        sp["og_description"],
                        sp["og_pills"],
                        f"mike10010100.github.io/policy-briefs/ai-governance/{sp['slug']}",
                        f"Web Brief · {spoke_pdf_pages[sp['slug']]}-Page PDF · {len(sp['glossary'])}-Term Glossary",
                    ),
                )
            )
        for i, (out_png, html_str) in enumerate(og_jobs):
            hfile = tdir / f"og_{i}.html"
            hfile.write_text(html_str, encoding="utf-8")
            render_png(chrome, hfile, out_png)
            print(f"[og]  {out_png.name} ({out_png.stat().st_size} bytes)")

    print("[DONE] Built 1 Hub + 6 Spokes + Root Index + README + 8 OG images.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
