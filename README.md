# Policy Briefs and Working Papers

Archive of policy briefs, working papers, and plain-English technical glossaries prepared by Michael Paulauski.

* **Archive Index (GitHub Pages):** https://mike10010100.github.io/policy-briefs/
* **Repository:** https://github.com/mike10010100/policy-briefs

## Published Briefs

### Brief 2026-01: Practical AI Governance Framework (November 13, 2026)

* **Web Edition:** https://mike10010100.github.io/policy-briefs/ai-governance/
* **Print-Ready PDF (6 pages):** [Practical-AI-Governance-Policy-Brief.pdf](./ai-governance/Practical-AI-Governance-Policy-Brief.pdf)
* **Plain Markdown Source:** [Practical-AI-Governance-Policy-Brief.md](./ai-governance/Practical-AI-Governance-Policy-Brief.md)

Covers five federal policy pillars:

1. Requiring hyperscale data centers to pay 100% of grid upgrades with minimum-term collateral, bring new deliverable clean power on a rising hourly-matched schedule with peak-hour load flexibility, end municipal drinking-water discounts in favor of closed-loop, hybrid adiabatic, or reclaimed municipal wastewater cooling, and close Clean Air Act and Federal Power Act loopholes for methane turbines and fossil emergency orders.
2. Expanding publicly owned compute and independent cloud vouchers under the NSF-DOE NAIRR Operations Center and CREATE AI Act, keeping open-weight models legal, policing cloud-compute tying and dominant-platform acqui-hires, and outlawing shared algorithmic price-fixing.
3. Setting statutory civil-liberties limits on offensive target selection and lethal force, nuclear launch authority, warrantless AI camera/facial-recognition dragnets, and commercial data-broker purchases, barring automated denials in sentencing, public benefits, and health care without individualized specialty-physician review or state remedies, and funding human staffing alongside privilege-protected legal-aid and defender tools.
4. Scaling back corporate 100% bonus depreciation toward economic depreciation while preserving Section 174A R&D and software expensing, pairing revenues with a trust-fund-neutral payroll credit, outlawing abusive workplace monitoring ("bossware") and forced arbitration waivers, and pairing modernized WARN Act notice for remote and rolling mass layoffs with federal wage insurance and sectoral training.
5. Closing civil deepfake litigation gaps alongside federal voice-and-likeness consent rights with parody, news, host, and non-negotiated contract guardrails, voice-clone fraud penalties, hosted synthetic-origin provenance rules, commercial training-data summaries, shadow-library and research-laundering bans, and voluntary collective licensing that pays individual creators.

## Repository Structure

* `index.html`: Top-level chronological policy archive index with topic filtering, search, direct download links, and section deep-links.
* `styles.css`: Shared light/dark stylesheet (warm archival paper in Light Mode and low-glare Flexoki-inspired ink-and-stone Dark Mode) shared by the index and individual briefs.
* `assets/`: Open Graph social preview images (`og-index.png`, `og-ai-governance.png`).
* `<slug>/`: Each published policy brief lives in its own subdirectory (starting with `ai-governance/`) containing:
  * `index.html`: Web reader edition with section deep-links, interactive inline glossary popovers, and Light/Dark toggle.
  * `*.md`: Plain Markdown source.
  * `brief.html` and `*.pdf`: Print-ready US Letter layout and exported PDF.

## Adding a Future Brief

1. Create a new folder `<slug>/` at the repo root containing `index.html` (linking `../styles.css`), its `.md` source, and optional `brief.html` / `.pdf`.
2. Add an `.archive-entry` card block under the matching year heading in root `index.html`.
3. Render `ai-governance/Practical-AI-Governance-Policy-Brief.pdf` (or future brief PDFs) from `brief.html` using Chromium headless print:

```bash
google-chrome --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=ai-governance/Practical-AI-Governance-Policy-Brief.pdf \
  "file://$(pwd)/ai-governance/brief.html"
```
