**ISSUE BRIEF**
Series: Practical AI Governance Framework (Brief 2026-01E)
Prepared by: Michael Paulauski
Date: November 15, 2026
Subject: Intimate-deepfake remedies, voice-clone fraud, and creator rights

### Bottom line up front

The May 2025 TAKE IT DOWN Act (Pub. L. 119-12) established federal criminal penalties and 48-hour platform removals for authentic and synthetic nonconsensual intimate imagery, yet victims still lack federal civil damages against intimate-deepfake perpetrators, individuals lack a federal consent remedy against unauthorized voice and visual clones, senior citizens face surging AI voice-clone wire scams, and working creators face pirated shadow-library scraping and coercive buyouts.

Congress should finish passing civil deepfake and voice-likeness consent rights with strong speech safe harbors, require privacy-respecting provenance labels on hosted commercial generators, enforce anti-piracy and anti-laundering training rules, and support voluntary collective compensation for creators.

### 1. Pass DEFIANCE civil suits and NO FAKES consent rights with speech safe harbors

Building on the criminal penalties and 48-hour platform takedowns enacted in the 2025 TAKE IT DOWN Act (paired with counter-notice restoration and bad-faith takedown penalties so 48-hour clocks cannot be abused to censor lawful speech), Congress should enact the DEFIANCE Act (S. 1837) so victims of intimate digital forgeries can sue perpetrators and knowing distributors directly in federal court under 15 U.S.C. Section 6851 instead of waiting solely on scarce prosecutorial resources.

Alongside DEFIANCE, Congress should pass a bipartisan NO FAKES Act paired with explicit parody, satire, news, historical, documentary, and DMCA-style host notice-and-takedown safe harbors, plus a statutory ban on lifetime likeness assignments and coercive terms-of-service or non-union click-wrap sign-aways so working creators and private citizens keep an enforceable consent right over AI clones of their voice and likeness.

### 2. Stop voice-clone fraud and mandate privacy-clean hosted provenance

Federal law should enforce the FTC Impersonation Rule (16 C.F.R. Part 461, while finalizing its individual-impersonation extension) alongside FCC TCPA AI-voice consent rules (FCC 24-17 and FCC 24-84), stiffen wire-fraud penalties for elder voice-clone scams, and close non-IP gaps in telecom caller-authentication rules so carriers can trace and block spoofed family-emergency and bank-impersonation calls.

Congress should also require hosted commercial media generators (explicitly excluding open-weight model downloads and plain text) to embed open synthetic-origin metadata or signal watermarks using ephemeral service-level signing keys with zero end-user identity fields, require large platforms to retain or re-attest provenance labels across transcoding, forbid algorithmic demotion or penalties against unsigned citizen or open-source media, and outlaw intentional stripping solely to defraud or impersonate.

### 3. Penalize shadow-library laundering and back voluntary creator licensing

For creative works, Congress should require commercial developers to publish high-level training-data summaries, enforce clear statutory penalties against pirated shadow libraries and the commercial laundering of noncommercial research datasets (closing the loophole where for-profit labs commercialize scrape indexes assembled under academic exemptions), and preserve lawful non-substitutive fair use where public-interest, academic, or commercial training relies on legitimately acquired material.

To ensure revenue actually reaches writers, journalists, illustrators, musicians, and voice actors instead of sitting solely with major catalogs, federal policy should authorize and support voluntary collective licensing mechanisms that pay individual working creators.

### Trade-offs to weigh in policy design

**05 · Likeness Rights & Creator Pay vs. Free Expression**
Overbroad publicity bills or poorly drafted provenance rules can chill political satire, news reporting, and open-source media tools. Scoping provenance obligations strictly to hosted commercial generators (never open-weight files or text), banning end-user identity assertions inside C2PA containers, barring penalties on unsigned citizen or open-source media, protecting parody/news/fair-use exceptions, and targeting statutory penalties at pirated shadow libraries protects victims and creators cleanly.

---
Key references for staff follow-up:
* U.S. Copyright Office, *Copyright and Artificial Intelligence, Part 3: Generative AI Training* (May 2025); *Bartz v. Anthropic* (including July 2026 $1.5B shadow-library settlement) and *Kadrey v. Meta* (2025-2026)
* TAKE IT DOWN Act (Pub. L. 119-12, enacted May 2025; FTC enforcement eff. May 2026); DEFIANCE Act (S. 1837); bipartisan NO FAKES Act (S. 4591)
* Coalition for Content Provenance and Authenticity (C2PA) open specification; FTC Impersonation Rule (16 C.F.R. Part 461) and FCC AI-Voice TCPA Rulings (FCC 24-17, FCC 24-84) (2024-2026)

---

### Appendix: Plain-English technical and policy glossary

#### Deepfakes, scams, and provenance

**TAKE IT DOWN, DEFIANCE, and NO FAKES Acts**
The May 2025 TAKE IT DOWN Act (Pub. L. 119-12) created federal criminal penalties and mandatory 48-hour takedowns for nonconsensual intimate images, including AI deepfakes. The DEFIANCE Act (S. 1837) adds federal civil damages against intimate-deepfake perpetrators and knowing distributors under 15 U.S.C. Section 6851, while the NO FAKES Act establishes a federal consent right over unauthorized voice or visual replicas paired with First Amendment and host notice-and-takedown safe harbors.

**Provenance (synthetic-origin) metadata and signal watermarks**
A cryptographic record (such as the open C2PA standard) or imperceptible signal watermark embedded in synthetic audio, video, or images by hosted commercial tools. While optional C2PA specifications allow identity assertions, federal statute (modeled on California SB 942) should mandate service-only signing keys with zero end-user identity fields, paired with signal watermarks or platform label retention across transcoding.

**Telecom caller authentication (STIR/SHAKEN) and voice-clone fraud**
STIR/SHAKEN is the cryptographic caller-ID verification framework used across IP phone networks to stop spoofed phone numbers that scammers pair with short-sample AI voice clones to impersonate family members or bank officials.

#### Training data and creator rights

**Shadow libraries, dataset laundering, and collective licensing**
Shadow libraries are illicit bulk repositories of pirated books, papers, and media; dataset laundering occurs when a commercial firm exploits datasets compiled by academics under noncommercial research claims to train proprietary products. Collective licensing enables rightsholders and working creators to opt works into transparent, shared royalty pools without blocking lawful fair use.
