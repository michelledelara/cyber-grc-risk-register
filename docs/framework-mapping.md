# Cyber GRC Framework Mapping

## 1. Purpose

This document maps the cybersecurity risks identified in the NovaShop Cloud case study to:

* AWS security capabilities
* NIST Cybersecurity Framework 2.0
* LGPD considerations
* security controls
* expected control evidence
* governance responsibilities

The purpose is to demonstrate how technical findings can be connected to broader Cyber GRC requirements.

This mapping is illustrative and was created for educational and portfolio purposes.

---

## 2. Mapping Approach

The project follows this structure:

```text
TECHNICAL FINDING
        ↓
BUSINESS RISK
        ↓
AWS SECURITY CONTROL
        ↓
NIST CSF 2.0
        ↓
LGPD PERSPECTIVE
        ↓
CONTROL EVIDENCE
        ↓
HUMAN VALIDATION
```

The mapping does not assume that one AWS control automatically satisfies a NIST or LGPD requirement.

Instead, the objective is to identify relationships that can support risk analysis, control design, governance, and audit activities.

---

# RISK-001

## Public exposure of customer data through Amazon S3

### Technical Finding

An S3 bucket containing customer information allows public access.

### Risk

Unauthorized individuals may access customer data, potentially resulting in privacy impact, regulatory exposure, reputational damage, and incident-response costs.

### AWS Context

* Amazon S3
* AWS IAM
* AWS Key Management Service
* Amazon Macie
* CloudTrail
* Security Hub

### NIST CSF 2.0 Mapping

* PR.DS - Data Security
* PR.AA - Identity Management, Authentication, and Access Control
* DE.CM - Continuous Monitoring

### LGPD Perspective

Relevant considerations include:

* Article 46 - security measures for protecting personal data
* Article 50 - governance and good practices
* Article 6 - security, prevention and accountability principles

### Controls

* Enable S3 Block Public Access
* Review bucket policies
* Remove unnecessary ACL-based access
* Apply IAM least privilege
* Encrypt sensitive data
* Classify stored information
* Monitor public exposure
* Detect sensitive data using Amazon Macie

### Expected Evidence

Possible evidence includes:

* S3 Block Public Access configuration
* bucket policy export
* IAM policy configuration
* encryption settings
* AWS Config evaluation
* Security Hub finding status
* Macie classification results
* CloudTrail access logs
* remediation ticket
* approval or exception record

### Control Owner

Cloud Security Lead / Data Owner

---

# RISK-002

## Excessive IAM permissions

### Technical Finding

IAM users or roles have privileges broader than required for their business activities.

### Risk

Compromised or misused credentials could enable unauthorized access, modification of resources, exposure of data, or service disruption.

### AWS Context

* AWS IAM
* IAM Access Analyzer
* AWS Organizations

### NIST CSF 2.0 Mapping

* PR.AA - Identity Management, Authentication, and Access Control
* GV.RR - Roles, Responsibilities, and Authorities
* ID.RA - Risk Assessment

### LGPD Perspective

Relevant considerations include:

* Article 46
* Article 50

Access to personal data should be governed according to appropriate security and governance mechanisms.

### Controls

* Apply least privilege
* Remove unused permissions
* Prefer IAM roles
* Use temporary credentials
* Review permission boundaries
* Review cross-account access
* Perform periodic entitlement reviews

### Expected Evidence

* IAM role configuration
* IAM policy documents
* Access Analyzer findings
* permissions review report
* approved access requests
* access review records
* role-owner documentation
* remediation evidence

### Control Owner

IAM / Security Lead

---

# RISK-003

## MFA not enforced for privileged access

### Technical Finding

Privileged human identities can authenticate without multi-factor authentication.

### Risk

Credential theft or phishing could result in privileged account compromise and unauthorized administrative activity.

### AWS Context

* AWS IAM
* AWS IAM Identity Center
* Identity Provider
* CloudTrail

### NIST CSF 2.0 Mapping

* PR.AA - Identity Management, Authentication, and Access Control

### LGPD Perspective

Relevant considerations include:

* Article 46
* Article 50

Stronger authentication mechanisms contribute to reducing unauthorized access to systems processing personal data.

### Controls

* Enforce MFA
* Prefer federation for human users
* Use temporary credentials
* Restrict root account usage
* Monitor privileged authentication
* Review privileged identities periodically

### Expected Evidence

* MFA configuration
* IAM credential report
* identity-provider configuration
* privileged user inventory
* authentication logs
* access review records
* root account security configuration

### Control Owner

IAM / Security Lead

---

# RISK-004

## Incomplete security logging

### Technical Finding

CloudTrail logging is incomplete, not centrally retained, or insufficiently integrated with monitoring processes.

### Risk

Malicious or unauthorized activity may not be detected or investigated effectively.

### AWS Context

* AWS CloudTrail
* Amazon CloudWatch
* Amazon S3
* AWS Security Hub

### NIST CSF 2.0 Mapping

* DE.CM - Continuous Monitoring
* DE.AE - Adverse Event Analysis
* RS.AN - Incident Analysis

### LGPD Perspective

Relevant considerations include:

* Article 46
* Article 48
* Article 50

Logging may support incident investigation, accountability, and assessment of events involving personal data.

### Controls

* Enable CloudTrail across relevant accounts and Regions
* Centralize audit logs
* Protect log storage
* Enable log integrity validation
* Configure retention
* Integrate logs with monitoring
* Create security alerts

### Expected Evidence

* CloudTrail configuration
* trail coverage report
* centralized logging architecture
* log retention policy
* CloudWatch alarm configuration
* log integrity settings
* incident investigation records
* SIEM or monitoring integration

### Control Owner

Security Operations Lead

---

# RISK-005

## Sensitive data without classification

### Technical Finding

Personal or sensitive information is stored without documented classification, ownership, or retention requirements.

### Risk

Data may receive inappropriate protection, excessive access, or inadequate retention management.

### AWS Context

* Amazon S3
* Amazon Macie
* AWS IAM
* AWS KMS
* relational databases

### NIST CSF 2.0 Mapping

* ID.AM - Asset Management
* PR.DS - Data Security
* GV.RR - Roles, Responsibilities, and Authorities

### LGPD Perspective

Relevant considerations include:

* Article 6
* Article 46
* Article 50

The scenario may involve principles related to necessity, security, prevention and accountability.

### Controls

* Create data inventory
* Define classification levels
* Assign Data Owners
* Define retention requirements
* Use Amazon Macie
* Apply encryption
* Restrict access according to classification
* Review data lifecycle requirements

### Expected Evidence

* data inventory
* classification policy
* Data Owner assignment
* Macie findings
* data retention policy
* encryption configuration
* IAM permissions
* data lifecycle records
* approved data handling procedures

### Control Owner

Data Owner / Privacy Lead

---

# RISK-006

## Configuration drift

### Technical Finding

AWS resources may deviate from approved security configurations without timely detection.

### Risk

Configuration changes may introduce vulnerabilities, inconsistent controls, or unintended exposure.

### AWS Context

* AWS Config
* Security Hub
* Infrastructure as Code
* AWS Organizations

### NIST CSF 2.0 Mapping

* PR.PS - Platform Security
* DE.CM - Continuous Monitoring
* GV.PO - Policy

### LGPD Perspective

Relevant considerations include:

* Article 46
* Article 50

Security measures should remain appropriate and consistently implemented across systems that process personal data.

### Controls

* Define security baselines
* Enable AWS Config
* Use AWS Config Rules
* Use conformance packs
* Adopt Infrastructure as Code
* Monitor configuration changes
* Automate remediation where appropriate

### Expected Evidence

* AWS Config inventory
* Config Rules
* conformance pack results
* Infrastructure as Code templates
* change records
* approved configuration baseline
* remediation logs
* Security Hub findings

### Control Owner

Cloud Platform / DevOps Lead

---

# RISK-007

## Inadequate backup and recovery capability

### Technical Finding

Critical systems and data do not have sufficiently tested backup and recovery procedures.

### Risk

Data loss, ransomware, accidental deletion, or system failure may result in prolonged downtime and loss of critical information.

### AWS Context

* AWS Backup
* Amazon S3
* databases
* backup vaults
* cross-account backup

### NIST CSF 2.0 Mapping

* PR.IR - Technology Infrastructure Resilience
* RC.RP - Incident Recovery Plan Execution

### LGPD Perspective

Relevant considerations include:

* Article 46
* Article 50

Availability and resilience are relevant components of protecting systems that process personal data.

### Controls

* Define backup policy
* Define RPO and RTO
* Automate backups
* Protect backup vaults
* Use cross-account or cross-Region copies when appropriate
* Test restoration regularly
* Document recovery procedures

### Expected Evidence

* AWS Backup policy
* backup job history
* recovery point inventory
* restore test results
* RPO/RTO documentation
* recovery runbook
* backup access configuration
* evidence of successful restoration tests

### Control Owner

IT Continuity / Cloud Operations Lead

---

# RISK-008

## Security findings remain unresolved

### Technical Finding

High-severity Security Hub findings remain open without consistent ownership, remediation targets, or escalation.

### Risk

Known vulnerabilities or weaknesses may remain exploitable and increase organizational exposure.

### AWS Context

* AWS Security Hub
* Amazon EventBridge
* AWS Config
* ticketing or workflow platform

### NIST CSF 2.0 Mapping

* ID.RA - Risk Assessment
* DE.AE - Adverse Event Analysis
* GV.OV - Oversight
* ID.IM - Improvement

### LGPD Perspective

Relevant considerations include:

* Article 46
* Article 50

Organizations should maintain mechanisms for security governance, monitoring, and remediation.

### Controls

* Define remediation SLAs
* Assign finding owners
* Prioritize according to severity and business context
* Create escalation procedures
* Integrate findings with workflow tools
* Monitor overdue findings
* Report metrics to governance stakeholders

### Expected Evidence

* Security Hub findings
* remediation SLA policy
* tickets
* assigned owners
* remediation timestamps
* exception records
* monthly security metrics
* governance reports
* management review minutes

### Control Owner

Security Operations Lead

---

# RISK-009

## Third-party cloud access

### Technical Finding

External providers have standing credentials or permissions broader than required.

### Risk

Compromise or misuse of a third-party identity could expose cloud resources or data.

### AWS Context

* AWS IAM
* IAM roles
* federation
* IAM Access Analyzer
* CloudTrail

### NIST CSF 2.0 Mapping

* GV.SC - Cybersecurity Supply Chain Risk Management
* PR.AA - Identity Management, Authentication, and Access Control
* GV.RR - Roles, Responsibilities, and Authorities

### LGPD Perspective

Relevant considerations include:

* Article 46
* Article 50

Third-party access should be subject to appropriate governance, security requirements, and accountability mechanisms.

### Controls

* Use federated or temporary access
* Avoid permanent vendor credentials
* Apply least privilege
* Define expiration dates
* Review vendor access periodically
* Monitor third-party activities
* Include security requirements in contracts and governance processes

### Expected Evidence

* third-party access inventory
* IAM roles
* federation configuration
* vendor access approvals
* contract security clauses
* access expiration configuration
* periodic access reviews
* CloudTrail activity
* vendor risk assessment

### Control Owner

Vendor Risk / Security Lead

---

# RISK-010

## Inadequate incident response capability

### Technical Finding

The organization does not maintain a sufficiently documented and tested cybersecurity and personal-data incident response process.

### Risk

During a security incident, unclear responsibilities and procedures may delay containment, investigation, communication, and recovery.

### AWS Context

* CloudTrail
* CloudWatch
* Security Hub
* EventBridge
* incident-response tools
* evidence storage

### NIST CSF 2.0 Mapping

* RS.MA - Incident Management
* RS.AN - Incident Analysis
* RS.CO - Incident Response Reporting and Communication
* RS.MI - Incident Mitigation
* GV.RR - Roles, Responsibilities, and Authorities

### LGPD Perspective

Relevant considerations include:

* Article 46
* Article 48
* Article 50

Article 48 may become particularly relevant where a security incident involving personal data may cause relevant risk or damage to data subjects.

### Controls

* Create an incident-response plan
* Define roles and responsibilities
* Establish escalation procedures
* Define security and privacy communication paths
* Create cloud-specific playbooks
* Conduct tabletop exercises
* Define evidence preservation procedures
* Review lessons learned

### Expected Evidence

* incident-response policy
* incident-response plan
* escalation matrix
* contact list
* incident playbooks
* tabletop exercise results
* incident tickets
* evidence collection procedure
* post-incident review
* communication records

### Control Owner

Incident Response Lead / Privacy Lead

---

# 3. Control Evidence Categories

Evidence can be grouped into several categories.

## Configuration Evidence

Evidence showing how a technical control is configured.

Examples:

* IAM policies
* S3 settings
* MFA configuration
* AWS Config rules
* CloudTrail configuration
* backup policies

---

## Operational Evidence

Evidence demonstrating that a control is operating.

Examples:

* monitoring alerts
* backup job history
* Security Hub findings
* access reviews
* incident tickets
* restore test results

---

## Governance Evidence

Evidence demonstrating oversight and accountability.

Examples:

* policies
* procedures
* approved standards
* risk acceptance records
* management reports
* committee minutes
* assigned owners
* remediation SLAs

---

## Audit Evidence

Evidence used to verify whether a control exists and operates as expected.

Examples:

```text
CONTROL
   ↓
EXPECTED CONFIGURATION
   ↓
TECHNICAL EVIDENCE
   ↓
OPERATIONAL RECORD
   ↓
OWNER
   ↓
REVIEW / APPROVAL
```

The existence of a configuration alone does not necessarily prove that a control is effective.

---

# 4. From Framework to Evidence

One objective of the project is to avoid stopping at framework mapping.

A mature GRC workflow should eventually connect:

```text
FRAMEWORK REQUIREMENT
        ↓
CONTROL
        ↓
CONTROL OWNER
        ↓
IMPLEMENTATION
        ↓
EVIDENCE
        ↓
TESTING
        ↓
RESULT
        ↓
REMEDIATION
```

This creates traceability between governance requirements and operational security activities.

---

# 5. Example Traceability

An example using RISK-003:

```text
RISK
Privileged account compromise

        ↓

NIST CSF
PR.AA

        ↓

CONTROL
Multi-factor authentication

        ↓

AWS IMPLEMENTATION
MFA / federated authentication

        ↓

EVIDENCE
IAM credential report
Identity provider configuration
Authentication logs

        ↓

CONTROL TEST
Verify that privileged identities cannot authenticate
without required MFA

        ↓

RESULT
Effective / Partially Effective / Ineffective

        ↓

ACTION
Maintain, improve, or remediate control
```

This traceability is important for:

* audits
* compliance assessments
* risk management
* control testing
* executive reporting
* remediation tracking

---

# 6. Human Validation

Framework mappings and control recommendations should be validated by qualified professionals before being used in a real environment.

Human review is necessary because control effectiveness depends on factors such as:

* organizational context
* architecture
* regulatory obligations
* risk appetite
* contractual requirements
* data sensitivity
* threat environment
* existing controls
* business priorities

The project therefore treats automated mapping as decision support rather than final decision-making.

---

# 7. Limitations

This project uses a fictional AWS environment.

The mappings are simplified and illustrative.

They should not be interpreted as:

* legal advice
* formal certification
* proof of LGPD compliance
* proof of NIST CSF conformity
* official AWS assessment results
* evidence from a real production environment

A real assessment would require direct examination of systems, policies, configurations, contracts, logs, processes, and organizational controls.

---

# 8. Framework Mapping Summary

| Risk     | AWS Area                | NIST CSF 2.0                      | LGPD Perspective | Main Evidence                                         |
| -------- | ----------------------- | --------------------------------- | ---------------- | ----------------------------------------------------- |
| RISK-001 | S3 / IAM / Macie        | PR.DS, PR.AA, DE.CM               | Art. 6, 46, 50   | S3 configuration, IAM policies, Macie findings        |
| RISK-002 | IAM                     | PR.AA, GV.RR, ID.RA               | Art. 46, 50      | IAM policies, access reviews, Access Analyzer         |
| RISK-003 | IAM / Identity          | PR.AA                             | Art. 46, 50      | MFA settings, credential reports, authentication logs |
| RISK-004 | CloudTrail / CloudWatch | DE.CM, DE.AE, RS.AN               | Art. 46, 48, 50  | audit logs, retention settings, alerts                |
| RISK-005 | S3 / Macie / Data       | ID.AM, PR.DS, GV.RR               | Art. 6, 46, 50   | data inventory, Macie results, classification records |
| RISK-006 | AWS Config              | PR.PS, DE.CM, GV.PO               | Art. 46, 50      | Config Rules, baselines, remediation records          |
| RISK-007 | AWS Backup              | PR.IR, RC.RP                      | Art. 46, 50      | backup logs, restore tests, RPO/RTO                   |
| RISK-008 | Security Hub            | ID.RA, DE.AE, GV.OV, ID.IM        | Art. 46, 50      | findings, SLAs, tickets, governance reports           |
| RISK-009 | IAM / Third Party       | GV.SC, PR.AA, GV.RR               | Art. 46, 50      | vendor access reviews, IAM roles, contracts           |
| RISK-010 | Incident Response       | RS.MA, RS.AN, RS.CO, RS.MI, GV.RR | Art. 46, 48, 50  | IR plan, playbooks, exercises, incident records       |

---

# 9. Core Principle

The purpose of framework mapping is not simply to attach a framework code to a risk.

The objective is to create traceability:

```text
RISK
  ↓
FRAMEWORK
  ↓
CONTROL
  ↓
IMPLEMENTATION
  ↓
EVIDENCE
  ↓
TESTING
  ↓
DECISION
```

Cyber GRC becomes more useful when governance requirements can be traced to actual controls and evidence.
