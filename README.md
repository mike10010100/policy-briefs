# Policy Briefs and Working Papers

Archive of policy briefs, statutory issue briefs, and plain-English technical glossaries prepared by Michael Paulauski.

* **Archive Index (GitHub Pages):** https://mike10010100.github.io/policy-briefs/
* **Repository:** https://github.com/mike10010100/policy-briefs

## Published Series

### Series 2026-01: Practical AI governance framework (November 15, 2026)

Six-pillar federal AI governance agenda separating open research speed from accountable commercial and government deployment across power, water, and air rules, public compute and antitrust, civil liberties and health care, worker tax parity and wage insurance, deepfakes and creator rights, and frontier bio-cyber safety plus youth protections without government-ID dragnets.

* **Executive Overview Web Edition:** https://mike10010100.github.io/policy-briefs/ai-governance/
* **Executive Overview PDF (3 pages):** [Practical-AI-Governance-Policy-Brief.pdf](./ai-governance/Practical-AI-Governance-Policy-Brief.pdf)
* **Executive Overview Markdown:** [Practical-AI-Governance-Policy-Brief.md](./ai-governance/Practical-AI-Governance-Policy-Brief.md)

Six standalone issue briefs under the overview:

1. **[Brief 2026-01A: Clean power, water, and air rules for hyperscale data centers](./ai-governance/power-water/power-water-brief.md)** ([Web](https://mike10010100.github.io/policy-briefs/ai-governance/power-water/) · [PDF (3 pp.)](./ai-governance/power-water/power-water-brief.pdf) · 8 glossary entries)
2. **[Brief 2026-01B: Public compute, open-weight models, and algorithmic antitrust](./ai-governance/compute-antitrust/compute-antitrust-brief.md)** ([Web](https://mike10010100.github.io/policy-briefs/ai-governance/compute-antitrust/) · [PDF (2 pp.)](./ai-governance/compute-antitrust/compute-antitrust-brief.pdf) · 5 glossary entries)
3. **[Brief 2026-01C: Statutory civil-liberties, courtroom, and patient-care guardrails](./ai-governance/civil-liberties/civil-liberties-brief.md)** ([Web](https://mike10010100.github.io/policy-briefs/ai-governance/civil-liberties/) · [PDF (2 pp.)](./ai-governance/civil-liberties/civil-liberties-brief.pdf) · 5 glossary entries)
4. **[Brief 2026-01D: Worker tax parity, workplace AI rules, and displacement insurance](./ai-governance/workers-taxes/workers-taxes-brief.md)** ([Web](https://mike10010100.github.io/policy-briefs/ai-governance/workers-taxes/) · [PDF (2 pp.)](./ai-governance/workers-taxes/workers-taxes-brief.pdf) · 3 glossary entries)
5. **[Brief 2026-01E: Intimate-deepfake remedies, voice-clone fraud, and creator rights](./ai-governance/deepfakes-creators/deepfakes-creators-brief.md)** ([Web](https://mike10010100.github.io/policy-briefs/ai-governance/deepfakes-creators/) · [PDF (2 pp.)](./ai-governance/deepfakes-creators/deepfakes-creators-brief.pdf) · 4 glossary entries)
6. **[Brief 2026-01F: Frontier safety, development pace, and youth protections without ID dragnets](./ai-governance/safety-youth-pace/safety-youth-pace-brief.md)** ([Web](https://mike10010100.github.io/policy-briefs/ai-governance/safety-youth-pace/) · [PDF (3 pp.)](./ai-governance/safety-youth-pace/safety-youth-pace-brief.pdf) · 5 glossary entries)

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
