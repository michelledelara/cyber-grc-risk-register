# 🛡️ Cyber GRC Risk Register

>  Practical Cyber GRC case study connecting AWS security findings, cybersecurity risks, controls, NIST CSF 2.0 and LGPD considerations.

---

## 🎯 About the Project

This project simulates a Cyber GRC assessment for a fictional e-commerce company operating primarily in AWS Cloud.

The company has experienced rapid growth and processes customer and operational data but does not yet have a mature cybersecurity governance structure.

The objective is to identify security weaknesses, translate technical findings into business risks and create a structured Risk Register that supports prioritization and risk treatment.

The project connects:

* Cybersecurity findings
* Business impact
* Risk assessment
* AWS security controls
* NIST Cybersecurity Framework 2.0
* LGPD
* Risk treatment
* Residual risk
* Governance and accountability

---

## 🏢 Scenario

The fictional company used in this case study is:

### NovaShop Cloud

NovaShop Cloud is a growing e-commerce company that operates its digital platform using AWS services.

The environment contains:

* Amazon S3
* IAM
* EC2
* relational databases
* CloudTrail
* AWS Config
* Security Hub
* CloudWatch

The platform processes customer information, authentication data, orders and operational information.

As the company expanded, cloud resources were created quickly and security controls were implemented inconsistently.

Management requested a Cyber GRC assessment to identify the most relevant risks and define a prioritized remediation plan.

---

## ❓ Business Problem

Rapid cloud adoption can create security and governance gaps when resources, permissions and controls are deployed without a consistent risk management process.

Examples include:

* excessive IAM permissions
* publicly accessible storage
* missing MFA
* insufficient logging
* lack of data classification
* configuration drift
* weak backup controls
* untracked security findings
* third-party access risks
* incomplete incident response processes

The central question of this project is:

> How can technical AWS security findings be translated into business risks and managed through a structured Cyber GRC process?

---

## 🔄 Cyber GRC Workflow

```text
AWS ENVIRONMENT
      ↓
SECURITY FINDING
      ↓
ASSET IDENTIFICATION
      ↓
BUSINESS IMPACT
      ↓
RISK IDENTIFICATION
      ↓
LIKELIHOOD + IMPACT
      ↓
INHERENT RISK
      ↓
CONTROL MAPPING
      ↓
NIST CSF + LGPD
      ↓
RISK TREATMENT
      ↓
RESIDUAL RISK
      ↓
MONITORING
```

---

## 📊 Risk Assessment Methodology

Each risk is evaluated using two dimensions:

### Likelihood

| Score | Level          |
| ----- | -------------- |
| 1     | Rare           |
| 2     | Unlikely       |
| 3     | Possible       |
| 4     | Likely         |
| 5     | Almost Certain |

### Impact

| Score | Level         |
| ----- | ------------- |
| 1     | Insignificant |
| 2     | Minor         |
| 3     | Moderate      |
| 4     | Major         |
| 5     | Severe        |

The risk score is calculated as:

```text
Risk Score = Likelihood × Impact
```

### Risk Classification

| Score | Classification |
| ----- | -------------- |
| 1–4   | Low            |
| 5–9   | Moderate       |
| 10–16 | High           |
| 17–25 | Critical       |

This simplified methodology was created for educational and portfolio purposes.

---
## 📊 Risk Matrix

The 10 cybersecurity risks were assessed using a 5×5 matrix based on Likelihood and Impact.

### Inherent Risk

The inherent risk represents the exposure before considering the effectiveness of the proposed treatment controls.

![Inherent Risk Matrix](risk-matrix-inherent.png)

The initial assessment identified:

- 3 Critical risks
- 7 High risks
- 0 Moderate risks
- 0 Low risks

The Critical risks were associated with:

- RISK-001 — Public exposure of customer data
- RISK-003 — Missing MFA for privileged access
- RISK-010 — Inadequate incident response capability

---

### Residual Risk

Residual risk represents the estimated exposure after the proposed controls are implemented and assumed to operate effectively.

![Residual Risk Matrix](risk-matrix-residual.png)

After the proposed treatment:

- 0 Critical risks
- 0 High risks
- 9 Moderate risks
- 1 Low risk

The reduction does not mean that risk has been eliminated.

It demonstrates the expected effect of the proposed controls under the assumptions of this simulated assessment.

> Residual risk should be reassessed using evidence of actual control implementation and effectiveness before a real risk-acceptance decision is made.

## 🔥 Initial Risk Scenarios

The assessment includes the following cybersecurity scenarios:

| ID       | Risk Scenario                                                               | AWS Context              | NIST CSF           |
| -------- | --------------------------------------------------------------------------- | ------------------------ | ------------------ |
| RISK-001 | Exposure of customer data through public storage                            | Amazon S3                | PROTECT            |
| RISK-002 | Unauthorized access caused by excessive permissions                         | AWS IAM                  | PROTECT            |
| RISK-003 | Account compromise due to missing MFA                                       | AWS IAM                  | PROTECT            |
| RISK-004 | Security incidents cannot be properly investigated due to insufficient logs | CloudTrail / CloudWatch  | DETECT             |
| RISK-005 | Sensitive data is stored without proper classification                      | S3 / Databases           | IDENTIFY / PROTECT |
| RISK-006 | Security controls become ineffective due to configuration drift             | AWS Config               | PROTECT / DETECT   |
| RISK-007 | Critical data cannot be recovered after an incident                         | Backup / Recovery        | RECOVER            |
| RISK-008 | Critical security findings remain unresolved                                | Security Hub             | IDENTIFY           |
| RISK-009 | Third-party access introduces unauthorized exposure                         | IAM / External Providers | GOVERN             |
| RISK-010 | Organization is unable to respond effectively to a data breach              | Incident Response        | RESPOND            |

---

## ☁️ AWS Security Controls

The project considers AWS security capabilities such as:

### AWS IAM

Used to manage identities, permissions and access controls.

Relevant controls include:

* least privilege
* MFA
* temporary credentials
* role-based access
* permissions review

### Amazon S3

Security considerations include:

* Block Public Access
* bucket policies
* encryption
* access monitoring
* data classification

### AWS CloudTrail

Provides visibility into API activity and supports security investigations and auditability.

### AWS Config

Supports continuous evaluation of AWS resource configurations and identification of non-compliant resources.

### AWS Security Hub

Provides centralized visibility into security findings and helps prioritize security issues across the AWS environment.

---

## 🧭 NIST Cybersecurity Framework 2.0

The project uses the six functions of NIST CSF 2.0:

```text
GOVERN
   ↓
IDENTIFY
   ↓
PROTECT
   ↓
DETECT
   ↓
RESPOND
   ↓
RECOVER
```

The framework is used to organize cybersecurity outcomes and connect technical findings with broader risk management activities.

---

## ⚖️ LGPD Perspective

Some risks in this scenario involve personal data.

The analysis therefore considers requirements and principles related to:

* security
* prevention
* accountability
* protection against unauthorized access
* protection against accidental or unlawful loss or alteration
* incident management
* governance and good practices

The purpose is not to claim that a technical control alone guarantees legal compliance.

Instead, LGPD is used as one of the regulatory perspectives considered during risk analysis.

---

## 🧠 From Technical Finding to Business Risk

A central concept of this project is distinguishing a technical finding from a risk.

Example:

```text
TECHNICAL FINDING

S3 bucket allows public access.

        ↓

THREAT

Unauthorized third party accesses stored files.

        ↓

BUSINESS RISK

Exposure of customer personal data may result in privacy impact,
regulatory exposure, reputational damage and incident response costs.

        ↓

CONTROL

Block Public Access
IAM policies
Monitoring
Data classification

        ↓

RESIDUAL RISK

Risk remaining after controls are implemented.
```

---

## 📁 Project Files

### risk-register.csv

Structured Cyber GRC Risk Register containing:

* risk ID
* asset
* finding
* threat
* business risk
* likelihood
* impact
* inherent risk
* controls
* NIST CSF mapping
* LGPD mapping
* risk owner
* treatment
* residual risk
* status

### findings/sample-findings.json

Structured representation of technical security findings that can later be used for automation or AI-assisted analysis.

### docs/methodology.md

Detailed explanation of the risk assessment methodology.

### docs/framework-mapping.md

Mapping between security scenarios, NIST CSF 2.0, AWS controls and privacy considerations.

### docs/executive-risk-summary.md

Executive-level summary of the Cyber GRC assessment, highlighting the risk posture, Top 3 Critical risks, management priorities, proposed residual risk and recommended Cyber GRC indicators.

### risk-matrix-inherent.png

Visual representation of the 10 cybersecurity risks before the proposed treatment controls.

### risk-matrix-residual.png

Visual representation of the estimated residual risk after the proposed treatment controls are assumed to be effectively implemented.

### automation/ai_grc_analyzer.py

Python-based preprocessing component that classifies structured security findings, assigns review priorities, identifies GRC domains and generates AI-ready review prompts.

### analysis/ai-assisted-analysis.json

Example output generated by the automated GRC preprocessing pipeline.

### docs/ai-assisted-grc.md

Documentation of the AI-assisted Cyber GRC architecture, including automation, human validation, limitations and future LLM integration.

## 🤖 AI-Assisted GRC Analysis

This project includes an automated preprocessing layer designed to support Cyber GRC analysis.

The current workflow transforms structured security findings into:

- automated review priorities
- GRC domain classifications
- privacy review indicators
- structured framework context
- recommended actions
- AI-ready review prompts

The workflow follows:

```text
SECURITY FINDING
       ↓
STRUCTURED JSON
       ↓
RULE-BASED PRE-CLASSIFICATION
       ↓
PRIORITY + GRC DOMAIN TAGS
       ↓
AI-READY REVIEW PROMPT
       ↓
HUMAN VALIDATION
       ↓
RISK DECISION
```

AI would support the analysis while human review remains responsible for risk validation and decision-making.

---

## 🚀 Project Roadmap

- [x] Build the initial Risk Register
- [x] Add 10 cybersecurity risks
- [x] Calculate inherent risk
- [x] Define risk treatment plans
- [x] Calculate residual risk
- [x] Map risks to NIST CSF 2.0
- [x] Map privacy-related risks to LGPD
- [x] Add AWS security controls
- [x] Create structured JSON findings
- [x] Add a risk matrix visualization
- [x] Create an executive risk summary
- [x] Explore AI-assisted GRC analysis

---

## 🏁 Project Goal

The objective of this project is to demonstrate how Cyber GRC can connect technical cybersecurity issues with business risk and governance.

```text
TECHNICAL FINDING
        +
BUSINESS CONTEXT
        +
RISK ASSESSMENT
        +
FRAMEWORKS
        +
CONTROLS
        =
CYBER GRC DECISION SUPPORT
```

> Cybersecurity findings become more useful to organizations when they are translated into risks that business and governance stakeholders can understand, prioritize and manage.
