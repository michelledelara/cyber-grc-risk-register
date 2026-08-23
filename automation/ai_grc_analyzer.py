#!/usr/bin/env python3
"""
AI-Assisted GRC Analyzer

Educational portfolio project for Cyber GRC.

This script:
1. Reads synthetic AWS security findings from JSON.
2. Performs deterministic pre-classification.
3. Assigns a priority score and review category.
4. Detects privacy / IAM / monitoring / resilience indicators.
5. Generates an AI review prompt for each finding.
6. Keeps human validation mandatory.

Important:
- This is not a legal-compliance engine.
- This does not call an external AI model.
- The generated AI prompt is designed for future LLM integration.
"""

import json
import sys
import textwrap
from pathlib import Path
from datetime import datetime, timezone

SEVERITY_WEIGHT = {
    "CRITICAL": 5,
    "HIGH": 4,
    "MEDIUM": 3,
    "LOW": 2,
    "INFORMATIONAL": 1,
}

KEYWORD_RULES = {
    "identity_access": [
        "iam", "permission", "privilege", "mfa", "credential",
        "authentication", "identity", "access"
    ],
    "data_privacy": [
        "personal data", "customer data", "sensitive data", "privacy",
        "classification", "public access", "exposure"
    ],
    "logging_monitoring": [
        "cloudtrail", "logging", "monitoring", "audit", "security hub",
        "alert", "finding"
    ],
    "configuration": [
        "aws config", "configuration", "drift", "baseline", "non-compliant"
    ],
    "resilience_recovery": [
        "backup", "restore", "recovery", "ransomware", "availability"
    ],
    "third_party": [
        "third-party", "third party", "vendor", "external provider"
    ],
    "incident_response": [
        "incident response", "incident", "containment", "escalation",
        "playbook", "evidence preservation"
    ],
}


def combined_text(finding):
    parts = [
        finding.get("title", ""),
        finding.get("description", ""),
        finding.get("finding_type", ""),
        finding.get("business_context", ""),
        " ".join(finding.get("evidence", [])),
        " ".join(finding.get("recommended_actions", [])),
    ]
    return " ".join(parts).lower()


def detect_domains(text):
    detected = []
    for domain, keywords in KEYWORD_RULES.items():
        if any(keyword in text for keyword in keywords):
            detected.append(domain)
    return detected or ["general_cybersecurity"]


def calculate_priority(finding, domains):
    severity = finding.get("severity", "MEDIUM").upper()
    score = SEVERITY_WEIGHT.get(severity, 3)

    if "data_privacy" in domains:
        score += 1
    if "identity_access" in domains and severity in {"CRITICAL", "HIGH"}:
        score += 1
    if "incident_response" in domains and severity == "CRITICAL":
        score += 1

    score = min(score, 7)

    if score >= 7:
        label = "P1 - Immediate"
    elif score >= 5:
        label = "P2 - High"
    elif score >= 3:
        label = "P3 - Medium"
    else:
        label = "P4 - Low"

    return score, label


def build_ai_prompt(finding, domains, priority_label):
    nist = ", ".join(finding.get("nist_csf_2_0", [])) or "Not provided"
    lgpd = ", ".join(finding.get("lgpd_reference", [])) or "Not provided"

    return textwrap.dedent(f"""
    You are supporting a Cyber GRC analyst.

    Analyze the synthetic security finding below using only the information supplied.
    Do not invent facts, legal conclusions, AWS configurations, or control evidence.

    Finding ID: {finding.get("finding_id")}
    Title: {finding.get("title")}
    Severity: {finding.get("severity")}
    Resource: {finding.get("resource_type")} / {finding.get("resource_id")}
    Business context: {finding.get("business_context")}
    Current NIST CSF 2.0 mapping: {nist}
    Current LGPD references: {lgpd}
    Automated domains: {", ".join(domains)}
    Automated priority: {priority_label}

    Tasks:
    1. Summarize the business risk in no more than 3 sentences.
    2. Review whether the current NIST CSF mapping is plausible based only on the supplied finding.
    3. Identify the proposed control objectives.
    4. List evidence that a human analyst should request to validate control implementation.
    5. Identify any assumptions or missing information.
    6. State explicitly whether privacy/legal review may be required.
    7. Do not state that the organization is compliant or non-compliant with LGPD.

    Return a concise structured response.
    """).strip()


def analyze_finding(finding):
    text = combined_text(finding)
    domains = detect_domains(text)
    priority_score, priority_label = calculate_priority(finding, domains)

    privacy_review = "data_privacy" in domains or bool(finding.get("lgpd_reference"))

    return {
        "finding_id": finding.get("finding_id"),
        "mapped_risk_id": finding.get("mapped_risk_id"),
        "severity": finding.get("severity"),
        "automated_priority_score": priority_score,
        "automated_priority": priority_label,
        "detected_grc_domains": domains,
        "privacy_review_recommended": privacy_review,
        "nist_csf_2_0": finding.get("nist_csf_2_0", []),
        "lgpd_reference": finding.get("lgpd_reference", []),
        "recommended_actions": finding.get("recommended_actions", []),
        "ai_review_prompt": build_ai_prompt(finding, domains, priority_label),
        "human_validation_required": True,
        "automation_note": (
            "Priority and domain tags are rule-based pre-classification. "
            "They are decision-support outputs and require human validation."
        ),
    }


def main(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        source = json.load(f)

    findings = source.get("findings", [])
    results = [analyze_finding(item) for item in findings]

    summary = {
        "total_findings": len(results),
        "priority_distribution": {},
        "privacy_review_count": sum(
            1 for item in results if item["privacy_review_recommended"]
        ),
    }

    for item in results:
        label = item["automated_priority"]
        summary["priority_distribution"][label] = (
            summary["priority_distribution"].get(label, 0) + 1
        )

    payload = {
        "project": "Cyber GRC Risk Register",
        "analysis_type": "AI-ready rule-based GRC pre-classification",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": source.get("data_type", "synthetic_security_findings"),
        "disclaimer": (
            "Educational portfolio output. Automated classifications do not replace "
            "security, privacy, legal, compliance, or risk-management judgment."
        ),
        "summary": summary,
        "analysis": results,
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"Analyzed {len(results)} findings.")
    print(f"Output written to: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_file = Path(sys.argv[1])
        output_file = Path(sys.argv[2])
    else:
        input_file = Path("findings/sample-findings.json")
        output_file = Path("analysis/ai-assisted-analysis.json")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    main(input_file, output_file)
