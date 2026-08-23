# AI-Assisted GRC Analysis

## Purpose

This component explores how automation and Artificial Intelligence can support Cyber GRC analysis without replacing human judgment.

The objective is to transform structured security findings into a repeatable review workflow that can support:

- triage
- prioritization
- GRC domain classification
- privacy review identification
- framework review
- control evidence requests
- analyst decision support

The implementation uses two layers:

1. deterministic preprocessing
2. AI-ready review prompts

Human validation remains mandatory.

---

## Architecture

```text
SECURITY FINDING
       ↓
STRUCTURED JSON
       ↓
RULE-BASED PRE-CLASSIFICATION
       ↓
PRIORITY + GRC DOMAIN TAGS
       ↓
AI REVIEW PROMPT
       ↓
FUTURE LLM ANALYSIS
       ↓
HUMAN VALIDATION
       ↓
RISK DECISION
```

---

## Input

The analyzer reads:

`findings/sample-findings.json`

The file contains synthetic security findings representing scenarios such as:

- public S3 exposure
- excessive IAM permissions
- missing MFA
- incomplete audit logging
- sensitive data without classification
- unresolved Security Hub findings

No real AWS account data is used.

---

## Automated Pre-Classification

The Python script performs a deterministic first-pass analysis.

It considers:

- finding severity
- security keywords
- identity and access indicators
- privacy and data indicators
- logging and monitoring indicators
- configuration issues
- resilience and recovery
- third-party risk
- incident-response context

The output includes:

- automated priority score
- priority category
- detected GRC domains
- privacy review recommendation
- NIST CSF references
- LGPD references
- recommended actions
- AI review prompt
- human validation requirement

---

## Priority Model

The prototype uses severity as the initial weighting factor.

Additional contextual weight may be added when a finding involves:

- personal or sensitive data
- privileged identity and access
- critical incident-response capability

The resulting categories are:

| Priority | Meaning |
| --- | --- |
| P1 - Immediate | Requires immediate review |
| P2 - High | High-priority analyst review |
| P3 - Medium | Standard analyst review |
| P4 - Low | Lower-priority review |

This model is intentionally simplified for portfolio purposes.

It is not a replacement for an organization's approved risk-scoring methodology.

---

## AI Review Prompt

For each finding, the analyzer generates a structured prompt that can later be submitted to an LLM.

The prompt asks the model to:

1. summarize the business risk
2. review the proposed NIST CSF mapping
3. identify control objectives
4. identify evidence required for validation
5. identify missing information and assumptions
6. flag potential privacy or legal review
7. avoid unsupported conclusions regarding LGPD compliance

The model is explicitly instructed not to invent:

- technical evidence
- AWS configurations
- legal conclusions
- compliance status

---

## Human-in-the-Loop

The workflow requires human validation before risk decisions are made.

Human review is necessary for:

- business impact
- likelihood
- risk severity
- control effectiveness
- legal interpretation
- residual risk
- risk acceptance
- remediation priority

The AI-assisted component is therefore treated as decision support.

```text
AI SUGGESTION
     ≠
FINAL RISK DECISION
```

---

## Current Implementation

The current prototype does not call an external AI service.

Instead, it creates AI-ready prompts and demonstrates the preprocessing layer that would precede an LLM integration.

This design keeps the repository:

- reproducible
- credential-free
- safe for public GitHub use
- independent of a specific AI provider

A future version could integrate an approved LLM or enterprise AI service.

---

## Files

### automation/ai_grc_analyzer.py

Python script responsible for:

- loading structured findings
- applying classification rules
- assigning priorities
- identifying GRC domains
- generating AI review prompts
- exporting the analysis

### analysis/ai-assisted-analysis.json

Example output generated from the synthetic findings dataset.

---

## Example Execution

From the repository root:

```bash
python automation/ai_grc_analyzer.py
```

Default input:

```text
findings/sample-findings.json
```

Default output:

```text
analysis/ai-assisted-analysis.json
```

A custom input and output can also be provided:

```bash
python automation/ai_grc_analyzer.py findings/sample-findings.json analysis/ai-assisted-analysis.json
```

---

## Current Sample Result

The current sample dataset contains 6 synthetic findings.

The automated preprocessing produced:

- 1 P1 - Immediate
- 3 P2 - High
- 2 P3 - Medium

All outputs remain subject to human review.

---

## Limitations

This prototype:

- does not inspect a real AWS environment
- does not make API calls to AWS
- does not provide legal advice
- does not determine LGPD compliance
- does not validate control effectiveness
- does not automatically accept or reject risk
- does not currently invoke an LLM

The classification logic is intentionally transparent so that every automated result can be reviewed.

---

## Future Evolution

Possible next steps include:

- integrate an LLM for controlled analysis
- validate outputs against a known framework mapping
- add confidence scores
- add analyst approval fields
- compare AI recommendations with human decisions
- log prompt and response history for auditability
- connect Security Hub findings
- connect AWS Config
- connect Amazon Macie
- create a human-review workflow
- create a dashboard for risk and remediation metrics

---

## Core Principle

```text
AUTOMATION
    +
AI ASSISTANCE
    +
HUMAN VALIDATION
    =
RESPONSIBLE GRC DECISION SUPPORT
```

AI can accelerate analysis and improve consistency, but accountability for risk decisions remains human.
