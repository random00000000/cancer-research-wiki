# Cancer Research Wiki

Languages: [English](README.md) | [Español](i18n/README.es.md) | [Deutsch](i18n/README.de.md) | [中文](i18n/README.zh.md) | [Русский](i18n/README.ru.md) | [Français](i18n/README.fr.md) | [Português](i18n/README.pt.md) | [العربية](i18n/README.ar.md) | [हिन्दी](i18n/README.hi.md) | [日本語](i18n/README.ja.md) | [한국어](i18n/README.ko.md) | [Italiano](i18n/README.it.md) | [Türkçe](i18n/README.tr.md) | [Bahasa Indonesia](i18n/README.id.md) | [Tiếng Việt](i18n/README.vi.md) | [More languages](i18n/README.md)

Cancer Research Wiki is an automated, evidence-first research wiki with a long-term intent: help move cancer research, prevention literacy, and therapeutic reasoning toward eradication by focusing on root mechanisms, not only symptoms.

This repository is meant to become a structured memory for cancer research agents. Over time, a new thread inside this repo should feel less like searching a pile of links and more like talking to a careful cancer specialist: mechanistic, visual, source-grounded, honest about uncertainty, and clear about when a licensed clinician must be involved.

## Main Goals

### 1. Public Cancer Literacy Infographic

The first major milestone is a large initial research pass that becomes one highly visual infographic for everyday humans.

The infographic should explain:

- What cancer is.
- How normal cells can become cancerous.
- How cancer keeps growing and evades normal controls.
- How cancer can spread.
- Which risk factors are evidence-backed.
- Which prevention, screening, and vaccination steps reduce risk at the population level.
- What individuals cannot fully control.
- When to talk to a medical professional.

Infographic status: first-pass SVG generated from the initial source set. Future versions can add richer generated artwork after more research review.

Current first-pass infographic:

![Cancer: how cells break the body's rules](visuals/cancer-literacy-infographic.svg)

Companion mechanism visual:

![How cancer keeps adapting](visuals/cancer-keeps-adapting.svg)

Screening and vaccination decision visual:

![Cancer screening and vaccination decision guide](visuals/screening-vaccination-decision.svg)

Localized companion mechanism variants:

- [Spanish companion SVG](visuals/cancer-keeps-adapting.es.svg)
- [German companion SVG](visuals/cancer-keeps-adapting.de.svg)
- [Mandarin Chinese companion SVG](visuals/cancer-keeps-adapting.zh.svg)
- [Russian companion SVG](visuals/cancer-keeps-adapting.ru.svg)

Localized infographic variants:

- [Spanish SVG](visuals/cancer-literacy-infographic.es.svg)
- [German SVG](visuals/cancer-literacy-infographic.de.svg)
- [Mandarin Chinese SVG](visuals/cancer-literacy-infographic.zh.svg)
- [Russian SVG](visuals/cancer-literacy-infographic.ru.svg)
- [French SVG](visuals/cancer-literacy-infographic.fr.svg)
- [Portuguese SVG](visuals/cancer-literacy-infographic.pt.svg)
- [Arabic SVG](visuals/cancer-literacy-infographic.ar.svg)
- [Hindi SVG](visuals/cancer-literacy-infographic.hi.svg)
- [Japanese SVG](visuals/cancer-literacy-infographic.ja.svg)
- [Korean SVG](visuals/cancer-literacy-infographic.ko.svg)
- [Italian SVG](visuals/cancer-literacy-infographic.it.svg)
- [Turkish SVG](visuals/cancer-literacy-infographic.tr.svg)
- [Indonesian SVG](visuals/cancer-literacy-infographic.id.svg)
- [Vietnamese SVG](visuals/cancer-literacy-infographic.vi.svg)
- [Translated captions and alt text](i18n/INFOGRAPHIC_CAPTIONS.md)

Research backing:

- [Non-official source strategy](sources/non-official-source-strategy.md)
- [Claim evaluation framework](sources/claim-evaluation-framework.md)
- [Goal 1 source cards](sources/goal-1-public-cancer-literacy.md)
- [Risk reduction levers](prevention/goal-1-risk-reduction-levers.md)
- [Alcohol and cancer evidence](prevention/alcohol-and-cancer-evidence.md)
- [Alcohol, ALDH2, tobacco, and upper aerodigestive cancer](prevention/alcohol-aldh2-tobacco-upper-aerodigestive-evidence.md)
- [Goal 1 effect-size evidence](prevention/effect-size-evidence.md)
- [Risk communication guide](prevention/risk-communication.md)
- [Non-screening absolute risk examples](prevention/non-screening-absolute-risk-examples.md)
- [Environmental and occupational exposure evidence](prevention/environmental-exposure-evidence.md)
- [Cancer-site prevention map](prevention/cancer-site-prevention-map.md)
- [Colorectal cancer prevention page](cancer-types/colorectal-cancer.md)
- [Cervical cancer prevention page](cancer-types/cervical-cancer.md)
- [Breast cancer prevention page](cancer-types/breast-cancer.md)
- [Liver cancer prevention page](cancer-types/liver-cancer.md)
- [Stomach cancer prevention page](cancer-types/stomach-cancer.md)
- [Lung cancer prevention page](cancer-types/lung-cancer.md)
- [Skin cancer prevention page](cancer-types/skin-cancer.md)
- [Oral/oropharyngeal cancer prevention page](cancer-types/oral-oropharyngeal-cancer.md)
- [Lifestyle and burden evidence](prevention/lifestyle-and-burden-evidence.md)
- [Infection-related cancer prevention](prevention/infection-related-cancer-prevention.md)
- [Misleading prevention claims](prevention/misleading-prevention-claims.md)
- [Cancer claim filter](prevention/cancer-claim-filter.md)
- [How to read cancer headlines](prevention/how-to-read-cancer-headlines.md)
- [Screening public guidance](prevention/screening-public-guidance.md)
- [Screening harms and tradeoffs](prevention/screening-harms-and-tradeoffs.md)
- [How cancer grows](concepts/how-cancer-grows.md)
- [Cancer growth mechanism map](concepts/cancer-growth-mechanism-map.md)
- [Infographic brief](visuals/goal-1-infographic-brief.md)
- [Claim-filter visual](visuals/cancer-claim-filter.svg)
- [How cancer keeps adapting visual](visuals/cancer-keeps-adapting.svg)
- [Screening and vaccination decision visual](visuals/screening-vaccination-decision.svg)

### 2. Agent-Friendly Cancer Specialist Wiki

The second milestone is a specialized wiki that helps agents answer cancer questions with useful, life-preserving rigor.

The wiki should support:

- Source-grounded answers with citations.
- Mechanistic explanations across genetics, immunity, metabolism, tissue ecology, inflammation, aging, infection, environment, and prevention.
- Evidence confidence labels.
- Clear separation between research knowledge, public health guidance, and personal medical advice.
- Pages designed for retrieval by agents as well as reading by humans.

### 3. mRNA Cancer Knowledge Vanguard

The third milestone is to become a frontier knowledge base for mRNA cancer vaccines and therapeutics.

This track should monitor:

- Personalized and off-the-shelf mRNA cancer vaccine strategies.
- Neoantigen discovery and antigen selection.
- Lipid nanoparticle and delivery systems.
- Trial phases, endpoints, safety signals, and clinical constraints.
- Cancer-type-specific evidence and resistance mechanisms.

The goal is research intelligence. Experimental mRNA concepts must never be presented as proven treatment recommendations.

## Research Method

This project should grow mostly through automated crawling, source triage, synthesis, and visual explanation.

Every major claim should be handled with the scientific method:

- Define the question.
- State the hypothesis.
- Gather the evidence.
- Inspect the method quality.
- Record counterevidence and uncertainty.
- Mark the translation stage: cell model, animal model, early human trial, clinical evidence, guideline, or standard of care.
- Update the wiki when stronger evidence changes the picture.

## Evidence Standards

Preferred sources include NCI, NIH, CDC, FDA, WHO/IARC, ClinicalTrials.gov, PubMed, PubMed Central, major journals, professional societies, major cancer centers, systematic reviews, clinical trials, and foundational cancer biology papers.

Preprints, press releases, conference abstracts, patents, and company claims can be tracked, but they must be marked as preliminary.

## Safety Boundary

This wiki is for research, education, prevention literacy, and scientific reasoning. It is not a doctor, diagnostic device, or treatment prescriber.

Agents using this repository should not diagnose people, modify treatment plans, or present experimental therapies as proven. When questions involve symptoms, diagnosis, staging, prognosis, treatment, supplements, clinical trials, or personal risk, responses should include an appropriate medical safety boundary and encourage clinician involvement.

## Project Guide

Agent behavior, crawling rules, wiki structure, evidence handling, visual guidance, and mRNA research priorities are defined in [AGENTS.md](AGENTS.md).
