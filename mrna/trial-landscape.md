# Starter mRNA Cancer Trial And Evidence Landscape

Status: starter map
Last updated: 2026-06-14

Audience label: trial landscape review, patient question preparation, research intelligence, not for clinical use.

This page starts the trial map for mRNA cancer vaccines and therapeutics. It is incomplete by design and should be expanded into source cards and disease-specific pages.

## Current Evidence Tiers

| Tier | Meaning | Current examples |
| --- | --- | --- |
| Strongest current clinical signal | Randomized human trial with recurrence/survival endpoint signal, still investigational | mRNA-4157/V940 plus pembrolizumab in resected high-risk melanoma |
| Important early human immune signal | Small trial showing immune response and possible clinical association | Autogene cevumeran in resected pancreatic ductal adenocarcinoma |
| Trial-in-progress frontier | Phase 2/3 or phase 3 studies testing whether the signal holds | INTerpath melanoma, NSCLC, bladder, renal cell, pancreatic phase 2 |
| Platform promise | Delivery and immunology appear plausible, but product-specific clinical benefit is unproven | LNP, lipoplex, dendritic-cell targeting, in situ mRNA immunotherapy |
| Preclinical/speculative | Cell/animal or design-stage evidence | many payload, adjuvant, cytokine, and combination concepts |

## Starter Trial Map

| Product / platform | Cancer type | Strategy | Trial / source | Current reading | Safety note |
| --- | --- | --- | --- | --- | --- |
| mRNA-4157 / V940 / intismeran autogene + pembrolizumab | Resected high-risk melanoma | Personalized neoantigen mRNA therapy plus PD-1 blockade | KEYNOTE-942, NCT03897881; phase 3 NCT05933577 | Best current randomized signal; phase 3 needed for practice-changing certainty | Investigational; adverse events and immune toxicity require oncology monitoring |
| Autogene cevumeran + atezolizumab + mFOLFIRINOX | Resected pancreatic ductal adenocarcinoma | Individualized mRNA-lipoplex neoantigen vaccine plus checkpoint and chemotherapy | Nature follow-up; phase 2 NCT05968326 | Small but important durable T-cell signal; not definitive | Complex combination; manufacturing and timing constraints matter |
| mRNA-4157 / V940 + pembrolizumab | Non-small cell lung cancer | Personalized neoantigen therapy in adjuvant/neoadjuvant combinations | INTerpath program, NCT06077760 and related trials | Trial-in-progress frontier | Do not infer melanoma results automatically apply to NSCLC |
| mRNA-4157 / V940 + pembrolizumab | Bladder/urothelial cancers | Personalized neoantigen therapy in adjuvant settings | INTerpath studies, e.g. NCT06305767 | Trial-in-progress frontier | Endpoint and recurrence setting matter |
| mRNA-4157 / V940 + pembrolizumab | Renal cell carcinoma | Personalized neoantigen therapy after definitive therapy | INTerpath study, e.g. NCT06307431 | Trial-in-progress frontier | RCC immune biology differs from melanoma |
| Autogene cevumeran | Colorectal cancer and melanoma | Individualized mRNA-lipoplex vaccine | BioNTech/Genentech program reports and trial records | Trial-in-progress frontier | Need peer-reviewed disease-specific outcome data |
| BNT111 + cemiplimab | Anti-PD-(L)1 relapsed/refractory advanced melanoma | Shared tumor-associated antigen mRNA-lipoplex vaccine plus PD-1 blockade | NCT04526899; BioNTech 2024 topline report; foundational FixVac report | Important shared-antigen signal, but company-reported phase 2 details need peer-reviewed publication | Historical-control interpretation and checkpoint-combination toxicity require caution |

## Source Cards Started

- `sources/mrna/keynote-942-mrna-4157-v940-melanoma.md`
- `sources/mrna/autogene-cevumeran-solid-tumors-and-pdac.md`
- `sources/mrna/bnt111-fixvac-shared-antigen-melanoma.md`
- `sources/mrna/lnp-and-mrna-cancer-vaccine-delivery-reviews.md`

## What To Track For Every Trial

- NCT identifier
- Sponsor and collaborators
- Cancer type, stage, and disease setting
- Personalized or off-the-shelf
- Antigen/payload category
- Delivery system and route
- Combination therapy
- Primary endpoint
- Secondary endpoints
- Manufacturing success rate and timeline, if available
- Immune response assay
- Toxicity and discontinuation
- Enrollment status and geography
- Publication status: peer-reviewed, conference abstract, company release, registry only

## Early Interpretation

Melanoma is the anchor because there is a randomized phase 2b trial with recurrence-free survival signal and active phase 3 testing. Pancreatic cancer is the mechanistic frontier because small studies suggest durable T-cell responses may be possible even in a hard-to-immunize tumor, but that evidence is still early.

The next frontier question is not "can mRNA make a target?" It is:

- Can the right target be found?
- Can it be manufactured in time?
- Can the immune system see it?
- Can T cells reach and function in the tumor environment?
- Can the tumor escape?
- Does the immune response translate into longer survival or less recurrence?

## Follow-Up Crawl Targets

- NCT05933577, NCT06077760, NCT06295809, NCT06307431, NCT06305767, NCT05968326, NCT04486378.
- Peer-reviewed updates after company or conference announcements.
- Failed or discontinued mRNA cancer vaccine programs.
- Shared-antigen mRNA vaccines, including tumor-associated antigen approaches.
- Delivery comparisons: LNP versus lipoplex versus dendritic-cell loading.
