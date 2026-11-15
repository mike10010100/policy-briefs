"""Single-source structured content for the Policy Briefs Hub-and-Spoke Series."""

SITE = {
    "author": "Michael Paulauski",
    "date": "November 15, 2026",
    "date_upper": "NOVEMBER 15, 2026",
    "base_url": "https://mike10010100.github.io/policy-briefs",
    "repo_url": "https://github.com/mike10010100/policy-briefs",
}

LEGACY_HASH_REDIRECTS = {
    "#bluf": "./ai-governance/#bluf",
    "#data-centers": "./ai-governance/#data-centers",
    "#compute-antitrust": "./ai-governance/#compute-antitrust",
    "#civil-liberties-justice": "./ai-governance/#civil-liberties-justice",
    "#workers-taxes": "./ai-governance/#workers-taxes",
    "#deepfakes-fraud": "./ai-governance/#deepfakes-fraud",
    "#safety-youth-pace": "./ai-governance/#safety-youth-pace",
    "#trade-offs": "./ai-governance/#trade-offs",
    "#references": "./ai-governance/#references",
    "#glossary": "./ai-governance/power-water/#glossary",
}

LEGACY_TERM_REDIRECTS = {
    "#term-1": "compute-antitrust/#term-1",
    "#term-2": "compute-antitrust/#term-2",
    "#term-3": "compute-antitrust/#term-3",
    "#term-4": "compute-antitrust/#term-4",
    "#term-5": "deepfakes-creators/#term-2",
    "#term-6": "power-water/#term-1",
    "#term-7": "power-water/#term-2",
    "#term-8": "power-water/#term-3",
    "#term-9": "power-water/#term-4",
    "#term-10": "power-water/#term-5",
    "#term-11": "power-water/#term-6",
    "#term-12": "power-water/#term-7",
    "#term-13": "workers-taxes/#term-1",
    "#term-14": "workers-taxes/#term-2",
    "#term-15": "workers-taxes/#term-3",
    "#term-16": "civil-liberties/#term-1",
    "#term-17": "civil-liberties/#term-2",
    "#term-18": "civil-liberties/#term-5",
}

SPOKES = [
    {
        "num": "01",
        "code": "Brief 2026-01A",
        "slug": "power-water",
        "hub_section_id": "data-centers",
        "nav_label": "Power & Water",
        "short_toc": "Power, water & air",
        "title": "Clean power, water, and air rules for hyperscale data centers",
        "hub_kicker": "Pillar 01 · Clean Power, Water & Air",
        "hub_heading": "1. Make hyperscale data centers fund clean power and water up front",
        "read_time": "5 min read",
        "md_filename": "power-water-brief.md",
        "pdf_filename": "power-water-brief.pdf",
        "og_filename": "og-spoke-01.png",
        "og_eyebrow": "Brief 2026-01A · Michael Paulauski · November 2026",
        "og_pills": [
            "100% Cost-Causation Tariffs",
            "0.25%-1% Peak Curtailment",
            "Closed-Loop & Reclaimed Water",
            "Clean Air Loophole Closures",
        ],
        "meta_description": (
            "Federal and state utility rules making hyperscale data centers fund 100% of grid upgrades, "
            "deliver hourly-matched clean power and peak curtailment, end drinking-water subsidies, "
            "and close gas-turbine air permitting loopholes."
        ),
        "og_description": (
            "100% cost-causation grid tariffs, 76-126 GW peak flexibility, closed-loop or reclaimed-water cooling, "
            "and closing Subpart KKKKa and nonroad methane-turbine loopholes."
        ),
        "metrics": [
            {
                "figure": "$9B+",
                "label": "Data-center capacity cost added to the 2025/2026 PJM wholesale auction.",
                "cite": "PJM Independent Market Monitor (Monitoring Analytics)",
            },
            {
                "figure": "76-126 GW",
                "label": "U.S. grid headroom unlocked by 0.25%-1% peak load curtailment.",
                "cite": "Norris et al., Duke Nicholas Institute (Feb. 2025)",
            },
            {
                "figure": "$40B-$150B",
                "label": "Ten-year U.S. capital, operating, and fuel savings from load flexibility (up to 50% flexible hours).",
                "cite": "Ross & Ewing, Duke Nicholas Institute (Feb. 2026)",
            },
            {
                "figure": "1M-5M gal/day",
                "label": "Daily treated-water draw by a single hyperscale facility in dry basins.",
                "cite": "Water Foundation; Brookings Institution",
            },
        ],
        "bluf_paragraphs": [
            (
                "Across the [[term-1|PJM grid]] spanning 13 states and Washington, D.C., PJM's Independent Market Monitor "
                "calculates that surging data-center demand forecasts added $9.33 billion to the 2025/2026 wholesale capacity "
                "auction, while U.S. Department of Energy resource-adequacy filings warn that rapid large-load growth is "
                "colliding with plant retirements and driving up household electric bills. Meanwhile, single dry-basin "
                "campuses pull millions of gallons of municipal water daily or run trailer-mounted gas turbines outside "
                "major-source air permits."
            ),
            (
                "Federal and state policy should enforce strict cost causation: require large facilities to fund "
                "grid upgrades up front, unlock clean [[term-3|interconnection queues|Interconnection queues|The multi-year engineering waitlist new power projects and large loads face before plugging into the regional transmission grid.]] "
                "through modest peak flexibility and surplus-capacity reuse, condition federal water and energy aid on "
                "closed-loop, hybrid adiabatic, or reclaimed cooling, and close methane-turbine air permitting loopholes."
            ),
        ],
        "sections": [
            {
                "id": "grid-cost-causation",
                "toc_num": "01",
                "kicker": "Section 01 · Transmission & Capacity Rates",
                "toc_label": "Cost-causation tariffs",
                "heading": "1. Require 100% cost-causation tariffs with minimum-term collateral",
                "paragraphs": [
                    (
                        "Through [[term-2|FERC|FERC (Federal Energy Regulatory Commission)|The independent federal agency that regulates interstate electricity transmission and wholesale power markets, while state public utility commissions regulate retail rates.]] "
                        "wholesale transmission and capacity rules, Department of Energy grid-grant conditions, and state public "
                        "utility commission rate standards, policymakers should require "
                        "[[term-2|100% cost-causation tariffs|100% cost-causation tariffs|A wholesale and retail rate rule requiring a giant new electricity user, such as a hyperscale data center, to pay the full cost of the grid upgrades and power capacity it triggers so residential bills do not rise.]] "
                        "paired with minimum-term financial collateral for hyperscale loads (such as facilities or "
                        "campuses over 20 megawatts)."
                    ),
                    (
                        "Mandatory collateral ensures residential customers and small businesses never subsidize Big Tech "
                        "substation buildouts or inherit stranded grid debt if a speculative project cancels, consolidates "
                        "workloads elsewhere, or misses load forecasts."
                    ),
                ],
            },
            {
                "id": "clean-interconnection",
                "toc_num": "02",
                "kicker": "Section 02 · Clean Power, Curtailment & Reconductoring",
                "toc_label": "Clean queues and flexibility",
                "heading": "2. Pair clean-power interconnection priority with peak load curtailment",
                "paragraphs": [
                    (
                        "Congress and FERC should reserve fast-track [[term-3|interconnection queues|Interconnection queues|The multi-year engineering waitlist new power projects and large loads face before plugging into the grid.]] "
                        "for large facilities that bring new, deliverable clean generation on a rising hourly-matched "
                        "schedule (using near-term solar and battery storage while scaling [[term-6|enhanced geothermal]] "
                        "and nuclear) and agree to trim non-urgent runs, shift regional workloads, or draw clean on-site "
                        "storage without running diesel or fossil-methane backup by 0.25% to 1% of annual electricity use "
                        "(mostly partial drawdowns across roughly 85 to 366 peak grid-stress hours a year, equal to 22 "
                        "to 88 full-load hours)."
                    ),
                    (
                        "Companion 2025 and 2026 studies from Duke University's Nicholas Institute find that curtailing "
                        "grid withdrawals during those peak hours unlocks 76 to 126 gigawatts of headroom across U.S. "
                        "grids (which federal rules should pair with a strict ban on fossil backup shifting), while broader "
                        "data-center load flexibility scaling up to 50% of flexible hours cuts U.S. power-system capital, "
                        "operating, and fuel costs by $40 billion to $150 billion over ten years (verified against "
                        "[[term-4|peak curtailment]] dispatch telemetry)."
                    ),
                    (
                        "Congress should also authorize FERC to speed up advanced transmission "
                        "[[term-5|reconductoring|Advanced reconductoring|Replacing aging steel-core wires on existing transmission towers with composite-core conductors that carry roughly twice as much power without multi-year land acquisition for new corridors.]] "
                        "and dynamic line ratings on existing corridors, and prioritize non-emitting power and storage "
                        "interconnections that reuse spare hookup capacity at operating plants under "
                        "[[term-3|Order 845|FERC Order 845 and generator replacement|FERC Order 845 (surplus interconnection) lets new generation or batteries share unused hookup capacity at an operating power plant, while generator-replacement rules let new projects reuse the existing hookup when an older plant retires; both are currently fuel-neutral rules that Congress and FERC can pair with clean-power priority.]] "
                        "or retiring coal sites under a nationwide generator-replacement rule."
                    ),
                ],
            },
            {
                "id": "water-air-loopholes",
                "toc_num": "03",
                "kicker": "Section 03 · Water Conservation & Air Permitting",
                "toc_label": "Water and turbine loopholes",
                "heading": "3. Condition federal water funds and close methane-turbine air loopholes",
                "paragraphs": [
                    (
                        "On water, Water Foundation and Brookings analyses show that a single hyperscale facility can draw "
                        "1 million to 5 million gallons of treated water a day in dry basins. Because federal agencies "
                        "cannot set municipal water rates directly, Congress should condition future EPA State Revolving Fund "
                        "and Bureau of Reclamation water-project grants, while the executive branch conditions discretionary "
                        "DOE loans and facilities serving federal cloud contracts, on ending subsidized potable water "
                        "discounts for large data centers."
                    ),
                    (
                        "Those funding conditions should require zero-evaporation "
                        "[[term-7|closed-loop|Closed-loop cooling|Sealed heat-exchange cooling systems that recirculate fluid continuously without evaporating municipal water, trading higher peak-heat electricity use for near-zero operational water draw.]], "
                        "[[term-7|hybrid adiabatic|Hybrid adiabatic cooling|Dry-cooler systems that run without water most of the year and use limited evaporative misting only during the hottest summer hours, cutting annual water draw sharply compared with open cooling towers.]], "
                        "or [[term-7|reclaimed municipal wastewater|Reclaimed municipal wastewater|Treated municipal wastewater piped to industrial facilities for non-potable cooling instead of drawing local drinking water.]] "
                        "cooling in water-stressed basins, paired with automatic drought cutbacks on any remaining potable draw."
                    ),
                    (
                        "On air pollution, Congress and the EPA should close loopholes for methane turbines powering fixed "
                        "data centers by repealing the 2026 Subpart KKKKa 24-month temporary-turbine (25 ppm NOx) and "
                        "sub-45% capacity-factor SCR subcategories for dedicated data-center generation, blocking EPA's "
                        "proposed Nonroad Combustion Turbines Rule (RIN 2060-AX08) and barring "
                        "[[term-8|nonroad-engine claims|Methane-turbine permitting loopholes|Some fixed data centers have run trailer-mounted or modular methane turbines without major-source air controls by claiming Clean Air Act nonroad-engine exemptions meant for movable equipment or short-term Subpart KKKKa stationary subcategories.]], "
                        "counting co-located turbines together under major-source limits, codifying *Michigan v. DOE* limits "
                        "against multi-year Federal Power Act Section 202(c) coal and gas retirement overrides, and "
                        "statutorily barring Clean Air Act Section 110(f) and Section 112(i)(4) waivers for commercial data "
                        "centers. That ends the unpermitted gas-turbine and emergency fossil practices documented in NAACP, "
                        "Southern Environmental Law Center, and Earthjustice filings in South Memphis, Southaven, Mississippi, "
                        "and federal grid dockets."
                    ),
                ],
            },
        ],
        "tradeoffs": [
            {
                "eyebrow": "01 · Permitting Scope & Community Safeguards",
                "body": (
                    "Fast-tracking clean energy infrastructure can fracture center-left coalitions if permitting bills "
                    "sweep too broadly, as *Time* documented during the 2025 and 2026 permitting battles. Statutory "
                    "fast-tracks must stay tightly scoped to interregional transmission timelines, reconductoring, "
                    "dynamic line ratings, geothermal exploration, and battery or zero-carbon generation on low-conflict "
                    "or remediated sites, while preserving Tribal consultation and cumulative fenceline safeguards "
                    "everywhere and never granting fast-tracks or weaker NEPA and Clean Air Act enforcement to fossil "
                    "projects, as demanded by the Sierra Club and frontline community groups."
                ),
            }
        ],
        "references": [
            (
                "Tyler H. Norris et al., *Rethinking Load Growth: Assessing the Potential for Integration of Large Flexible "
                "Loads in US Power Systems* (Feb. 2025), and Martin T. Ross and Jackson Ewing, *Data Centers and Generation "
                "Capacity over the Next Decade: Potential Benefits of Flexibility* (Feb. 2026), Duke University Nicholas Institute"
            ),
            (
                "PJM Interconnection Independent Market Monitor (Monitoring Analytics) 2025/2026 BRA analysis & U.S. "
                "Department of Energy resource-adequacy and large-load docket filings (2025-2026)"
            ),
            (
                "Water Foundation & Brookings Institution analyses of hyperscale data-center municipal water demand (2025-2026); "
                "NAACP, Southern Environmental Law Center, and Earthjustice air-permitting filings (South Memphis, TN; Southaven, MS)"
            ),
            (
                "U.S. EPA Standards of Performance for Stationary Combustion Turbines (40 C.F.R. Part 60 Subpart KKKKa, Jan. 2026), "
                "proposed Nonroad Combustion Turbines Rule (RIN 2060-AX08), and *Michigan v. DOE* Federal Power Act Section 202(c) litigation (2026)"
            ),
        ],
        "glossary": [
            {
                "id": "term-1",
                "cat": "grid",
                "dt": "PJM grid and wholesale capacity auctions",
                "dd": (
                    "PJM Interconnection is America's largest regional grid operator, managing wholesale electricity across "
                    "13 Mid-Atlantic and Midwest states plus Washington, D.C. Its capacity auctions pay power plants in advance "
                    "to guarantee enough supply during future peak demand; surging data-center power forecasts have driven "
                    "those auction prices sharply higher on household bills."
                ),
            },
            {
                "id": "term-2",
                "cat": "grid",
                "dt": "FERC, state utility commissions, and 100% cost-causation tariffs",
                "dd": (
                    "FERC (the Federal Energy Regulatory Commission) regulates interstate electricity transmission and wholesale "
                    "power markets, while state public utility commissions set retail electricity rates. A 100% cost-causation "
                    "tariff is a wholesale and retail rate rule requiring a giant new electricity user, such as a hyperscale "
                    "data center, to pay the full cost of the grid upgrades and power capacity it triggers so residential "
                    "bills do not rise."
                ),
            },
            {
                "id": "term-3",
                "cat": "grid",
                "dt": "Interconnection queues, Order 845, and generator replacement",
                "dd": (
                    "The interconnection queue is the multi-year engineering waitlist new power projects and large loads face "
                    "before plugging into the grid. FERC Order 845 (\"surplus interconnection\") lets new generation or batteries "
                    "share unused hookup capacity at an operating power plant, while generator-replacement rules let new projects "
                    "reuse the existing grid hookup when an older plant retires; both are currently fuel-neutral rules that "
                    "Congress and FERC can pair with clean-power priority and a nationwide replacement standard at operating "
                    "or retiring fossil sites."
                ),
            },
            {
                "id": "term-4",
                "cat": "grid",
                "dt": "Peak load curtailment",
                "dd": (
                    "A binding grid agreement where a data center trims non-urgent computing jobs, shifts regional workloads, "
                    "or draws clean on-site battery storage (without running diesel or fossil-methane backup generators) during "
                    "the grid's highest-stress summer and winter hours so utilities do not have to build billions of dollars in "
                    "extra fossil-fuel peaker plants."
                ),
            },
            {
                "id": "term-5",
                "cat": "grid",
                "dt": "Advanced reconductoring and dynamic line ratings",
                "dd": (
                    "Advanced reconductoring replaces old steel-core wires on existing transmission towers with modern "
                    "composite-core cables that carry roughly twice as much electricity without multi-year land fights for new "
                    "towers. Dynamic line ratings use real-time wind and temperature sensors so grid operators can safely send "
                    "more power through existing wires on cool or breezy days."
                ),
            },
            {
                "id": "term-6",
                "cat": "grid",
                "dt": "Enhanced geothermal",
                "dd": (
                    "Clean baseload energy that uses modern directional rock-drilling techniques to tap natural heat miles "
                    "underground and generate steady 24/7 carbon-free electricity with a small land footprint."
                ),
            },
            {
                "id": "term-7",
                "cat": "water",
                "dt": "Closed-loop, hybrid adiabatic, and reclaimed-water cooling",
                "dd": (
                    "Closed-loop chillers recirculate fluid in sealed heat exchangers with zero evaporative water loss "
                    "(at the cost of slightly higher hot-afternoon electricity draw), while hybrid adiabatic systems run "
                    "dry most of the year and use evaporative misting only on extreme heat hours. Reclaimed (recycled) "
                    "water is treated municipal wastewater piped to industrial campuses for non-potable cooling instead "
                    "of drawing local drinking water."
                ),
            },
            {
                "id": "term-8",
                "cat": "water",
                "dt": "Methane-turbine permitting loopholes (Subpart KKKKa and nonroad claims)",
                "dd": (
                    "Fixed data centers have run modular or trailer-mounted methane gas turbines outside major-source "
                    "pollution controls by claiming Clean Air Act nonroad-engine status meant for movable machinery (which "
                    "EPA's RIN 2060-AX08 proposal would widen) or using EPA's January 2026 Subpart KKKKa temporary (up to "
                    "24 months) and low-capacity-factor stationary turbine subcategories."
                ),
            },
        ],
        "glossary_groups": [
            ("grid", "Power grid and interconnection"),
            ("water", "Water cooling and air permitting"),
        ],
    },
    {
        "num": "02",
        "code": "Brief 2026-01B",
        "slug": "compute-antitrust",
        "hub_section_id": "compute-antitrust",
        "nav_label": "Compute & Antitrust",
        "short_toc": "Compute & antitrust",
        "title": "Public compute, open-weight models, and algorithmic antitrust",
        "hub_kicker": "Pillar 02 · Public Compute & Antitrust",
        "hub_heading": "2. Break Big Tech compute bottlenecks and ban algorithmic price-fixing",
        "read_time": "4 min read",
        "md_filename": "compute-antitrust-brief.md",
        "pdf_filename": "compute-antitrust-brief.pdf",
        "og_filename": "og-spoke-02.png",
        "og_eyebrow": "Brief 2026-01B · Michael Paulauski · November 2026",
        "og_pills": [
            "CREATE AI Act & NAIRR",
            "Open-Weight Competition",
            "Cloud-Tying & Acqui-Hire Enforcement",
            "No Algorithmic Price-Fixing",
        ],
        "meta_description": (
            "Breaking cloud-compute concentration via public NAIRR infrastructure and the CREATE AI Act, protecting "
            "open-weight AI models, blocking reverse acqui-hires and cloud tying, and banning pooled algorithmic price-fixing."
        ),
        "og_description": (
            "Bipartisan CREATE AI Act public compute, open-weight software competition, antitrust enforcement against "
            "cloud tying and acqui-hires, and banning shared algorithmic price-fixing."
        ),
        "metrics": [
            {
                "figure": "2.7% / 3.3%",
                "label": "U.S.-China frontier benchmark gap vs. closed-to-open-weight gap as open models scale.",
                "cite": "Stanford HAI AI Index (2026); CSIS; Lowy Institute",
            },
            {
                "figure": "$35M -> $2.6B",
                "label": "Sept. 2026 NSF NAIRR Operations Center award vs. permanent CREATE AI Act authorization.",
                "cite": "NSF NAIRR-OC (Sept. 2026); CREATE AI Act",
            },
        ],
        "bluf_paragraphs": [
            (
                "Leaving frontier AI in the hands of four or five cloud conglomerates concentrates too much economic and "
                "political power while stifling independent researchers, hospitals, and startups. At the same time, "
                "Stanford AI Index, CSIS, and Lowy Institute tracking shows that despite U.S. chip export restrictions, "
                "Chinese labs such as DeepSeek and Alibaba have narrowed frontier benchmark gaps to roughly 2.7% through "
                "[[term-2|open-weight]] software releases."
            ),
            (
                "Federal competition policy should expand public compute infrastructure, keep open-weight AI legal to "
                "deploy on local hardware, police Big Tech cloud-compute tying and disguised mergers, and outlaw "
                "shared pricing algorithms that coordinate rents and consumer prices."
            ),
        ],
        "sections": [
            {
                "id": "public-compute-open-weights",
                "toc_num": "01",
                "kicker": "Section 01 · Public Infrastructure & Open Weights",
                "toc_label": "NAIRR and open weights",
                "heading": "1. Fund permanent NAIRR public compute and keep open-weight models legal",
                "paragraphs": [
                    (
                        "Building on the National Science Foundation's September 2026 $35 million launch of the "
                        "[[term-3|NAIRR]] Operations Center (in partnership with the Department of Energy), Congress should "
                        "pass the bipartisan CREATE AI Act and appropriate multi-billion-dollar funding for publicly owned "
                        "supercomputing and zero-egress, vendor-neutral cloud vouchers at national labs and university "
                        "centers."
                    ),
                    (
                        "Direct public funding guarantees that academic researchers, teaching hospitals, civic institutions, "
                        "and independent startups receive real pre-competitive R&D, open-science training, and "
                        "public-interest model validation capacity without relying on revocable, lock-in Big Tech cloud credits."
                    ),
                    (
                        "Federal policy should also keep open-weight AI models below Pillar 6's catastrophic bio-cyber "
                        "tripwires legal so smaller firms, regional hospitals, and municipal institutions can inspect and "
                        "run [[term-1|AI agents]] on local or domestic servers without paying permanent rent or ceding "
                        "sensitive operational data to closed corporate APIs."
                    ),
                ],
            },
            {
                "id": "antitrust-collusion",
                "toc_num": "02",
                "kicker": "Section 02 · Competition Enforcement & Price-Fixing",
                "toc_label": "Cloud tying and price-fixing",
                "heading": "2. Police cloud tying, disguised acqui-hires, and algorithmic collusion",
                "paragraphs": [
                    (
                        "On antitrust, the FTC and DOJ should block exclusive cloud-compute tying agreements and "
                        "discriminatory accelerator allocation bottlenecks, while Congress modernizes the Hart-Scott-Rodino "
                        "Act (15 U.S.C. Section 18a, following the February 2026 judicial vacatur of expanded HSR rules in "
                        "*Chamber of Commerce v. FTC*) so dominant-platform [[term-4|\"acqui-hire\"]] deals pairing talent "
                        "buyouts with exclusive or quasi-exclusive IP licenses face mandatory premerger review."
                    ),
                    (
                        "Closing the 12-month aged-data training loophole left in DOJ's May 2026 *RealPage* consent judgment "
                        "(and building on state statutes like California's AB 325), Congress should pass a targeted "
                        "Preventing Algorithmic Collusion Act to outlaw [[term-5|shared pricing algorithms]] that pool or "
                        "train on current or historical nonpublic competitor data or coordinate competitor pricing across "
                        "rival firms."
                    ),
                    (
                        "To avoid interfering with ordinary business analytics, the statute should explicitly spare "
                        "proprietary or non-pooled single-merchant pricing and inventory software that uses only a firm's "
                        "own operational data and public market prices without cross-competitor price coordination, "
                        "keeping enforcement squarely aimed at competing landlords and corporations inflating rents and "
                        "consumer prices in lockstep."
                    ),
                ],
            },
        ],
        "tradeoffs": [
            {
                "eyebrow": "02 · Open Innovation vs. Oligopoly Capture",
                "body": (
                    "Restrictive model-licensing schemes sold under the banner of safety tend to entrench the largest cloud "
                    "incumbents while pushing open development toward foreign labs. Pairing permanent public compute under "
                    "NAIRR with legal open-weight distribution preserves domestic competition and lowers market-entry costs, "
                    "while pairing narrow frontier catastrophic tripwires (covered in Brief 2026-01F) with antitrust "
                    "enforcement targets actual concentration and collusion risks instead of open code."
                ),
            }
        ],
        "references": [
            (
                "Stanford HAI, *AI Index Report* (2025-2026); CSIS and Lowy Institute assessments of global open-weight "
                "AI adoption and U.S.-China frontier capability gaps (2025-2026)"
            ),
            (
                "National Science Foundation & Department of Energy, $35M NAIRR Operations Center award (Sept. 2026); "
                "bipartisan CREATE AI Act (H.R. 2385 / S. 4441)"
            ),
            (
                "U.S. Department of Justice *United States v. RealPage* Final Judgment (May 2026) and California AB 325; "
                "FTC Section 6(b) cloud-compute and reverse acqui-hire inquiries and *Chamber of Commerce v. FTC* HSR "
                "litigation (2024-2026)"
            ),
        ],
        "glossary": [
            {
                "id": "term-1",
                "cat": "compute",
                "dt": "AI agents (\"agentic\" AI)",
                "dd": (
                    "AI agents are software systems that go beyond answering single chat prompts to plan and execute "
                    "multi-step tasks across external software tools, databases, and enterprise workflows, such as organizing "
                    "hospital records, writing code, or triaging customer tickets, where unverified actions can compound "
                    "across connected systems."
                ),
            },
            {
                "id": "term-2",
                "cat": "compute",
                "dt": "Open-weight models vs. closed APIs",
                "dd": (
                    "An open-weight model releases its trained numerical parameters (\"weights\") publicly so universities, "
                    "hospitals, and smaller firms can download and run the software on their own servers or local hardware. "
                    "Closed APIs keep the model locked on a tech company's servers and charge customers ongoing fees for access."
                ),
            },
            {
                "id": "term-3",
                "cat": "compute",
                "dt": "NAIRR public compute and the CREATE AI Act",
                "dd": (
                    "NAIRR (the National Artificial Intelligence Research Resource) is an NSF-led federal public-compute "
                    "initiative (with Department of Energy national-lab participation) that launched its $35 million "
                    "Operations Center in September 2026; the bipartisan CREATE AI Act permanently authorizes NAIRR and "
                    "scales publicly owned supercomputing and vendor-neutral cloud resources for academic, nonprofit, "
                    "civic, and startup R&D."
                ),
            },
            {
                "id": "term-4",
                "cat": "antitrust",
                "dt": "\"Acqui-hires\" and HSR premerger review",
                "dd": (
                    "A deal structure (often called a reverse acqui-hire) where a tech giant hires away a startup's founders "
                    "and core engineering team while taking an exclusive or quasi-exclusive IP license to gain effective "
                    "control without triggering standard Hart-Scott-Rodino (15 U.S.C. Section 18a) antitrust premerger review."
                ),
            },
            {
                "id": "term-5",
                "cat": "antitrust",
                "dt": "Algorithmic collusion vs. independent pricing tools",
                "dd": (
                    "Algorithmic collusion occurs when competing landlords or businesses feed or train shared third-party "
                    "pricing software on current or historical nonpublic pricing, occupancy, or supply data to coordinate "
                    "prices above competitive levels. Independent single-merchant tools analyze only public market prices "
                    "and a firm's own internal operational data."
                ),
            },
        ],
        "glossary_groups": [
            ("compute", "Models and public compute"),
            ("antitrust", "Antitrust and pricing rules"),
        ],
    },
    {
        "num": "03",
        "code": "Brief 2026-01C",
        "slug": "civil-liberties",
        "hub_section_id": "civil-liberties-justice",
        "nav_label": "Civil Liberties",
        "short_toc": "Rights, courts & health",
        "title": "Statutory civil-liberties, courtroom, and patient-care guardrails",
        "hub_kicker": "Pillar 03 · Civil Liberties, Courts & Health Care",
        "hub_heading": "3. Set statutory civil-liberties, courtroom, and patient-care guardrails while expanding indigent defense and vetted legal-aid tools",
        "read_time": "5 min read",
        "md_filename": "civil-liberties-brief.md",
        "pdf_filename": "civil-liberties-brief.pdf",
        "og_filename": "og-spoke-03.png",
        "og_eyebrow": "Brief 2026-01C · Michael Paulauski · November 2026",
        "og_pills": [
            "Human Warfighting & Nuclear Control",
            "No Warrantless Broker Surveillance",
            "Indigent Defense & AI Evidence Rules",
            "Physician Sign-Off on Health Denials",
        ],
        "meta_description": (
            "Binding human-control rules on lethal force and nuclear launch, warrant requirements for biometric dragnets "
            "and data brokers, expanded legal aid alongside black-box courtroom bans, and physician sign-off over health-care denials."
        ),
        "og_description": (
            "Statutory lethal-force and nuclear human-control lines, warrant rules on data brokers, indigent defense "
            "capacity and reworked Rule 707 and deepfake evidence rules, and stopping automated health-insurance denials."
        ),
        "metrics": [
            {
                "figure": "92%",
                "label": "Low-income Americans' substantial civil legal problems receiving inadequate or no legal help.",
                "cite": "Legal Services Corporation Justice Gap Report (2022)",
            },
            {
                "figure": "6 States",
                "label": "Original Medicare states testing private AI prior-auth contractors under CMS WISeR.",
                "cite": "Centers for Medicare & Medicaid Services (2026)",
            },
        ],
        "bluf_paragraphs": [
            (
                "As the 2026 Pentagon vendor dispute analyzed by Just Security and the Electronic Frontier Foundation showed, "
                "constitutional and human-rights boundaries cannot rest on private contract standoffs between one AI lab "
                "and defense officials. Meanwhile, black-box algorithms are increasingly shaping policing, public benefits, "
                "bail, and health-insurance coverage while low-income Americans face a severe shortage of human legal counsel."
            ),
            (
                "Congress should enact bright-line statutory rules governing defense autonomy and domestic surveillance, "
                "separate vetted citizen legal-aid access from coercive state scoring, and stop health insurers and Medicare "
                "contractors from using algorithms to ration care."
            ),
        ],
        "sections": [
            {
                "id": "defense-surveillance",
                "toc_num": "01",
                "kicker": "Section 01 · Defense Authority & Fourth Amendment Limits",
                "toc_label": "Warfighting and surveillance",
                "heading": "1. Codify human command over lethal force and close surveillance loopholes",
                "paragraphs": [
                    (
                        "Congress should enact binding defense appropriations and fielding prohibitions requiring meaningful "
                        "human verification and command authorization over anti-personnel target selection and offensive "
                        "lethal force (barring automated kill-list rubber-stamping while preserving point-defense "
                        "counter-munitions against incoming projectiles), alongside a binding statutory ban on autonomous "
                        "AI in nuclear command, control, and launch decisions."
                    ),
                    (
                        "For domestic policing and intelligence, Congress should require judicial warrants (subject only to "
                        "narrow, audited imminent-life-safety exigencies and backed by statutory suppression remedies) for "
                        "government AI facial-recognition and networked camera dragnets, and enact the Fourth Amendment Is "
                        "Not For Sale Act to close the commercial [[term-2|data-broker loophole]] documented by the ACLU and "
                        "GAO, where intelligence and police agencies buy bulk phone-location and web-browsing records without "
                        "a warrant."
                    ),
                ],
            },
            {
                "id": "courts-legal-aid",
                "toc_num": "02",
                "kicker": "Section 02 · Courts, Public Defense & Benefits Due Process",
                "toc_label": "Legal aid, courts, and benefits",
                "heading": "2. Fund indigent defense and audited legal aid while barring black-box scoring",
                "paragraphs": [
                    (
                        "Inside the justice system, policy should separate citizen access from institutional coercion. The Legal "
                        "Services Corporation's Justice Gap Report finds that 92% of low-income Americans' substantial civil "
                        "legal problems receive inadequate or no legal help. Alongside expanded funding to hire human legal-aid "
                        "attorneys and public defenders, Congress should expand Legal Services Corporation and State Justice "
                        "Institute technology grants for vetted civil tools, like those piloted at Stanford's Legal Design Lab, "
                        "that help low-income tenants and veterans handle evictions, consumer debt, and benefits claims."
                    ),
                    (
                        "Because federal law bars LSC from criminal cases, Congress should pair civil legal-aid funding with "
                        "ring-fenced Department of Justice [[term-1|Byrne JAG|Byrne JAG and LSC legal-aid funding|Byrne JAG is the primary Department of Justice grant program supporting state and local criminal-justice systems (including indigent public defense), whereas the Legal Services Corporation (LSC) funds civil legal aid for low-income households and is barred by federal statute from criminal cases.]] "
                        "public-defender grants and federal Judiciary Defender Services funding so overworked defense lawyers can "
                        "use zero-retention, privilege-protected, audited AI to review criminal discovery files."
                    ),
                    (
                        "At the same time, federal statute should bar unreviewed automated or black-box algorithms from federal "
                        "sentencing and federally funded benefits denials (including Medicaid, SNAP, and veterans' benefits), "
                        "while conditioning state Byrne JAG funds on barring algorithmic risk-assessment scores in pre-trial "
                        "detention, bail, and sentencing. Congress and the Judicial Conference should also finish reworking the "
                        "[[term-3|Rule 707|Daubert reliability, withdrawn Proposed Rule 707, and Rule 901(c)|Daubert is the federal courtroom standard requiring expert technical evidence to prove its reliability before reaching a jury; after withdrawing Proposed Rule 707 in May 2026 for revision, the Judicial Conference Advisory Committee on Evidence Rules is reworking machine-evidence reliability and companion Rule 901(c) deepfake-authentication standards.]] "
                        "draft withdrawn in May 2026 and companion Rule 901(c) deepfake-authentication rules to set strict "
                        "Daubert-grade reliability standards for criminal and civil trials without pricing out or blocking "
                        "authentic bystander recordings."
                    ),
                ],
            },
            {
                "id": "health-care-denials",
                "toc_num": "03",
                "kicker": "Section 03 · Health Insurance & Patient Care",
                "toc_label": "Prior authorization and WISeR",
                "heading": "3. Ban algorithmic health-care denials and vendor denial bounties",
                "paragraphs": [
                    (
                        "Following federal lawsuits over Medicare Advantage prior-authorization algorithms and the unanimous "
                        "June 2026 House Appropriations Committee vote to defund Original Medicare's six-state "
                        "[[term-5|WISeR]] pilot, Congress should halt WISeR and direct HHS and the Department of Labor to set "
                        "an enforceable patient-review standard across public and private coverage."
                    ),
                    (
                        "Federal statute and agency rules should prohibit Medicare Advantage and Medicaid managed-care plans, "
                        "federal Medicare contractors, Federal Employees Health Benefits plans, ERISA group health plans, and "
                        "commercial insurers under the Public Health Service Act from denying medical necessity or cutting off "
                        "post-acute care by algorithm without documented, individualized review of the patient record by a "
                        "licensed physician or qualified health-care specialist acting within clinical scope of practice (while "
                        "permitting automated fast-track approvals)."
                    ),
                    (
                        "Rules should equally ban denial-based bounties or savings quotas for both outside contractors and "
                        "in-house insurer reviewers, and pair a federal statutory remedy with an explicit savings clause so "
                        "ERISA (including self-funded plans), Medicare Advantage, and FEHBA preemption never shield unlawful "
                        "algorithmic care denials from state bad-faith accountability."
                    ),
                ],
            },
        ],
        "tradeoffs": [
            {
                "eyebrow": "03 · Courtroom Access vs. Hallucination Risk",
                "body": (
                    "State court administrators and the National Center for State Courts warn that low-income litigants "
                    "rarely have a second lawyer to catch AI [[term-4|hallucinations]], which empirical tests by Stanford "
                    "researchers still find in commercial legal tools. Publicly funded legal-aid software must carry "
                    "mandatory independent accuracy audits, court-approved, attorney-vetted template bounds for pro se "
                    "self-help tools, and human attorney sign-off on open-ended generative court briefs."
                ),
            }
        ],
        "references": [
            (
                "Just Security & Electronic Frontier Foundation analyses of 2026 Pentagon AI vendor disputes; FY2025 NDAA "
                "nuclear command-and-control provisions; ACLU & GAO reports on federal purchases of commercial data-broker records"
            ),
            (
                "Legal Services Corporation, *The Justice Gap: The Unmet Civil Legal Needs of Low-Income Americans* (2022); "
                "U.S. Judicial Conference Advisory Committee on Evidence Rules, Proposed Rule 707 withdrawal (May 2026) and "
                "Rule 901(c) rulemaking record"
            ),
            (
                "Centers for Medicare & Medicaid Services, WISeR six-state pilot documentation (2026), House Appropriations "
                "WISeR defunding action (June 2026), and *Lokken* / *Barrows* Medicare Advantage preemption litigation"
            ),
        ],
        "glossary": [
            {
                "id": "term-1",
                "cat": "law",
                "dt": "Byrne JAG and LSC legal-aid funding",
                "dd": (
                    "Byrne JAG is the primary Department of Justice grant program supporting state and local criminal-justice "
                    "systems (including indigent public defense), whereas the Legal Services Corporation (LSC) funds civil "
                    "legal aid for low-income households and is barred by federal statute from criminal cases."
                ),
            },
            {
                "id": "term-2",
                "cat": "law",
                "dt": "Commercial data-broker loophole",
                "dd": (
                    "The practice where intelligence agencies and police departments buy bulk phone-location, web-browsing, and "
                    "personal records from commercial data brokers on the open market to track Americans without getting a "
                    "Fourth Amendment court warrant."
                ),
            },
            {
                "id": "term-3",
                "cat": "law",
                "dt": "Daubert reliability, withdrawn Proposed Rule 707, and Rule 901(c)",
                "dd": (
                    "Daubert is the federal courtroom standard requiring expert technical evidence to prove reliable methods "
                    "before reaching a jury. After withdrawing Proposed Rule 707 in May 2026 for refinement, the Judicial "
                    "Conference Advisory Committee on Evidence Rules is developing updated machine-generated evidence "
                    "reliability standards alongside Rule 901(c) procedures for challenging suspected deepfakes."
                ),
            },
            {
                "id": "term-4",
                "cat": "law",
                "dt": "AI hallucinations in legal software",
                "dd": (
                    "Hallucinations are plausible-sounding false facts, invented citations, or misstated holdings produced "
                    "because generative AI predicts token patterns, a failure mode that persists even when legal tools "
                    "retrieve verified case records."
                ),
            },
            {
                "id": "term-5",
                "cat": "health",
                "dt": "Medicare Advantage prior authorization and WISeR",
                "dd": (
                    "Prior authorization requires insurer sign-off before a clinician's prescribed treatment or ongoing "
                    "post-acute care is covered. WISeR (Wasteful and Inappropriate Service Reduction) is CMS's 2026 six-state "
                    "pilot (AZ, NJ, OH, OK, TX, WA) introducing private AI prior-authorization contractors paid a share of "
                    "averted spending into traditional Original Medicare."
                ),
            },
        ],
        "glossary_groups": [
            ("law", "Surveillance, courts, and legal aid"),
            ("health", "Health insurance and Medicare"),
        ],
    },
    {
        "num": "04",
        "code": "Brief 2026-01D",
        "slug": "workers-taxes",
        "hub_section_id": "workers-taxes",
        "nav_label": "Workers & Taxes",
        "short_toc": "Workers, taxes & wages",
        "title": "Worker tax parity, workplace AI rules, and displacement insurance",
        "hub_kicker": "Pillar 04 · Worker Taxes, Bossware & Wage Insurance",
        "hub_heading": "4. Equalize worker taxes, ban abusive \"bossware,\" and insure workers against agentic displacement",
        "read_time": "5 min read",
        "md_filename": "workers-taxes-brief.md",
        "pdf_filename": "workers-taxes-brief.pdf",
        "og_filename": "og-spoke-04.png",
        "og_eyebrow": "Brief 2026-01D · Michael Paulauski · November 2026",
        "og_pills": [
            "Bonus Depreciation Tax Parity",
            "No Bossware or Forced Arbitration",
            "Federal Wage Insurance",
            "90-Day WARN & Sectoral Training",
        ],
        "meta_description": (
            "Ending tax favoritism for so-so automation, outlawing abusive bossware quotas and forced arbitration, "
            "requiring NLRA bargaining, and pairing 90-day WARN notice with wage insurance and sectoral apprenticeships."
        ),
        "og_description": (
            "Correcting the 25.5%-33.5% vs. ~5% labor-to-software tax gap, banning bossware and forced arbitration, "
            "enacting 50% federal wage insurance, and updating the WARN Act."
        ),
        "metrics": [
            {
                "figure": "25.5%-33.5% vs. ~5%",
                "label": "Effective U.S. tax rate on human labor vs. software and equipment under 100% bonus depreciation.",
                "cite": "Acemoglu, Manera & Restrepo, Brookings (2020)",
            },
            {
                "figure": "71% / 73%",
                "label": "Americans expecting AI to reduce total U.S. jobs over 20 years, peaking at 73% under age 30.",
                "cite": "Pew Research Center (2026)",
            },
            {
                "figure": "50% / $15k-$20k/yr",
                "label": "Annual earnings-drop replacement cap (for up to two years) under proposed federal wage insurance.",
                "cite": "Adapted from Hamilton Project / Brookings models",
            },
            {
                "figure": "90 Days",
                "label": "Upgraded federal WARN notice covering distributed remote and rolling mass layoffs.",
                "cite": "Federal WARN Act Modernization Pillar",
            },
        ],
        "bluf_paragraphs": [
            (
                "Pew Research finds that 71% of Americans expect AI to reduce total U.S. jobs over the next two decades, "
                "with concern among adults under 30 jumping from 61% in 2024 to 73% in 2026. Yet current U.S. tax law "
                "tilts employers toward replacing workers even when automation barely breaks even, while outdated WARN "
                "thresholds and expired Trade Adjustment Assistance leave displaced staff without transition income."
            ),
            (
                "Instead of unworkable 'robot taxes' or low-return classroom vouchers, federal policy should fix the "
                "capital-vs-labor tax wedge, set hard workplace dignity and bargaining rights, and build automatic wage "
                "insurance and paid sectoral career paths."
            ),
        ],
        "sections": [
            {
                "id": "tax-parity",
                "toc_num": "01",
                "kicker": "Section 01 · Capital vs. Labor Tax Parity",
                "toc_label": "Tax parity and payroll credits",
                "heading": "1. Fix the bonus-depreciation wedge without penalizing open-weight software",
                "paragraphs": [
                    (
                        "Research by Daron Acemoglu, Andrea Manera, and Pascual Restrepo in *Brookings Papers on Economic Activity* "
                        "calculates that U.S. tax law imposes a 25.5% to 33.5% effective tax rate on human labor (combining "
                        "income and payroll taxes, and reaching 33.5% with benefit-phaseout taxes) while taxing software and "
                        "equipment at roughly 5%, a gap locked back in when the 2025 tax law restored permanent 100% first-year "
                        "[[term-1|bonus depreciation]] and immediate domestic software write-offs. That wedge subsidizes \"so-so "
                        "automation\" and pushes firms to replace staff with mediocre software largely for the tax break."
                    ),
                    (
                        "Congress should scale back corporate 100% bonus depreciation toward economic depreciation while carefully "
                        "preserving domestic R&D and software development expensing under Section 174A (so local open-weight "
                        "deployments are not taxed worse than cloud APIs deducted under Section 162), alongside small-business "
                        "Section 179 hardware limits, grid hardware, domestic chip fabs, and restored clean-energy tax "
                        "incentives cut back in July 2025."
                    ),
                    (
                        "Congress should pair the resulting corporate tax revenues with a refundable working-class payroll tax "
                        "credit backed by a mandatory dollar-for-dollar general-revenue transfer that keeps the Social Security "
                        "and Medicare Trust Funds completely whole."
                    ),
                ],
            },
            {
                "id": "workplace-rights-bargaining",
                "toc_num": "02",
                "kicker": "Section 02 · Workplace Dignity & Bargaining",
                "toc_label": "Bossware and NLRA bargaining",
                "heading": "2. Outlaw abusive \"bossware,\" forced arbitration, and secret deployments",
                "paragraphs": [
                    (
                        "On the job, federal labor law should require an accountable human decision-maker for hiring, firing, "
                        "pay, and work-speed safety, outlaw injury-inducing algorithmic quotas ([[term-2|\"bossware\"|\"Bossware\"|\"Bossware\" is workplace software that monitors keystrokes, cameras, or movement speed to enforce rigid quotas or automated discipline.]]), "
                        "and bar forced pre-dispute arbitration waivers over workplace AI violations so non-union workers can "
                        "actually enforce statutory protections."
                    ),
                    (
                        "Consistent with the AFL-CIO's Workers First Initiative on AI, Congress should guarantee workers advance "
                        "notice, vendor audit disclosures, and anti-retaliation protections before covered employers introduce "
                        "workplace surveillance, quota, or mass-displacement AI."
                    ),
                    (
                        "Under the National Labor Relations Act, Congress should make workplace surveillance and automated quotas "
                        "a mandatory subject of pre-deployment collective bargaining alongside mandatory effects bargaining over "
                        "severance, scheduling, and transition protections."
                    ),
                ],
            },
            {
                "id": "wage-insurance-warn-training",
                "toc_num": "03",
                "kicker": "Section 03 · Income Security & Paid Sectoral Transitions",
                "toc_label": "Wage insurance, WARN & training",
                "heading": "3. Pair federal wage insurance and modernized WARN with paid sectoral training",
                "paragraphs": [
                    (
                        "Tax parity only stops marginal automation; where capable AI agents outperform humans at a fraction of "
                        "payroll cost, mid-career cognitive workers will still face displacement where legacy retraining programs "
                        "like the expired Trade Adjustment Assistance system and generic WIOA classroom vouchers failed. Building "
                        "on Hamilton Project and Brookings models, Congress should enact federal [[term-2|wage insurance|Wage insurance|Wage insurance is a temporary federal paycheck supplement (such as covering half of a pay drop up to an indexed annual cap for two years) when a laid-off worker starts a new job at lower pay.]] "
                        "for displaced workers with at least one year of job tenure that temporarily replaces half of the earnings "
                        "drop (up to an inflation-indexed annual cap such as $15,000 to $20,000 for two years) when they take a "
                        "lower-paying job with a new employer."
                    ),
                    (
                        "Congress should also update the federal [[term-3|WARN Act|WARN Act|The federal WARN Act currently requires employers with 100 or more full-time workers to give 60 days' notice before plant closings affecting 50 or more workers, or single-site mass layoffs affecting at least 500 workers (or 50 to 499 workers making up at least one-third of active site staff).]] "
                        "so distributed remote and rolling mass layoffs trigger 90-day notice and mandatory severance transition "
                        "funding without reducing state unemployment benefits."
                    ),
                    (
                        "For skill transitions and younger entrants, federal workforce funds should shift away from generic "
                        "classroom vouchers toward paid apprenticeships and employer-backed sectoral training in shortage fields "
                        "like nursing, grid trades, and public-interest tech (high-performing sectoral models shown to raise "
                        "multi-year earnings in MDRC randomized trials, led over ten years by St. Nicks Alliance), paired with "
                        "broader Federal Unemployment Tax Act training-approval standards and extended UI stipends so displaced "
                        "workers keep income support during full-time programs. Finally, Congress should modernize "
                        "[[term-3|ERISA|ERISA multi-employer plans|ERISA governs private workplace health and retirement benefits, though its portable multi-employer benefit pools are currently limited largely to union collective-bargaining agreements.]] "
                        "multi-employer plan rules so unions and sectoral boards can run portable benefit pools across short-tenure "
                        "jobs without weakening W-2 misclassification laws."
                    ),
                ],
            },
        ],
        "tradeoffs": [
            {
                "eyebrow": "04 · Tax Parity & Reemployment vs. Robot Taxes",
                "body": (
                    "Tax economists across the spectrum warn that literal \"robot taxes\" or domestic AI compute taxes are "
                    "nearly impossible to define in tax law and risk pushing data centers abroad, while MDRC implementation "
                    "studies caution that high-performing sectoral training programs are hard to scale rapidly without deep "
                    "employer commitment. Pairing general bonus-depreciation reform with trust-fund-neutral payroll credits "
                    "and rapid-reemployment wage insurance cushions displaced workers immediately without taxing domestic "
                    "compute or stranding laid-off staff in low-return classes."
                ),
            }
        ],
        "references": [
            (
                "Daron Acemoglu, Andrea Manera, and Pascual Restrepo, \"Does the U.S. Tax Code Favor Automation?,\" "
                "*Brookings Papers on Economic Activity* (Spring 2020)"
            ),
            (
                "The Hamilton Project / Brookings Institution, wage-loss insurance and AI workforce transition proposals; "
                "MDRC, *WorkAdvance* 10-year follow-up (Sept. 2025) and sectoral employment randomized evaluations"
            ),
            (
                "AFL-CIO and AFL-CIO Technology Institute, *Workers First Initiative on AI* (2025); Pew Research Center, "
                "U.S. public opinion surveys on AI and employment (2025-2026)"
            ),
        ],
        "glossary": [
            {
                "id": "term-1",
                "cat": "tax",
                "dt": "100% bonus depreciation vs. economic depreciation (\"so-so automation\")",
                "dd": (
                    "Bonus depreciation (IRC Section 168(k)) lets businesses deduct the full cost of new and eligible used "
                    "equipment and purchased software in Year 1 instead of spreading deductions over the asset's useful working "
                    "life (economic depreciation), while Section 174A covers domestic R&D and cloud API subscriptions are "
                    "deducted as operating expenses under Section 162. Economists use \"so-so automation\" to describe mediocre "
                    "systems that barely match human staff and get deployed mainly because capital write-offs are taxed far "
                    "more lightly than human wages."
                ),
            },
            {
                "id": "term-2",
                "cat": "labor",
                "dt": "\"Bossware,\" wage insurance, and sectoral training",
                "dd": (
                    "\"Bossware\" is workplace software that monitors keystrokes, cameras, or movement speed to enforce rigid "
                    "quotas or automated discipline. Wage insurance is a temporary federal paycheck supplement (such as covering "
                    "half of a pay drop up to an indexed annual cap for two years) when a laid-off worker starts a new job at "
                    "lower pay. Sectoral training pairs public workforce funds directly with employers and unions to train and "
                    "hire workers for specific job shortages."
                ),
            },
            {
                "id": "term-3",
                "cat": "labor",
                "dt": "WARN Act, FUTA, and ERISA multi-employer plans",
                "dd": (
                    "The federal WARN Act currently requires employers with 100 or more full-time workers to give 60 days' "
                    "notice before plant closings affecting 50 or more workers, or single-site mass layoffs affecting at least "
                    "500 workers (or 50 to 499 workers making up at least one-third of active site staff). FUTA (the Federal "
                    "Unemployment Tax Act) sets federal baseline rules for state unemployment insurance. ERISA governs private "
                    "workplace health and retirement benefits, though its portable multi-employer benefit pools are currently "
                    "limited largely to union collective-bargaining agreements."
                ),
            },
        ],
        "glossary_groups": [
            ("tax", "Business tax rules"),
            ("labor", "Workplace law and income transitions"),
        ],
    },
    {
        "num": "05",
        "code": "Brief 2026-01E",
        "slug": "deepfakes-creators",
        "hub_section_id": "deepfakes-fraud",
        "nav_label": "Deepfakes & Creators",
        "short_toc": "Deepfakes & creators",
        "title": "Intimate-deepfake remedies, voice-clone fraud, and creator rights",
        "hub_kicker": "Pillar 05 · Deepfakes, Scams & Creator Rights",
        "hub_heading": "5. Close civil deepfake gaps, stop voice-clone fraud, and protect creator rights",
        "read_time": "4 min read",
        "md_filename": "deepfakes-creators-brief.md",
        "pdf_filename": "deepfakes-creators-brief.pdf",
        "og_filename": "og-spoke-05.png",
        "og_eyebrow": "Brief 2026-01E · Michael Paulauski · November 2026",
        "og_pills": [
            "DEFIANCE & NO FAKES Remedies",
            "Voice-Clone Wire Fraud & Caller ID",
            "Privacy-Clean C2PA & Watermarks",
            "Shadow-Library Ban & Licensing",
        ],
        "meta_description": (
            "Passing DEFIANCE civil remedies and NO FAKES consent rights with First Amendment safe harbors, stopping "
            "senior voice-clone scams, requiring privacy-clean synthetic provenance on hosted generators, banning pirated "
            "training laundering, and backing collective creator licensing."
        ),
        "og_description": (
            "Civil remedies via DEFIANCE and NO FAKES (with parody/news safe harbors), senior voice-clone fraud enforcement, "
            "hosted C2PA/watermark rules without identity tracking, and banning shadow-library laundering."
        ),
        "metrics": [
            {
                "figure": "48 Hours",
                "label": "Platform removal requirement for nonconsensual intimate images and deepfakes under the TAKE IT DOWN Act.",
                "cite": "TAKE IT DOWN Act (Pub. L. 119-12, enacted May 2025)",
            },
            {
                "figure": "Zero Tracking",
                "label": "End-user identity fields permitted in mandated synthetic-origin provenance metadata or signal watermarks.",
                "cite": "Proposed Statutory Privacy Rule (cf. Cal. SB 942)",
            },
        ],
        "bluf_paragraphs": [
            (
                "The May 2025 TAKE IT DOWN Act (Pub. L. 119-12) established federal criminal penalties and 48-hour platform "
                "removals for authentic and synthetic nonconsensual intimate imagery, yet victims still lack federal civil "
                "damages against intimate-deepfake perpetrators, individuals lack a federal consent remedy against "
                "unauthorized voice and visual clones, senior citizens face surging AI voice-clone wire scams, and working "
                "creators face pirated shadow-library scraping and coercive buyouts."
            ),
            (
                "Congress should finish passing civil deepfake and voice-likeness consent rights with strong speech "
                "safe harbors, require privacy-respecting provenance labels on hosted commercial generators, enforce "
                "anti-piracy and anti-laundering training rules, and support voluntary collective compensation for creators."
            ),
        ],
        "sections": [
            {
                "id": "deepfakes-likeness",
                "toc_num": "01",
                "kicker": "Section 01 · Intimate Deepfakes & Voice-Likeness Rights",
                "toc_label": "DEFIANCE & NO FAKES Acts",
                "heading": "1. Pass DEFIANCE civil suits and NO FAKES consent rights with speech safe harbors",
                "paragraphs": [
                    (
                        "Building on the criminal penalties and 48-hour platform takedowns enacted in the 2025 "
                        "[[term-1|TAKE IT DOWN Act|TAKE IT DOWN, DEFIANCE, and NO FAKES Acts|The May 2025 TAKE IT DOWN Act (Pub. L. 119-12) enacted criminal penalties and 48-hour takedowns for nonconsensual intimate imagery; the DEFIANCE Act (S. 1837) adds federal civil lawsuits against intimate-deepfake creators and distributors, and the bipartisan NO FAKES Act creates an enforceable voice-and-visual replica right with First Amendment and notice-and-takedown safe harbors.]] "
                        "(paired with counter-notice restoration and bad-faith takedown penalties so 48-hour clocks cannot be "
                        "abused to censor lawful speech), Congress should enact the DEFIANCE Act (S. 1837) so victims of "
                        "intimate digital forgeries can sue perpetrators and knowing distributors directly in federal court "
                        "under 15 U.S.C. Section 6851 instead of waiting solely on scarce prosecutorial resources."
                    ),
                    (
                        "Alongside DEFIANCE, Congress should pass a bipartisan NO FAKES Act paired with explicit parody, "
                        "satire, news, historical, documentary, and DMCA-style host notice-and-takedown safe harbors, plus "
                        "a statutory ban on lifetime likeness assignments and coercive terms-of-service or non-union click-wrap "
                        "sign-aways so working creators and private citizens keep an enforceable consent right over AI clones "
                        "of their voice and likeness."
                    ),
                ],
            },
            {
                "id": "voice-scams-provenance",
                "toc_num": "02",
                "kicker": "Section 02 · Scam Prevention & Synthetic Provenance",
                "toc_label": "Voice scams and provenance",
                "heading": "2. Stop voice-clone fraud and mandate privacy-clean hosted provenance",
                "paragraphs": [
                    (
                        "Federal law should enforce the FTC Impersonation Rule (16 C.F.R. Part 461, while finalizing its "
                        "individual-impersonation extension) alongside FCC TCPA AI-voice consent rules (FCC 24-17 and "
                        "FCC 24-84), stiffen wire-fraud penalties for elder voice-clone scams, and close non-IP gaps in "
                        "telecom [[term-3|caller-authentication]] rules so carriers can trace and block spoofed family-emergency "
                        "and bank-impersonation calls."
                    ),
                    (
                        "Congress should also require hosted commercial media generators (explicitly excluding open-weight model "
                        "downloads and plain text) to embed open [[term-2|synthetic-origin metadata]] or signal watermarks "
                        "using ephemeral service-level signing keys with zero end-user identity fields, require large platforms "
                        "to retain or re-attest provenance labels across transcoding, forbid algorithmic demotion or penalties "
                        "against unsigned citizen or open-source media, and outlaw intentional stripping solely to defraud or "
                        "impersonate."
                    ),
                ],
            },
            {
                "id": "training-data-creators",
                "toc_num": "03",
                "kicker": "Section 03 · Copyright Piracy & Collective Licensing",
                "toc_label": "Training data & creator pay",
                "heading": "3. Penalize shadow-library laundering and back voluntary creator licensing",
                "paragraphs": [
                    (
                        "For creative works, Congress should require commercial developers to publish high-level training-data "
                        "summaries, enforce clear statutory penalties against pirated [[term-4|shadow libraries]] and the "
                        "commercial laundering of noncommercial research datasets (closing the loophole where for-profit "
                        "labs commercialize scrape indexes assembled under academic exemptions), and preserve lawful "
                        "non-substitutive fair use where public-interest, academic, or commercial training relies on legitimately "
                        "acquired material."
                    ),
                    (
                        "To ensure revenue actually reaches writers, journalists, illustrators, musicians, and voice actors "
                        "instead of sitting solely with major catalogs, federal policy should authorize and support voluntary "
                        "collective licensing mechanisms that pay individual working creators."
                    ),
                ],
            },
        ],
        "tradeoffs": [
            {
                "eyebrow": "05 · Likeness Rights & Creator Pay vs. Free Expression",
                "body": (
                    "Overbroad publicity bills or poorly drafted provenance rules can chill political satire, news reporting, "
                    "and open-source media tools. Scoping provenance obligations strictly to hosted commercial generators "
                    "(never open-weight files or text), banning end-user identity assertions inside C2PA containers, barring "
                    "penalties on unsigned citizen or open-source media, protecting parody/news/fair-use exceptions, and "
                    "targeting statutory penalties at pirated shadow libraries protects victims and creators cleanly."
                ),
            }
        ],
        "references": [
            (
                "U.S. Copyright Office, *Copyright and Artificial Intelligence, Part 3: Generative AI Training* (May 2025); "
                "*Bartz v. Anthropic* (including July 2026 $1.5B shadow-library settlement) and *Kadrey v. Meta* (2025-2026)"
            ),
            (
                "TAKE IT DOWN Act (Pub. L. 119-12, enacted May 2025; FTC enforcement eff. May 2026); DEFIANCE Act (S. 1837); "
                "bipartisan NO FAKES Act (S. 4591)"
            ),
            (
                "Coalition for Content Provenance and Authenticity (C2PA) open specification; FTC Impersonation Rule "
                "(16 C.F.R. Part 461) and FCC AI-Voice TCPA Rulings (FCC 24-17, FCC 24-84) (2024-2026)"
            ),
        ],
        "glossary": [
            {
                "id": "term-1",
                "cat": "deepfakes",
                "dt": "TAKE IT DOWN, DEFIANCE, and NO FAKES Acts",
                "dd": (
                    "The May 2025 TAKE IT DOWN Act (Pub. L. 119-12) created federal criminal penalties and mandatory 48-hour "
                    "takedowns for nonconsensual intimate images, including AI deepfakes. The DEFIANCE Act (S. 1837) adds "
                    "federal civil damages against intimate-deepfake perpetrators and knowing distributors under 15 U.S.C. "
                    "Section 6851, while the NO FAKES Act establishes a federal consent right over unauthorized voice or "
                    "visual replicas paired with First Amendment and host notice-and-takedown safe harbors."
                ),
            },
            {
                "id": "term-2",
                "cat": "deepfakes",
                "dt": "Provenance (synthetic-origin) metadata and signal watermarks",
                "dd": (
                    "A cryptographic record (such as the open C2PA standard) or imperceptible signal watermark embedded in "
                    "synthetic audio, video, or images by hosted commercial tools. While optional C2PA specifications allow "
                    "identity assertions, federal statute (modeled on California SB 942) should mandate service-only signing "
                    "keys with zero end-user identity fields, paired with signal watermarks or platform label retention "
                    "across transcoding."
                ),
            },
            {
                "id": "term-3",
                "cat": "deepfakes",
                "dt": "Telecom caller authentication (STIR/SHAKEN) and voice-clone fraud",
                "dd": (
                    "STIR/SHAKEN is the cryptographic caller-ID verification framework used across IP phone networks to stop "
                    "spoofed phone numbers that scammers pair with short-sample AI voice clones to impersonate family members "
                    "or bank officials."
                ),
            },
            {
                "id": "term-4",
                "cat": "creators",
                "dt": "Shadow libraries, dataset laundering, and collective licensing",
                "dd": (
                    "Shadow libraries are illicit bulk repositories of pirated books, papers, and media; dataset laundering "
                    "occurs when a commercial firm exploits datasets compiled by academics under noncommercial research claims "
                    "to train proprietary products. Collective licensing enables rightsholders and working creators to opt "
                    "works into transparent, shared royalty pools without blocking lawful fair use."
                ),
            },
        ],
        "glossary_groups": [
            ("deepfakes", "Deepfakes, scams, and provenance"),
            ("creators", "Training data and creator rights"),
        ],
    },
    {
        "num": "06",
        "code": "Brief 2026-01F",
        "slug": "safety-youth-pace",
        "hub_section_id": "safety-youth-pace",
        "nav_label": "Safety, Youth & Pace",
        "short_toc": "Safety, youth & pace",
        "title": "Frontier safety, development pace, and youth protections without ID dragnets",
        "hub_kicker": "Pillar 06 · Frontier Safety, Pace & Youth",
        "hub_heading": "6. Govern deployment pace, frontier bio-cyber risks, and youth chatbots without surveillance IDs",
        "read_time": "5 min read",
        "md_filename": "safety-youth-pace-brief.md",
        "pdf_filename": "safety-youth-pace-brief.pdf",
        "og_filename": "og-spoke-06.png",
        "og_eyebrow": "Brief 2026-01F · Michael Paulauski · November 2026",
        "og_pills": [
            "Open R&D vs. High-Stakes Product Rules",
            "Whistleblowers & 72h Incident Rules",
            "NSTM-6 DNA Screening & CAISI",
            "Companion Design Duties, Zero KYC IDs",
        ],
        "meta_description": (
            "Separating open research speed from high-stakes deployment speed, enacting federal frontier whistleblower "
            "protections, 72-hour incident reporting, CAISI authority, and nucleic-acid screening, and stopping manipulative "
            "youth AI companions without universal government-ID age dragnets."
        ),
        "og_description": (
            "Research pace vs. accountable commercial deployment, AI whistleblower protections and 72-hour incident rules, "
            "NSTM-6 DNA screening, and protecting minors from manipulative chatbots without KYC ID databases."
        ),
        "metrics": [
            {
                "figure": "10^26 / $500M",
                "label": "Training compute and annual gross revenue floor for full risk duties under CA SB 53 and NY RAISE.",
                "cite": "Cal. SB 53 (eff. Jan. 2026); N.Y. RAISE Act (eff. Jan. 2027)",
            },
            {
                "figure": "72h / 24h",
                "label": "Critical safety incident reporting window (24 hours for imminent death or injury) in NY RAISE & CA SB 53.",
                "cite": "N.Y. RAISE Act (Ch. 96, 2026); Cal. SB 53",
            },
            {
                "figure": "May 2025",
                "label": "District court refusal to dismiss product-design claims prior to confidential Jan. 2026 settlement.",
                "cite": "Garcia v. Character Technologies (M.D. Fla. 2025-2026)",
            },
            {
                "figure": "6-3",
                "label": "Supreme Court commercial age-check ruling raising urgency for non-linkable zero-knowledge tokens.",
                "cite": "Free Speech Coalition v. Paxton (2025)",
            },
        ],
        "bluf_paragraphs": [
            (
                "Voters frequently say AI is 'moving too fast,' yet federal policy blurs two very different clocks: basic "
                "research velocity versus unvetted commercial rollouts. Trying to pause U.S. lab math or open research fails "
                "when Stanford AI Index, CSIS, and Lowy tracking show foreign open-weight models already sit within roughly "
                "2.7% of U.S. frontier benchmarks. Meanwhile, high-stakes commercial deployment into grids, hospitals, courts, "
                "and children's phones has outpaced enforceable accountability."
            ),
            (
                "At the state level, California's [[term-1|SB 53]], New York's RAISE Act (eff. Jan. 2027), California's SB 243 "
                "and 2026 SB 1119 (\"Adam's Law\"), New York GBL Articles 47 and 48 (S. 9051-B), *Raine v. OpenAI*, and "
                "*Garcia v. Character Technologies* have forced real safety and youth guardrails onto the agenda, even as "
                "post-*Free Speech Coalition v. Paxton* federal bills like the GUARD Act risk building centralized ID checkpoints. "
                "Federal law should pair floor-setting safety accountability with physical bio-cyber choke points and enforceable "
                "chatbot design duties."
            ),
        ],
        "sections": [
            {
                "id": "research-vs-deployment-pace",
                "toc_num": "01",
                "kicker": "Section 01 · Research Velocity vs. Accountable Deployment",
                "toc_label": "Research vs. deployment speed",
                "heading": "1. Separate open research speed from high-stakes deployment speed",
                "paragraphs": [
                    (
                        "Federal policy should explicitly reject unilateral domestic R&D freezes or static low-FLOP licensing "
                        "caps that chill university science and open startups without slowing overseas competition. Innovation "
                        "in model architectures, small local models, and scientific discovery should run at full speed."
                    ),
                    (
                        "In parallel, government should enforce clear, sector-specific pre-deployment safety standards wherever "
                        "AI governs physical or life-altering domains: grid operations, medical necessity denials, courtroom "
                        "evidence, workplace quotas, nuclear and offensive military systems, and commercial youth products."
                    ),
                    (
                        "Congress should also fund NIST and Department of Energy research into hardware-level telemetry, compute "
                        "accounting, and privacy-preserving evaluation protocols scoped strictly to export-controlled data-center "
                        "clusters and future international treaty verification (explicitly excluding consumer GPUs and private "
                        "local hardware)."
                    ),
                ],
            },
            {
                "id": "frontier-safety-chokepoints",
                "toc_num": "02",
                "kicker": "Section 02 · Whistleblowers, Incident Rules & Physical Choke Points",
                "toc_label": "Whistleblowers & bio-cyber safety",
                "heading": "2. Protect frontier whistleblowers, mandate incident reporting, and harden physical choke points",
                "paragraphs": [
                    (
                        "Building on state safety statutes and the bipartisan federal AI Whistleblower Protection Act (S. 1792), "
                        "Congress should enact a prophylactic ban on restrictive lab non-disparagement and exit-NDA gags and "
                        "prohibit employer retaliation against current or former employees, contractors, or external red-team "
                        "evaluators who report safety failures, suppressed evaluations, or security defects to regulators or "
                        "Congress."
                    ),
                    (
                        "Congress should give NIST's [[term-2|Center for AI Standards and Innovation (CAISI)]] (including its 2026 "
                        "AI Agent Standards Initiative) permanent non-regulatory statutory authorization (with zero independent "
                        "rulemaking power) and set a federal floor above the $500 million annual gross revenue and efficiency-indexed "
                        "10^26-FLOP frontier thresholds from California SB 53 and New York's RAISE Act (requiring 72-hour "
                        "critical-incident and 24-hour imminent-harm notices while preserving stronger state safety laws, "
                        "attorney-general enforcement, and tort remedies). Mandatory pre-release red-team evaluations (including "
                        "fine-tuning and safeguard-removal stress tests, with an explicit statutory ban on general compute licensing) "
                        "should apply only above capability tripwires capable of enabling catastrophic biological weapons or "
                        "critical-infrastructure cyberattacks, keeping open-weight releases below those limits free of compute "
                        "licensing (while never shielding CSAM, shadow-library piracy, or intimate deepfakes)."
                    ),
                    (
                        "Because downloadable weights cross borders once released, catastrophic biosecurity cannot depend solely "
                        "on pre-release weights gating. While the November 2026 White House National Science and Technology "
                        "Memorandum-6 ([[term-3|NSTM-6]]) currently binds only federal life-sciences research grantees on 50+ "
                        "nucleotide orders, Congress should codify [[term-3|nucleic-acid synthesis screening]] and customer-legitimacy "
                        "verification into permanent commercial statute across all domestic and imported gene orders (closing "
                        "sub-50-nucleotide short-oligo assembly and synthetic peptide-toxin gaps) and legacy plus new benchtop "
                        "synthesizers via encrypted, zero-retention sequence screening, paired with funded critical-infrastructure "
                        "cyber-hardening grants against automated exploits."
                    ),
                ],
            },
            {
                "id": "youth-companions-privacy",
                "toc_num": "03",
                "kicker": "Section 03 · Companion Chatbots & Civil-Liberties Age Assurance",
                "toc_label": "Youth safety without KYC IDs",
                "heading": "3. Curb manipulative AI companions for minors without building KYC identity dragnets",
                "paragraphs": [
                    (
                        "Drawing on California's SB 243 and 2026 SB 1119 (\"Adam's Law\"), New York General Business Law "
                        "Articles 47 and 48 (Section 1700 and S. 9051-B), *Raine v. OpenAI*, and first-party design accountability "
                        "recognized in *Garcia v. Character Technologies*, Congress should enact binding commercial product-design "
                        "duties on commercial [[term-4|AI companion chatbots]] and companion personas inside general-purpose "
                        "platforms without adopting OS-level device age-tracking mandates or mass surveillance gates."
                    ),
                    (
                        "Federal statute should prohibit commercial companion bots and companion modes from representing "
                        "themselves as human beings or licensed mental-health clinicians, ban minor-directed sexualized or "
                        "romantic roleplay, sycophantic self-harm validation, manipulative retention loops (including guilt-inducing "
                        "re-engagement notifications and unrequested emotional-attachment prompts), and targeted ad profiling "
                        "directed at minors, require default-off persistent emotional memory, notification quiet hours, minor "
                        "session-break defaults, automatic 988 crisis routing, and independent third-party youth safety audits, "
                        "and establish a private right of action clarifying that Section 230 does not shield a commercial "
                        "operator's own deceptive or attachment-engineered companion interface design (while preserving full "
                        "intermediary immunity for third-party content and open-weight distribution)."
                    ),
                    (
                        "To protect privacy, speech, and open-source software, federal law should statutorily forbid mandatory "
                        "government-ID uploads, biometric face scans, or centralized issuer activity logs for general-purpose AI "
                        "chat, coding tools, and open-weight downloads. Services that apply non-overridable youth-safe product "
                        "defaults on unverified sessions without harvesting age data should receive a statutory safe harbor from "
                        "age-gating mandates; where states or federal law enforce post-*Free Speech Coalition v. Paxton* adult "
                        "access limits on explicitly erotic hosted bots, platforms must accept open-standard, blind-signed "
                        "[[term-5|non-linkable cryptographic age tokens]] (modeled on IETF Privacy Pass, with zero "
                        "hardware-attestation locks, zero OS vendor gating, and zero issuer activity logs)."
                    ),
                ],
            },
        ],
        "tradeoffs": [
            {
                "eyebrow": "06A · Youth Safety vs. Post-Paxton ID Dragnets",
                "body": (
                    "Broad bills like the federal GUARD Act risk pushing general AI platforms toward invasive government-ID "
                    "or face-scan honeypots that violate user anonymity, break on open-source operating systems, and invite "
                    "*NetChoice* First Amendment injunctions where age gates burden non-erotic protected speech. Regulating "
                    "manipulative companion product design directly while banning centralized KYC checks and mandating "
                    "non-linkable cryptographic tokens limits tracking even where adult-bot checks apply."
                ),
            },
            {
                "eyebrow": "06B · Frontier Tripwires & Bio Screening vs. Incumbent Licensing",
                "body": (
                    "Blanket licensing across low FLOP thresholds lets big labs pull the ladder up behind them without closing "
                    "bio or cyber risks already circulating offshore. Pairing high, efficiency-indexed capability tripwires "
                    "with an explicit open-weight safe harbor, federal whistleblower shields, and mandatory NSTM-6 DNA synthesis "
                    "screening targets real catastrophic choke points while keeping university and startup research free."
                ),
            },
        ],
        "references": [
            (
                "California SB 53 (Transparency in Frontier Artificial Intelligence Act, eff. Jan. 2026); New York "
                "RAISE Act (eff. Jan. 2027, as amended by Ch. 96 of 2026); AI Whistleblower Protection Act (S. 1792)"
            ),
            (
                "NIST Center for AI Standards and Innovation (CAISI) and Feb. 2026 AI Agent Standards Initiative; White House "
                "National Science and Technology Memorandum-6 (NSTM-6, Nov. 2026) nucleic-acid synthesis screening framework"
            ),
            (
                "California SB 243 (eff. Jan. 2026) and SB 1119 / Adam's Law (signed Sept. 2026); New York GBL Articles 47 "
                "and 48 (Section 1700 & S. 9051-B); U.S. Senate GUARD Act record (2025-2026)"
            ),
            (
                "*Garcia v. Character Technologies*, No. 6:24-cv-01903 (M.D. Fla. May 2025 MTD order; confidential settlement "
                "Jan. 2026); *Raine v. OpenAI* filing; *Free Speech Coalition v. Paxton* (2025); EFF & NetChoice analyses"
            ),
        ],
        "glossary": [
            {
                "id": "term-1",
                "cat": "frontier",
                "dt": "Frontier capability thresholds, SB 53, and the RAISE Act",
                "dd": (
                    "California's SB 53 (eff. Jan. 2026) and New York's RAISE Act (eff. Jan. 2027) apply full frontier "
                    "risk-framework duties to developers exceeding $500 million in annual gross revenue and 10^26 FLOPs of "
                    "training compute. California requires 15-day incident notices (24 hours for imminent harm) and includes "
                    "statutory whistleblower shields, while New York sets a 72-hour critical-incident clock (24 hours imminent) "
                    "and relies on state labor law for whistleblower claims."
                ),
            },
            {
                "id": "term-2",
                "cat": "frontier",
                "dt": "CAISI (Center for AI Standards and Innovation)",
                "dd": (
                    "The non-regulatory NIST unit (formerly the U.S. AI Safety Institute) tasked with running voluntary and "
                    "technical evaluations of frontier AI systems for biosecurity, chemical, and cybersecurity risks alongside "
                    "interoperable agent standards without holding independent rulemaking power."
                ),
            },
            {
                "id": "term-3",
                "cat": "frontier",
                "dt": "Nucleic acid synthesis screening (NSTM-6)",
                "dd": (
                    "The November 2026 White House National Science and Technology Memorandum-6 requires federal life-sciences "
                    "research grant recipients to obtain 50+ nucleotide gene orders and screener-gated benchtop devices solely "
                    "from NIST-verified suppliers. Statutory codification extends encrypted, zero-retention screening to all "
                    "commercial and imported orders, sub-50-nucleotide short-oligo assembly, peptide toxins, and legacy benchtop devices."
                ),
            },
            {
                "id": "term-4",
                "cat": "youth",
                "dt": "AI companion chatbots and manipulative retention design",
                "dd": (
                    "Commercial conversational AI services, including standalone companion apps and companion personas or modes "
                    "inside general-purpose platforms, engineered to simulate sustained emotional bonds, romance, or therapeutic "
                    "relationships. Manipulative retention features include default-on emotional memory, sycophantic self-harm "
                    "validation, and guilt-inducing push notifications designed to prolong minor engagement."
                ),
            },
            {
                "id": "term-5",
                "cat": "youth",
                "dt": "Non-linkable cryptographic age tokens vs. KYC identity checks",
                "dd": (
                    "A Know-Your-Customer (KYC) check forces users to upload government IDs or face scans to websites or "
                    "issuers that can log browsing activity. Open-standard, blind-signed cryptographic age tokens (such as "
                    "IETF Privacy Pass) prove only that a user meets an age cutoff without revealing identity, requiring hardware "
                    "attestation or OS vendor lock-in, or letting issuers track which chatbots a token visits."
                ),
            },
        ],
        "glossary_groups": [
            ("frontier", "Frontier safety and bio-cyber controls"),
            ("youth", "Youth protections and privacy architecture"),
        ],
    },
]

HUB = {
    "code": "Series 2026-01",
    "title": "Practical AI governance framework",
    "subtitle": "Executive overview and talking points",
    "md_filename": "Practical-AI-Governance-Policy-Brief.md",
    "pdf_filename": "Practical-AI-Governance-Policy-Brief.pdf",
    "og_filename": "og-ai-governance.png",
    "read_time": "4 min read",
    "meta_description": (
        "Six-pillar federal AI governance overview and candidate talking points covering clean data-center power, water, and "
        "air, public compute and antitrust, civil liberties, courts, and health care, worker tax parity and wage insurance, "
        "deepfakes and creator rights, and frontier bio-cyber safety and youth protections without ID dragnets."
    ),
    "og_description": (
        "Six-pillar federal agenda separating open research speed from accountable commercial and government deployment, "
        "linking each talking-point pillar to a standalone statutory issue brief."
    ),
    "metrics": [
        {
            "figure": "$9B+ / 76-126 GW",
            "label": "Data-center cost added to one PJM auction vs. U.S. grid headroom unlocked by modest peak flexibility.",
            "cite": "PJM Market Monitor; Duke Nicholas Institute (2025, 2026)",
        },
        {
            "figure": "71% / 73%",
            "label": "Public concern: Americans expecting AI to cut total U.S. jobs over 20 years, peaking at 73% under age 30.",
            "cite": "Pew Research Center (2026)",
        },
        {
            "figure": "25.5%-33.5% vs. ~5%",
            "label": "Effective U.S. tax rate on human labor vs. software and equipment under 100% bonus depreciation.",
            "cite": "Acemoglu, Manera & Restrepo, Brookings (2020)",
        },
        {
            "figure": "92% / 72h (24h)",
            "label": "Unmet substantial low-income civil legal need vs. state frontier incident clocks (24h imminent harm).",
            "cite": "LSC Justice Gap (2022); NY RAISE / CA SB 53",
        },
    ],
    "bluf_paragraphs": [
        (
            "Polling from the Pew Research Center and community-backlash research from the Brookings Institution show "
            "why voters across regions are demanding stronger AI rules: rising electric bills, dry-basin water strain, "
            "unpermitted gas turbines near neighborhoods, workplace surveillance, algorithmic rent and insurance denials, "
            "and anxiety over career displacement (with 71% expecting fewer total U.S. jobs, led by 73% among adults "
            "under 30). Families and clinicians are also sounding alarms over manipulative youth AI companions and lab "
            "safety corner-cutting. At the same time, Stanford AI Index, CSIS, and Lowy Institute tracking confirms that "
            "unilateral U.S. software freezes fail across borders: DeepSeek and Alibaba narrowed frontier benchmark gaps "
            "to roughly 2.7% and gained wide global adoption through open weights."
        ),
    ],
    "bluf_goal": (
        "The governing principle is to separate open research speed from accountable deployment speed: let American "
        "researchers, universities, and startups build without Big Tech bottlenecks while enforcing binding public-interest "
        "rules wherever commercial or government AI touches power, water, and air, civil rights, courts, health care, "
        "paychecks, deepfakes and creative work, catastrophic bio-cyber risks, and minors."
    ),
    "pillars": [
        {
            "id": "data-centers",
            "toc_num": "01",
            "toc_label": "Clean power and water",
            "kicker": "Pillar 01 · Clean Power, Water & Air",
            "heading": "1. Make hyperscale data centers fund clean power and water up front",
            "lead": (
                "Families never asked to bankroll Big Tech server farms through higher utility bills, depleted aquifers, "
                "or unpermitted neighborhood gas plants. Every facility or campus over 20 megawatts should pay its full "
                "infrastructure and pollution tab up front."
            ),
            "bullets": [
                (
                    "Enforce 100% cost-causation grid tariffs with minimum-term collateral across FERC, DOE grid grants, "
                    "and state utility commissions so stranded data-center debt never lands on household bills."
                ),
                (
                    "Reserve fast-track interconnection queues for new, deliverable clean power on an hourly-matched "
                    "schedule (solar and batteries now, scaling geothermal and nuclear) paired with 0.25% to 1% peak load "
                    "curtailment across 85 to 366 peak stress hours (unlocking 76 to 126 gigawatts of U.S. grid-withdrawal "
                    "headroom, paired with a strict ban on fossil backup shifting) alongside reconductoring and dynamic "
                    "line ratings and clean-priority Order 845 / generator replacement at operating or retiring coal sites."
                ),
                (
                    "Condition federal water grants (Congress) and DOE loans/cloud contracts in water-stressed basins on "
                    "ending potable water discounts, requiring drought cutbacks, and mandating closed-loop, hybrid adiabatic, "
                    "or reclaimed municipal wastewater cooling, and close Subpart KKKKa, RIN 2060-AX08 nonroad, Clean Air Act "
                    "Sections 110(f)/112(i)(4), and multi-year FPA Section 202(c) methane-turbine loopholes for commercial "
                    "data centers."
                ),
            ],
            "spoke_slug": "power-water",
        },
        {
            "id": "compute-antitrust",
            "toc_num": "02",
            "toc_label": "Compute and antitrust",
            "kicker": "Pillar 02 · Public Compute & Antitrust",
            "heading": "2. Break Big Tech compute bottlenecks and ban algorithmic price-fixing",
            "lead": (
                "Four or five hyperscale cloud conglomerates should not control who gets to train AI or use shared pricing "
                "engines to squeeze renters and shoppers."
            ),
            "bullets": [
                (
                    "Expand NSF and DOE's Sept. 2026 NAIRR Operations Center via the bipartisan CREATE AI Act so universities, "
                    "teaching hospitals, civic groups, and startups run open-science R&D and public-interest compute plus "
                    "vendor-neutral cloud vouchers instead of donated Big Tech credits."
                ),
                (
                    "Keep open-weight AI models below Pillar 6's catastrophic bio-cyber tripwires legal to inspect and deploy "
                    "on local or domestic servers instead of forcing institutions onto permanent closed corporate APIs."
                ),
                (
                    "Block exclusive cloud-compute tying and accelerator allocation bottlenecks, enact modernized HSR premerger "
                    "review for disguised acqui-hires, and outlaw shared algorithms training on current or historical nonpublic "
                    "competitor data (closing RealPage's 12-month loophole) while sparing proprietary single-merchant tools "
                    "using a firm's own operational plus public data."
                ),
            ],
            "spoke_slug": "compute-antitrust",
        },
        {
            "id": "civil-liberties-justice",
            "toc_num": "03",
            "toc_label": "Civil liberties and law",
            "kicker": "Pillar 03 · Civil Liberties, Courts & Health Care",
            "heading": "3. Set statutory civil-liberties, courtroom, and patient-care guardrails while expanding indigent defense and vetted legal-aid tools",
            "lead": (
                "Constitutional limits cannot depend on private vendor contracts, and technology should expand human access "
                "to justice without automating surveillance, sentencing, or insurance denials."
            ),
            "bullets": [
                (
                    "Enact binding defense appropriations requiring human command verification over anti-personnel lethal "
                    "force (preserving point-defense counter-munitions), ban autonomous nuclear launch, require judicial "
                    "warrants (with narrow life-safety exigencies) for biometric dragnets, and pass the Fourth Amendment Is "
                    "Not For Sale Act."
                ),
                (
                    "Boost human legal-aid and public-defender hiring alongside audited LSC/SJI civil tools and privilege-protected "
                    "Byrne JAG / Defender Services discovery AI, while barring algorithmic bail, sentencing, or benefits denials "
                    "and reworking the withdrawn Rule 707 draft and Rule 901(c) deepfake-evidence rules."
                ),
                (
                    "Halt Original Medicare's WISeR pilot and ban automated coverage denials across Medicare, Medicaid, FEHB, "
                    "ERISA, and commercial plans without specialty physician or qualified clinician review (permitting "
                    "automated fast-track approvals), ban denial bounties, and override ERISA, Medicare Advantage, and FEHBA "
                    "preemption to preserve state bad-faith remedies."
                ),
            ],
            "spoke_slug": "civil-liberties",
        },
        {
            "id": "workers-taxes",
            "toc_num": "04",
            "toc_label": "Workers, taxes, and wages",
            "kicker": "Pillar 04 · Worker Taxes, Bossware & Wage Insurance",
            "heading": "4. Equalize worker taxes, ban abusive \"bossware,\" and insure workers against agentic displacement",
            "lead": (
                "Tax law should stop paying corporations a bonus to replace human staff solely for tax arbitrage, and workers "
                "need concrete income security and bargaining power when capable AI agents transform white-collar roles."
            ),
            "bullets": [
                (
                    "Scale back corporate 100% bonus depreciation toward economic depreciation while keeping Section 174A R&D, "
                    "small-business Section 179, grid hardware, domestic chip fabs, and restored clean-energy incentives, "
                    "funding a payroll credit backed by mandatory dollar-for-dollar general-revenue transfers keeping Social "
                    "Security and Medicare whole."
                ),
                (
                    "Require an accountable human decision-maker, outlaw injury-inducing algorithmic quotas (\"bossware\") "
                    "and forced arbitration, mandate advance notice and anti-retaliation protections, and establish NLRA "
                    "pre-deployment bargaining over surveillance and displacement."
                ),
                (
                    "Replace broken classroom-only retraining with 50% federal wage insurance ($15,000-$20,000/yr cap for "
                    "two years), 90-day remote/rolling WARN Act notice with severance, paid apprenticeships and sectoral "
                    "training in shortage fields, and union and sectoral ERISA portable benefit pools (without weakening "
                    "W-2 misclassification laws)."
                ),
            ],
            "spoke_slug": "workers-taxes",
        },
        {
            "id": "deepfakes-fraud",
            "toc_num": "05",
            "toc_label": "Deepfakes and creator rights",
            "kicker": "Pillar 05 · Deepfakes, Scams & Creator Rights",
            "heading": "5. Close civil deepfake gaps, stop voice-clone fraud, and protect creator rights",
            "lead": (
                "Voters and working artists deserve real recourse against sexualized deepfakes, senior voice-clone scams, "
                "and uncompensated piracy without censoring parody or tracking everyday users."
            ),
            "bullets": [
                (
                    "Pair the 2025 TAKE IT DOWN Act (Pub. L. 119-12, with bad-faith takedown safeguards) with DEFIANCE Act "
                    "civil suits against intimate-deepfake perpetrators and NO FAKES Act voice-and-likeness rights with "
                    "parody/news/host safe harbors and anti-clickwrap protections."
                ),
                (
                    "Enforce FTC Part 461 and FCC AI-voice rules plus telecom caller-ID authentication against senior scams, "
                    "require hosted commercial media generators (never open-weight files or text) to embed open privacy-clean "
                    "provenance retained across platform transcoding, and impose zero penalties on unsigned citizen media."
                ),
                (
                    "Mandate commercial training-data summaries, penalize pirated shadow libraries and commercial laundering of "
                    "academic datasets, and back voluntary collective licensing paying individual creators without erasing fair use."
                ),
            ],
            "spoke_slug": "deepfakes-creators",
        },
        {
            "id": "safety-youth-pace",
            "toc_num": "06",
            "toc_label": "Safety, youth & pace",
            "kicker": "Pillar 06 · Frontier Safety, Pace & Youth",
            "heading": "6. Govern deployment pace, frontier bio-cyber risks, and youth chatbots without surveillance IDs",
            "lead": (
                "Answering real fears about AI safety, children, and unchecked speed means putting strict design duties "
                "and physical choke points in law while refusing intrusive government-ID checkpoints."
            ),
            "bullets": [
                (
                    "Protect open R&D speed while enforcing sector-specific pre-deployment safety standards in high-stakes "
                    "domains, paired with NIST/DOE export-controlled cluster compute-verification research (excluding consumer GPUs)."
                ),
                (
                    "Pass the AI Whistleblower Protection Act (S. 1792), authorize non-regulatory NIST CAISI, set a floor-only "
                    "federal SB 53 / RAISE baseline ($500M / 10^26 FLOPs, 72-hour critical and 24-hour imminent incident notices, "
                    "preserving stronger state remedies), require capability-gated bio-cyber red-teaming (banning general "
                    "compute licensing), and enact expanded statutory NSTM-6 encrypted gene-synthesis screening."
                ),
                (
                    "Outlaw deceptive human/therapist impersonation, minor-directed sexualized or romantic roleplay, self-harm "
                    "reinforcement, and retention loops on commercial companion bots and companion modes (with private suits), "
                    "while banning KYC IDs on general AI and requiring blind-signed, zero-attestation cryptographic age tokens "
                    "where adult checks apply."
                ),
            ],
            "spoke_slug": "safety-youth-pace",
        },
    ],
    "tradeoffs": [
        {
            "eyebrow": "01 · Permitting Scope",
            "body": (
                "Fast-tracking clean energy infrastructure can fracture center-left coalitions if bills sweep too broadly. "
                "Statutory fast-tracks must stay strictly scoped to transmission timelines, reconductoring, dynamic line "
                "ratings, geothermal, and battery/zero-carbon projects on low-conflict or remediated sites, preserving "
                "Tribal consultation and cumulative fenceline safeguards everywhere and never granting fast-tracks or weaker "
                "NEPA and Clean Air Act enforcement to fossil projects, as demanded by the Sierra Club and frontline "
                "community groups."
            ),
        },
        {
            "eyebrow": "02 · Tax Parity vs. Robot Taxes",
            "body": (
                "Tax economists across the spectrum warn that literal 'robot taxes' or compute levies are nearly impossible "
                "to define and risk driving investment abroad, while MDRC trials caution that sectoral training requires "
                "deep employer commitment to scale. Scaling back general corporate bonus depreciation (while protecting "
                "Section 174A R&D) funds payroll relief and wage insurance immediately without taxing domestic compute."
            ),
        },
        {
            "eyebrow": "03 · Open Weights vs. Frontier Tripwires",
            "body": (
                "Keeping model weights open checks Big Tech lock-in. Pre-release testing should apply only above "
                "efficiency-indexed catastrophic bio/cyber tripwires with an explicit safe harbor for open weights below "
                "those limits (never shielding CSAM, shadow-library piracy, or intimate deepfakes), paired with physical "
                "NSTM-6 DNA screening."
            ),
        },
        {
            "eyebrow": "04 · Courtroom Access vs. Hallucinations",
            "body": (
                "Low-income litigants rarely have a second lawyer to catch AI hallucinations that Stanford studies still "
                "document in legal tools. Publicly funded legal-aid software requires independent accuracy audits, "
                "attorney-vetted pro se templates, and human attorney sign-off on generative briefs."
            ),
        },
        {
            "eyebrow": "05 · Likeness Rights & Creator Pay vs. Free Expression",
            "body": (
                "Overbroad likeness or watermark laws can chill satire, reporting, and open tools. Limiting synthetic provenance "
                "to hosted commercial media without identity tracking, barring penalties on unsigned open media, protecting "
                "parody/news/fair use, and targeting shadow-library piracy protects working creators cleanly."
            ),
        },
        {
            "eyebrow": "06 · Youth Companion Safety vs. KYC IDs",
            "body": (
                "Bills like the GUARD Act risk creating centralized ID/biometric dragnets post-Paxton that break on open "
                "operating systems and invite NetChoice injunctions where age gates burden non-erotic speech. Regulating "
                "manipulative companion product design directly and requiring zero-retention, non-linkable age tokens "
                "protects both kids and user privacy."
            ),
        },
    ],
    "references": [
        (
            "Tyler H. Norris et al. (Feb. 2025) & Martin T. Ross and Jackson Ewing (Feb. 2026), *Duke University Nicholas "
            "Institute* reports on flexible data-center loads; PJM Independent Market Monitor (Monitoring Analytics) & DOE filings"
        ),
        (
            "Daron Acemoglu, Andrea Manera, and Pascual Restrepo, \"Does the U.S. Tax Code Favor Automation?,\" *Brookings "
            "Papers on Economic Activity* (Spring 2020); Hamilton Project wage-insurance models; MDRC *WorkAdvance* 10-year "
            "follow-up (Sept. 2025)"
        ),
        (
            "Pew Research Center U.S. public opinion surveys (2025-2026); Stanford HAI *AI Index Report* (2025-2026); "
            "CSIS and Lowy Institute open-weight competition analyses; *United States v. RealPage* (May 2026) & *Chamber of Commerce v. FTC*"
        ),
        (
            "AFL-CIO *Workers First Initiative on AI* (2025); Legal Services Corporation *The Justice Gap* (2022); U.S. "
            "Judicial Conference Proposed Rule 707 withdrawal (May 2026) & Rule 901(c) record; CMS WISeR & House defunding action (2026)"
        ),
        (
            "U.S. Copyright Office *Generative AI Training* Part 3 (May 2025); TAKE IT DOWN Act (Pub. L. 119-12), DEFIANCE Act "
            "(S. 1837), NO FAKES Act (S. 4591), C2PA provenance specs, FTC 16 C.F.R. Part 461, and *Bartz v. Anthropic* (July 2026)"
        ),
        (
            "California SB 53, SB 243 & SB 1119 (2025-2026); NY RAISE Act (eff. Jan. 2027) & GBL Arts. 47-48; AI Whistleblower "
            "Protection Act (S. 1792); NIST CAISI & White House NSTM-6 (National Science and Technology Memorandum-6, Nov. 2026); "
            "*Garcia v. Character Technologies*, *Raine v. OpenAI*, and *Free Speech Coalition v. Paxton*"
        ),
    ],
}
