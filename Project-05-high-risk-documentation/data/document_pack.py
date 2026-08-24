DOCUMENT_META = {
    "org_name": "Acme Financial Services",
    "system_name": "TalentMatch AI",
    "system_id": "ACM-AI-003",
    "classification": "High-Risk under EU AI Act Annex III 4(a)",
    "owner": "Head of HR and Chief Risk Officer",
    "review_cycle": "Quarterly",
    "assessment_date": "April 2026",
    "provider": "HireFlow Technologies Ltd"
}

RISK_MANAGEMENT_SUMMARY = [
    ["Bias and exclusion risk", "Moderate; mitigated by fairness review and human oversight."],
    ["Explainability risk", "Moderate; final recommendation requires human review and justification logging."],
    ["Data quality risk", "High; controlled through provenance validation and periodic dataset review."],
    ["Operational misuse risk", "Moderate; governed by access controls and approved deployment policy."],
]

TECHNICAL_SUMMARY = [
    ["Purpose", "Assist recruiters in screening CVs and suggesting candidates for interview consideration."],
    ["Model type", "Gradient-boosted decision model with structured feature engineering."],
    ["Validation", "Backtesting, fairness analysis, and threshold review against business acceptance criteria."],
    ["Monitoring", "Drift, model error rate, and demographic parity tracking monitored on a weekly basis."],
]

HUMAN_OVERSIGHT_CONTROLS = [
    ["Decision gate", "No candidate rejection is final without HR review and documented override reason."],
    ["Override logging", "Any override is stored with rationale and reviewed monthly."],
    ["Appeal path", "Candidates may request human review of a rejected application."],
    ["Escalation", "Material anomalies are reported to the AI Governance Office within 24 hours."],
]

DATA_GOVERNANCE_CONTROLS = [
    ["Source validation", "Training data is verified against approved collection and retention rules."],
    ["Label quality", "Labels are reviewed for consistency and possible historical bias."],
    ["Lawful use", "The system is used only within permitted recruitment and selection workflows."],
    ["Retention", "Model and dataset logs retain evidence for governance review and audits."],
]

CONFORMITY_ITEMS = [
    "Risk management system documented and reviewed",
    "Technical documentation maintained for system purpose, design, and validation",
    "Human oversight controls applied to key decisions",
    "Data governance and quality controls reviewed for training and operation",
    "Monitoring and incident escalation framework in place",
    "Periodic review of performance, fairness, and residual risk"
]
