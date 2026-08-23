# Cyber GRC Risk Assessment Methodology

## 1. Purpose

This document describes the methodology used in the Cyber GRC Risk Register project.

The objective is to provide a consistent process for transforming technical cybersecurity findings into business-oriented risks that can be assessed, prioritized, treated, monitored, and mapped to governance and compliance references.

The methodology connects:

* technical security findings
* assets
* threat scenarios
* business impact
* likelihood
* impact
* inherent risk
* security controls
* NIST Cybersecurity Framework 2.0
* LGPD considerations
* treatment plans
* residual risk
* risk ownership
* monitoring

This methodology was created for educational and portfolio purposes and represents a simplified Cyber GRC assessment model.

---

## 2. Assessment Context

The case study uses a fictional e-commerce company called NovaShop Cloud.

The organization operates primarily in AWS and processes customer, authentication, order, and operational information.

The simulated environment includes services and capabilities such as:

* Amazon S3
* AWS IAM
* EC2
* relational databases
* AWS CloudTrail
* AWS Config
* AWS Security Hub
* Amazon CloudWatch
* Amazon Macie
* AWS Backup

The assessment assumes that the company has grown rapidly and that some security and governance controls have been implemented inconsistently.

---

## 3. Assessment Workflow

The Cyber GRC analysis follows the process below:

```text
TECHNICAL FINDING
        ↓
ASSET IDENTIFICATION
        ↓
THREAT SCENARIO
        ↓
BUSINESS RISK
        ↓
LIKELIHOOD
        +
IMPACT
        ↓
INHERENT RISK
        ↓
EXISTING / PROPOSED CONTROLS
        ↓
FRAMEWORK MAPPING
        ↓
RISK TREATMENT
        ↓
RESIDUAL RISK
        ↓
RISK OWNER
        ↓
MONITORING
```

Each stage provides additional context that helps transform a technical issue into information that can support governance and business decision-making.

---

## 4. Technical Finding

A technical finding describes an observed or simulated security weakness.

Examples include:

* an S3 bucket allowing public access
* excessive IAM permissions
* MFA not enabled for privileged access
* incomplete CloudTrail coverage
* sensitive data without documented classification
* unresolved high-severity Security Hub findings

A finding is not automatically equivalent to a business risk.

The finding represents the technical condition that may contribute to a risk scenario.

---

## 5. Asset Identification

Each finding is associated with an asset or resource that may be affected.

Examples include:

* customer data
* S3 buckets
* databases
* IAM roles
* privileged identities
* audit logs
* backup systems
* security findings
* third-party access

Understanding the asset helps determine the business relevance of the technical condition.

---

## 6. Threat Scenario

The threat scenario describes how the technical weakness could potentially be exploited or contribute to an undesirable event.

Example:

```text
Finding:
S3 bucket permits public access

Threat Scenario:
An unauthorized external user accesses objects stored in the bucket
```

The goal is to establish a logical connection between the technical weakness and a plausible security event.

---

## 7. Business Risk

The business risk translates the technical scenario into potential organizational consequences.

Example:

```text
Technical Finding
S3 bucket allows public access

        ↓

Threat Scenario
Unauthorized access to stored files

        ↓

Business Risk
Exposure of customer personal data may result in
privacy impact, regulatory exposure, reputational
damage, and incident-response costs
```

This translation is central to Cyber GRC because technical findings need to be understandable to stakeholders outside security engineering teams.

---

## 8. Likelihood Assessment

Likelihood represents the estimated probability that the risk scenario could occur.

The project uses a five-level qualitative scale.

| Score | Level          | Description                                             |
| ----- | -------------- | ------------------------------------------------------- |
| 1     | Rare           | The scenario is unlikely to occur                       |
| 2     | Unlikely       | The scenario could occur but is not expected            |
| 3     | Possible       | The scenario may reasonably occur                       |
| 4     | Likely         | The scenario has a significant possibility of occurring |
| 5     | Almost Certain | The scenario is highly likely to occur                  |

Likelihood estimates are based on the simulated environment, the nature of the finding, exposure, available controls, and reasonable assumptions made for the case study.

They do not represent statistical probabilities.

---

## 9. Impact Assessment

Impact represents the potential consequence to the organization if the risk scenario occurs.

The project uses the following scale:

| Score | Level         | Description                                                                    |
| ----- | ------------- | ------------------------------------------------------------------------------ |
| 1     | Insignificant | Minimal operational or business impact                                         |
| 2     | Minor         | Limited disruption or manageable impact                                        |
| 3     | Moderate      | Noticeable operational, financial, or compliance impact                        |
| 4     | Major         | Significant impact requiring management attention                              |
| 5     | Severe        | Potentially serious operational, regulatory, financial, or reputational impact |

Impact may consider factors such as:

* confidentiality
* integrity
* availability
* privacy
* financial loss
* business disruption
* regulatory exposure
* customer impact
* reputation

---

## 10. Inherent Risk

Inherent risk represents the level of risk before considering the effectiveness of additional treatment controls proposed in the assessment.

The project calculates inherent risk using:

```text
Inherent Risk Score = Likelihood × Impact
```

Example:

```text
Likelihood = 4
Impact = 5

4 × 5 = 20
```

The resulting score is classified using the following scale:

| Score | Classification |
| ----- | -------------- |
| 1–4   | Low            |
| 5–9   | Moderate       |
| 10–16 | High           |
| 17–25 | Critical       |

This simplified matrix is used to support prioritization.

---

## 11. Control Identification

After the inherent risk is assessed, relevant controls are identified.

Controls may be:

### Preventive

Designed to reduce the probability of an incident.

Examples:

* MFA
* least privilege
* S3 Block Public Access
* encryption
* restrictive IAM policies

### Detective

Designed to identify suspicious activity or control failures.

Examples:

* AWS CloudTrail
* AWS Config
* Security Hub
* CloudWatch monitoring
* Amazon Macie

### Corrective or Recovery

Designed to reduce impact or restore services after an incident.

Examples:

* AWS Backup
* restore procedures
* incident-response playbooks
* remediation workflows

Multiple control types may be used together.

---

## 12. NIST CSF 2.0 Mapping

Security risks and controls are mapped to relevant NIST Cybersecurity Framework 2.0 Functions and Categories.

The six Functions are:

```text
GOVERN
IDENTIFY
PROTECT
DETECT
RESPOND
RECOVER
```

Examples used in this project include:

* GV.RR - Roles, Responsibilities, and Authorities
* GV.SC - Cybersecurity Supply Chain Risk Management
* ID.AM - Asset Management
* ID.RA - Risk Assessment
* PR.AA - Identity Management, Authentication, and Access Control
* PR.DS - Data Security
* DE.CM - Continuous Monitoring
* DE.AE - Adverse Event Analysis
* RS.MA - Incident Management
* RS.AN - Incident Analysis
* RS.CO - Incident Response Reporting and Communication
* RS.MI - Incident Mitigation
* RC.RP - Incident Recovery Plan Execution

The mapping is used to organize cybersecurity outcomes and demonstrate how individual risks relate to broader governance and security objectives.

The mappings are contextual and should be validated when applied to a real organization.

---

## 13. LGPD Mapping

Some scenarios involve personal data and therefore include references to relevant LGPD provisions.

The project considers concepts such as:

* security
* prevention
* accountability
* protection against unauthorized access
* incident response
* governance and good practices

Examples include references to:

* Article 6
* Article 46
* Article 48
* Article 50

LGPD references are included as a governance and compliance perspective.

They should not be interpreted as a legal conclusion that implementing a specific technical control automatically guarantees compliance.

A real compliance assessment would require analysis of:

* processing activities
* legal basis
* roles and responsibilities
* contracts
* data flows
* organizational context
* regulatory guidance
* applicable legal requirements

---

## 14. Risk Treatment

Each risk is assigned a treatment strategy.

Common risk treatment options include:

### Mitigate

Implement or improve controls to reduce likelihood or impact.

### Avoid

Stop the activity that creates the risk.

### Transfer

Transfer part of the financial or operational consequence through mechanisms such as contracts or insurance.

### Accept

Formally accept the risk when it falls within the organization's risk appetite.

In this portfolio scenario, most identified risks use mitigation because they represent security weaknesses that can be reduced through technical or governance controls.

---

## 15. Treatment Plan

The treatment plan defines actions that should be taken to reduce the risk.

Example:

```text
Risk:
Unauthorized access caused by excessive IAM permissions

Treatment:
Mitigate

Actions:
- Review permissions
- Remove unused access
- Apply least privilege
- Use temporary credentials
- Establish periodic entitlement reviews
```

A real organization would normally add:

* accountable owner
* deadline
* budget
* implementation status
* evidence
* dependencies
* exception process

---

## 16. Residual Risk

Residual risk represents the estimated level of risk remaining after the proposed controls are implemented and considered effective.

The same calculation model is used:

```text
Residual Risk Score =
Residual Likelihood × Residual Impact
```

Example:

```text
Before treatment:

Likelihood = 4
Impact = 5

Inherent Risk = 20
Classification = Critical


After treatment:

Residual Likelihood = 1
Residual Impact = 5

Residual Risk = 5
Classification = Moderate
```

In this example, controls significantly reduce the likelihood of exposure.

The potential impact may remain high because exposure of sensitive customer data could still have serious consequences if the event occurs.

This illustrates an important risk-management principle:

```text
Controls do not necessarily eliminate risk.
They modify risk.
```

---

## 17. Risk Owner

Each risk is assigned to a simulated risk owner.

Examples include:

* Cloud Security Lead
* Data Owner
* IAM Lead
* Security Operations Lead
* Privacy Lead
* Vendor Risk Lead
* Incident Response Lead
* Cloud Operations Lead

The purpose is to demonstrate accountability.

The Risk Owner is responsible for ensuring that the risk is understood, monitored, and treated according to organizational governance processes.

---

## 18. Risk Status

The Risk Register uses a simple status field.

Examples include:

* Open
* Planned
* In Progress
* Mitigated
* Accepted
* Closed

For the initial portfolio version, treatment actions are mainly marked as Planned because the environment is simulated and the proposed controls have not actually been implemented.

---

## 19. Human Validation

Human validation is a required component of this methodology.

Automated tools and AI may support:

* finding classification
* risk description
* framework mapping
* control recommendations
* prioritization
* documentation

However, final risk decisions should consider organizational context.

The workflow therefore includes:

```text
AUTOMATED OR AI-ASSISTED ANALYSIS
              ↓
        HUMAN REVIEW
              ↓
    CONTEXT VALIDATION
              ↓
       RISK DECISION
```

Human validation is particularly important for:

* business impact
* likelihood
* legal interpretation
* control effectiveness
* residual risk
* risk acceptance
* treatment prioritization

---

## 20. Assumptions and Limitations

This project contains several intentional simplifications.

### Fictional Environment

NovaShop Cloud is fictional.

No real AWS environment, customer data, credentials, or security findings are used.

### Synthetic Findings

The security findings are synthetic examples inspired by common cloud security scenarios.

They are not exports from AWS services.

### Simplified Risk Scoring

The 5 × 5 matrix is used for educational purposes.

Real organizations may use:

* quantitative models
* financial impact estimates
* different likelihood scales
* risk appetite thresholds
* risk velocity
* control maturity
* threat intelligence

### Simplified Framework Mapping

NIST CSF and LGPD mappings are illustrative and contextual.

A production assessment would require validation against the organization's actual environment, policies, regulatory obligations, and control architecture.

---

## 21. Methodology Summary

The project follows this logic:

```text
OBSERVE
Technical finding

        ↓

UNDERSTAND
Asset + threat + business context

        ↓

ASSESS
Likelihood + impact

        ↓

PRIORITIZE
Inherent risk

        ↓

CONTROL
AWS and governance controls

        ↓

MAP
NIST CSF + LGPD perspective

        ↓

TREAT
Risk treatment plan

        ↓

REASSESS
Residual risk

        ↓

GOVERN
Owner + status + monitoring
```

The purpose of the methodology is to demonstrate how Cyber GRC can connect technical cybersecurity information with governance, risk management, compliance, and business decision-making.
