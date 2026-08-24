INCIDENT_META = {
    "org_name": "Acme Financial Services",
    "incident_id": "AI-INC-2026-014",
    "system_name": "Customer Advisory AI",
    "date_detected": "April 2026",
    "severity": "High",
    "owner": "Chief Risk Officer",
    "status": "Contained; investigation ongoing"
}

INCIDENT_TIMELINE = [
    ["T-0: 09:10", "Model monitoring identifies a sharp rise in customer complaints and anomaly in output distribution."],
    ["T+0:30", "AI Governance Office opens an incident and requests immediate temporary suspension of the assistant's decision-support mode."],
    ["T+1:00", "Legal and compliance teams are notified due to potential consumer detriment and disclosure obligations."],
    ["T+2:00", "Customer service leadership pauses publication of the model's recommendations to human agents."],
    ["T+4:00", "Data science team reviews alerting data, logs, and upstream training set drift."],
    ["T+8:00", "Root-cause analysis confirms a configuration change introduced an overly aggressive recommendation strategy."],
    ["T+24:00", "Board notification and regulator-facing status briefing prepared."],
]

RCA_QUESTIONS = [
    "What was the triggering event and how was it detected?",
    "Who owned the decision to continue use after the anomaly alert?",
    "Which control failed and why did escalation not occur earlier?",
    "What customer harm or legal exposure has been identified?",
    "What corrective actions are required to prevent recurrence?"
]

IMMEDIATE_ACTIONS = [
    ["Suspend decision-support mode", "AI System Owner + Engineering", "Immediate"],
    ["Notify legal and compliance", "Chief Compliance Officer", "Immediate"],
    ["Preserve logs and model artefacts", "Data Steward + Security", "Within 24 hours"],
    ["Customer communications review", "Customer Experience Team", "Within 48 hours"],
    ["Independent RCA", "Chief Risk Officer + Internal Audit", "Within 5 business days"],
]
