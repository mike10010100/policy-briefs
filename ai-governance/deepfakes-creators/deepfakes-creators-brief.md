**ISSUE BRIEF**
Series: Practical AI Governance Framework (Brief 2026-01E)
Prepared by: Michael Paulauski
Date: November 15, 2026
Subject: Intimate-deepfake remedies, voice-clone fraud, and creator rights

### Bottom line up front

The May 2025 TAKE IT DOWN Act (Pub. L. 119-12) established federal criminal penalties and 48-hour platform removals for authentic and synthetic nonconsensual intimate imagery, yet victims still lack federal civil damages against intimate-deepfake perpetrators, individuals lack a federal consent remedy against unauthorized voice and visual clones, senior citizens face surging AI voice-clone wire scams, and working creators face pirated shadow-library scraping and coercive buyouts.

Congress should finish passing civil deepfake and voice-likeness consent rights with strong speech safe harbors, require privacy-respecting provenance labels on hosted commercial generators, enforce anti-piracy and anti-laundering training rules, and support voluntary collective compensation for creators.

### 1. Pass DEFIANCE civil suits and NO FAKES consent rights with speech safe harbors

Building on the criminal penalties and 48-hour platform takedowns enacted in the 2025 TAKE IT DOWN Act (which Congress should amend with steep bad-faith false-notice penalties and facial-scope guardrails so 48-hour clocks cannot censor non-intimate speech without forcing victims to sue to block automatic re-uploads), Congress should enact the DEFIANCE Act (S. 1837) amending 15 U.S.C. Section 6851 so victims of intimate digital forgeries can sue perpetrators and knowing or reckless distributors directly (paired with a narrow Section 230 carve-out for sites knowingly profiting from nonconsensual intimate abuse).

Alongside DEFIANCE, Congress should pass a revised NO FAKES Act protecting parody, satire, news, historical, and documentary speech as threshold exclusions, removing S. 4591's mandatory staydown fingerprinting, non-judicial unmasking subpoenas, and Section 230 IP carve-out, and banning lifetime assignments plus terms-of-service or non-union click-wrap likeness licenses so working creators and private citizens keep an enforceable consent right over AI clones.

### 2. Stop voice-clone fraud and mandate privacy-clean hosted provenance

Federal law should enforce the FTC Impersonation Rule (16 C.F.R. Part 461, while finalizing its individual-impersonation extension) and the FCC's TCPA AI-voice ruling (FCC 24-17, while finalizing FCC 24-84 disclosures), fund cross-border wire-fraud recovery, stiffen elder wire-fraud penalties, and adopt FCC 25-25 non-IP caller-authentication and foreign-gateway traceback rules so carriers can trace and block spoofed family-emergency and bank-impersonation calls.

Congress should also require hosted commercial media generators (explicitly excluding open-weight model downloads and plain text) to embed open C2PA synthetic-origin metadata (using short-lived, RFC 3161-timestamped service signing keys with zero end-user or user-correlatable asset IDs, avoiding California SB 942 and SB 1000's unique-ID and small-tool mandates) or non-tracking soft-binding watermarks, require large platforms to preserve intact manifests or soft bindings across transcoding, bar government mandates that penalize or force demotion of unsigned citizen or open-source media (or false AI labeling solely for lacking provenance), and punish intentional stripping to defraud, impersonate, or conceal unlawful intimate abuse.

### 3. Ban shadow-library piracy, guard fair use, and back voluntary licensing

For creative works, Congress should require commercial developers to publish high-level training-data summaries, enforce clear statutory penalties against pirated shadow libraries and the commercial laundering of corpora obtained via academic paywall or DMCA Section 1201 research-exemption breaches (sparing open public-web URL indexes), and preserve lawful non-substitutive fair use where public-interest, academic, or commercial training relies on legitimately acquired material (excepting market-diluting commercial substitution).

To ensure revenue actually reaches writers, journalists, illustrators, musicians, and voice actors instead of sitting solely with major catalogs, federal policy should authorize voluntary collective licensing backed by a narrow antitrust safe harbor and non-waivable direct creator payout splits.

### Trade-offs to weigh in policy design

**05 · Likeness Rights & Creator Pay vs. Free Expression**
Overbroad publicity bills or poorly drafted provenance rules can chill political satire, news reporting, and open-source media tools. Scoping provenance obligations strictly to hosted commercial generators (never open-weight files or text), banning end-user identity assertions inside C2PA containers, barring state penalties on unsigned citizen or open-source media, protecting parody/news/fair-use exceptions, and targeting statutory penalties at pirated shadow libraries protects victims and creators cleanly.

---
Key references for staff follow-up:
* U.S. Copyright Office, *Copyright and Artificial Intelligence, Part 3: Generative AI Training* (May 2025); *Bartz v. Anthropic* (including July 2026 $1.5B shadow-library settlement) and *Kadrey v. Meta* market-dilution orders (2025-2026)
* TAKE IT DOWN Act (Pub. L. 119-12, enacted May 2025; FTC enforcement eff. May 2026); DEFIANCE Act (S. 1837); bipartisan NO FAKES Act (S. 4591)
* Coalition for Content Provenance and Authenticity (C2PA) open spec & RFC 3161; Cal. SB 942 / SB 1000; FTC Impersonation Rule (16 C.F.R. Part 461), FCC 24-17 AI-voice ruling, and FCC 24-84 / FCC 25-25 proceedings

---

### Appendix: Plain-English technical and policy glossary

#### Deepfakes, scams, and provenance

**TAKE IT DOWN, DEFIANCE, and NO FAKES Acts**
The May 2025 TAKE IT DOWN Act (Pub. L. 119-12) created federal criminal penalties and mandatory 48-hour takedowns for nonconsensual intimate images, including AI deepfakes. The DEFIANCE Act (S. 1837) amends 15 U.S.C. Section 6851 with federal civil damages against intimate-deepfake perpetrators and knowing or reckless distributors, while a revised NO FAKES Act establishes a consent right over unauthorized voice or visual replicas paired with threshold speech exclusions and host safe harbors.

**Provenance (synthetic-origin) metadata and signal watermarks**
A cryptographic C2PA manifest (using short-lived, RFC 3161-timestamped service signing keys) or an imperceptible signal watermark embedded in synthetic media by hosted commercial tools. Unlike California SB 942's unique-identifier mandate and SB 1000's small-tool sweep, federal rules should forbid end-user and user-correlatable asset IDs while preserving intact labels or soft bindings across platform transcoding.

**Telecom caller authentication (STIR/SHAKEN) and voice-clone fraud**
STIR/SHAKEN is the cryptographic caller-ID verification framework across IP phone networks (with FCC 25-25 proposing non-IP expansion) that verifies calling numbers instead of detecting cloned AI voices on legitimate VoIP lines, making FCC AI-voice consent rules and wire-fraud enforcement essential.

#### Training data and creator rights

**Shadow libraries, dataset laundering, and collective licensing**
Shadow libraries are illicit bulk repositories of pirated books, papers, and media; dataset laundering occurs when a commercial firm exploits corpora obtained through academic paywall or DMCA Section 1201 research-exemption breaches (distinct from open public-web URL indexes). Collective licensing enables voluntary royalty pools with statutory antitrust protection and direct creator payout splits.
