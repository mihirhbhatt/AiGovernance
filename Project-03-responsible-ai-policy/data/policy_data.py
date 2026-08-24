POLICY_META = {
    "org_name": "Acme Financial Services",
    "policy_name": "Responsible AI Policy",
    "version": "v1.0",
    "approved_by": "Board Risk & Compliance Committee",
    "effective_date": "April 2026",
    "owner": "Chief Risk Officer"
}

PRINCIPLES = [
    "Human accountability remains with the business owner and the organisation.",
    "AI systems must be fit for purpose, transparent, and explainable in their intended use.",
    "AI must not be used to make decisions that materially affect individuals without meaningful human review.",
    "Fairness, data quality, and security are mandatory design and operating controls.",
    "AI incidents must be reported, triaged, and remediated without delay.",
    "Third-party AI vendors are subject to the same governance expectations as internal systems."
]

GOVERNANCE_ROLES = [
    ["Board Risk & Compliance Committee", "Approves policy, risk appetite, and major system use-case decisions."],
    ["Chief Risk Officer", "Owns AI governance programme, oversight cadence, and escalation decisions."],
    ["AI System Owner", "Accountable for system performance, controls, and business decisions tied to the AI output."],
    ["Data Steward", "Ensures datasets meet quality, provenance, and lawful-use requirements."],
    ["Legal & Compliance", "Reviews regulatory exposure, contracts, and disclosure obligations."],
    ["Model/AI Product Team", "Implements technical controls, monitoring, and documentation."],
    ["Ethics & Human Oversight Review Group", "Challenges high-impact decisions and reviews exceptions."],
]

OPERATING_MODEL = [
    ["1. Intake", "Business teams submit a new AI use case to the governance office for classification and risk review."],
    ["2. Assessment", "The AI team, risk, legal, and data functions assess purpose, data quality, impacts, and controls."],
    ["3. Approval", "The System Owner and Chief Risk Officer approve deployment only if residual risks are acceptable."],
    ["4. Monitoring", "Continuous monitoring tracks drift, error rates, fairness indicators, and operational incidents."],
    ["5. Review", "Quarterly governance review confirms the system remains in scope and within risk appetite."],
    ["6. Retirement", "Decommissioning or redesign is required if the system no longer meets control standards."],
]

CONTROL_REQUIREMENTS = [
    "Mandatory human review for any high-impact decision affecting credit, employment, healthcare, or eligibility.",
    "Documentation of model purpose, limitations, validation results, and data sources before use in production.",
    "Bias and fairness assessment for systems with material impacts on individuals or groups.",
    "Logging and monitoring of model outputs, overrides, and exceptions.",
    "Vendor due diligence including AI risk clauses, documentation, and incident reporting obligations.",
    "Clear user communication where AI contributes materially to decisions or recommendations."
]
