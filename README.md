# Practical AI Governance Framework

Policy brief and plain-English technical glossary prepared by Michael Paulauski (November 13, 2026).

* **Web Edition (GitHub Pages):** https://mike10010100.github.io/ai-policy-brief/
* **Print-Ready PDF (6 pages):** [Practical-AI-Governance-Policy-Brief.pdf](./Practical-AI-Governance-Policy-Brief.pdf)
* **Plain Markdown Source:** [Practical-AI-Governance-Policy-Brief.md](./Practical-AI-Governance-Policy-Brief.md)

## Overview

The brief outlines federal policy proposals across five areas:

1. Requiring hyperscale data centers to pay 100% of grid upgrades, bring matched clean power and peak-hour load flexibility, end municipal drinking-water subsidies, and close Clean Air Act loopholes for unpermitted methane turbines.
2. Expanding publicly owned compute under the NSF NAIRR Operations Center and CREATE AI Act, keeping open-weight models legal, policing cloud-compute tying and acqui-hires, and outlawing nonpublic algorithmic price-fixing.
3. Setting statutory civil-liberties limits on lethal autonomous targeting, nuclear launch authority, and commercial data-broker surveillance, barring black-box algorithms in sentencing, public benefits, and medical-necessity denials, and funding audited AI tools for civil legal aid and public defenders.
4. Reducing the tax gap between human wages and corporate equipment write-offs with a trust-fund-neutral payroll credit, outlawing abusive workplace monitoring ("bossware"), and pairing modernized WARN Act notice with federal wage insurance and sectoral training.
5. Closing civil deepfake litigation gaps alongside federal voice-and-likeness consent rights, voice-clone fraud penalties, and platform provenance metadata rules.

## Repository Contents

* `index.html` and `styles.css`: Responsive web edition hosted via GitHub Pages, with Open Graph metadata (`assets/og-card.png`), direct section deep-links for social sharing, Light/Dark mode, and a filterable glossary.
* `Practical-AI-Governance-Policy-Brief.md`: Plain-text Markdown version of the complete brief and glossary.
* `Practical-AI-Governance-Policy-Brief.pdf`: 6-page US Letter PDF export.
* `brief.html`: Print-styled HTML source used to build `Practical-AI-Governance-Policy-Brief.pdf`.

## Rebuilding the PDF

Render `Practical-AI-Governance-Policy-Brief.pdf` directly from `brief.html` using Chromium headless print:

```bash
google-chrome --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=Practical-AI-Governance-Policy-Brief.pdf \
  "file://$(pwd)/brief.html"
```
