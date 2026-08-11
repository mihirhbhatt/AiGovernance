# EU AI Act Risk Classification — Acme Financial Services
**Classification Date:** August 2026 | **Review Due:** September 2026

## 1. Classification Framework
| Tier | Regulatory Treatment |
| :--- | :--- |
| **High Risk** | Strict pre-deployment obligations. Conformity assessment required. |
| **Limited Risk** | Transparency obligations (Art 52). |
| **Minimal Risk** | No specific AI Act obligations. |

## 2. Classification Decisions

### ACM-AI-001 · CreditScore Pro
**Classification:** HIGH-RISK

**Legal Basis:** Annex III, Category 5(b)

**Rationale:** Directly determines creditworthiness of natural persons for retail loans. Outputs carry significant financial consequences for individuals.

**Obligations Triggered:**
- Conformity assessment (Art 43), Tech Doc (Art 11), Logging (Art 12), Oversight (Art 14)

**Current compliance gap:** Explainability (SHAP) implemented but not documented to Article 13 standards. Conformity assessment pending.

---

### ACM-AI-002 · FraudGuard 360
**Classification:** LIMITED RISK

**Legal Basis:** Not listed in Annex III

**Rationale:** Flags suspicious transactions for human review. Human-in-the-loop (HITL) prevents autonomous legal effects on users.

**Obligations Triggered:**
- Transparency & AI disclosure to end users (Art 52/53)

**Current compliance gap:** Vendor contract (FraudTech) lacks AI Act specific compliance clauses.

---

### ACM-AI-003 · TalentMatch AI
**Classification:** HIGH-RISK

**Legal Basis:** Annex III, Category 4(a)

**Rationale:** Used for CV screening and candidate shortlisting. Directly impacts employment opportunities and carries high bias risk.

**Obligations Triggered:**
- Conformity assessment (Art 43), Tech Doc (Art 11), Logging (Art 12), Oversight (Art 14)

**Current compliance gap:** No conformity assessment, no documented bias audit, and no registration in the EU AI database.

---

### ACM-AI-004 · SupportBot Aria
**Classification:** LIMITED RISK

**Legal Basis:** Article 52(1) Transparency

**Rationale:** Conversational AI interacting with natural persons. Requires clear disclosure to users that they are not speaking to a human.

**Obligations Triggered:**
- Transparency & AI disclosure to end users (Art 52/53)

**Current compliance gap:** Mobile app implementation lacks the 'AI Assistant' disclosure banner.

---

### ACM-AI-005 · MarketPersonaliser
**Classification:** MINIMAL RISK

**Legal Basis:** Not listed in Annex III

**Rationale:** Surfaces product recommendations based on browsing. Customer retains full agency to accept or ignore offers.

**Obligations Triggered:**
- General GDPR and internal policy monitoring.

**Current compliance gap:** None identified under AI Act. GDPR profiling notices are active.

---

### ACM-AI-006 · DocIntel Underwriting
**Classification:** HIGH-RISK

**Legal Basis:** Annex III, Category 5(c)

**Rationale:** Extracts data for health/life insurance risk assessment. Accuracy errors could lead to wrongful denial of coverage.

**Obligations Triggered:**
- Conformity assessment (Art 43), Tech Doc (Art 11), Logging (Art 12), Oversight (Art 14)

**Current compliance gap:** Still in Pilot phase. Requires a Fundamental Rights Impact Assessment (FRIA) before production.

---

### ACM-AI-007 · RegulatoryRadar
**Classification:** MINIMAL RISK

**Legal Basis:** Internal Use Only

**Rationale:** Processes public legal texts for internal intelligence. No interaction with or impact on natural persons.

**Obligations Triggered:**
- General GDPR and internal policy monitoring.

**Current compliance gap:** None. System provides informational support to trained compliance staff.

---

### ACM-AI-008 · FaceID Onboard
**Classification:** HIGH-RISK

**Legal Basis:** Annex III, Category 1(a)

**Rationale:** Remote biometric identification for KYC. Carries risk of exclusion based on demographic bias in liveness detection.

**Obligations Triggered:**
- Conformity assessment (Art 43), Tech Doc (Art 11), Logging (Art 12), Oversight (Art 14)

**Current compliance gap:** Documented bias testing for diverse skin tones needs quarterly updates.

---

### ACM-AI-009 · AML-Sentry
**Classification:** LIMITED RISK

**Legal Basis:** AMLD6 / Art 52 Disclosure

**Rationale:** Monitors transactions for money laundering. Regulated under AML laws; transparency obligations apply under AI Act.

**Obligations Triggered:**
- Transparency & AI disclosure to end users (Art 52/53)

**Current compliance gap:** Requires clearer human-oversight logging to demonstrate HITL compliance.

---

### ACM-AI-010 · StaffPulse
**Classification:** HIGH-RISK

**Legal Basis:** Annex III, Category 4(b)

**Rationale:** Monitors employee behavior to predict burnout/churn. High risk of infringing on worker privacy and rights.

**Obligations Triggered:**
- Conformity assessment (Art 43), Tech Doc (Art 11), Logging (Art 12), Oversight (Art 14)

**Current compliance gap:** Deployment in EU paused pending mandatory Works Council consultation and Data Protection Impact Assessment (DPIA).

---

### ACM-AI-011 · ACME GPT
**Classification:** GPAI

**Legal Basis:** Article 53 Obligations

**Rationale:** General Purpose AI model (LLM) used for coding and summaries. Subject to systemic risk evaluation if compute thresholds met.

**Obligations Triggered:**
- Transparency & AI disclosure to end users (Art 52/53)

**Current compliance gap:** Internal usage policy exists, but technical documentation for downstream users is not finalized.

---

### ACM-AI-012 · ClaimLogic Health
**Classification:** HIGH-RISK

**Legal Basis:** Annex III, Category 5(c)

**Rationale:** Automated triage and settlement of health claims. Directly impacts access to essential medical financing.

**Obligations Triggered:**
- Conformity assessment (Art 43), Tech Doc (Art 11), Logging (Art 12), Oversight (Art 14)

**Current compliance gap:** Model drift detected in April 2024. Re-training documentation lacks quantitative robustness proof.

---

### ACM-AI-013 · TradeWatch
**Classification:** LIMITED RISK

**Legal Basis:** MiFID II Governance

**Rationale:** Monitors for wash trading and spoofing. Primarily deterministic with ML components; high degree of human oversight.

**Obligations Triggered:**
- Transparency & AI disclosure to end users (Art 52/53)

**Current compliance gap:** Alignment between MiFID II algorithmic trading logs and AI Act Article 12 logs needed.

---

### ACM-AI-014 · LimitOptimizer
**Classification:** HIGH-RISK

**Legal Basis:** Annex III, Category 5(b)

**Rationale:** Adjusts credit limits dynamically. Could exploit vulnerable customers by increasing debt during financial distress.

**Obligations Triggered:**
- Conformity assessment (Art 43), Tech Doc (Art 11), Logging (Art 12), Oversight (Art 14)

**Current compliance gap:** Fairness testing against 'financial vulnerability' metrics not yet performed.

---

### ACM-AI-015 · EcoScore
**Classification:** MINIMAL RISK

**Legal Basis:** Not listed in Annex III

**Rationale:** Scores corporate ESG reports. Does not impact natural persons; governed by CSRD/SFDR frameworks.

**Obligations Triggered:**
- General GDPR and internal policy monitoring.

**Current compliance gap:** None identified under AI Act. Data quality reviews ongoing.

---

### ACM-AI-016 · ChurnPredict
**Classification:** MINIMAL RISK

**Legal Basis:** Not listed in Annex III

**Rationale:** Predicts customer churn likelihood for internal retention strategy. No legal impact on individuals.

**Obligations Triggered:**
- General GDPR and internal policy monitoring.

**Current compliance gap:** GDPR Right to Object (Article 21) handling is manual; needs automation.

---

### ACM-AI-017 · SmartVault Bio
**Classification:** HIGH-RISK

**Legal Basis:** Annex III, Category 1(a)

**Rationale:** Facial recognition for secure data center access. High risk to biometric privacy of employees.

**Obligations Triggered:**
- Conformity assessment (Art 43), Tech Doc (Art 11), Logging (Art 12), Oversight (Art 14)

**Current compliance gap:** Fundamental Rights Impact Assessment (FRIA) completed; needs annual review.

---

### ACM-AI-018 · ACME-Write
**Classification:** GPAI

**Legal Basis:** Article 52(3) / Art 53

**Rationale:** GenAI used for marketing and social content. Transparency rules for AI-generated text apply.

**Obligations Triggered:**
- Transparency & AI disclosure to end users (Art 52/53)

**Current compliance gap:** Consistent watermarking or tagging of AI-generated content not yet universal across all channels.

---

### ACM-AI-019 · DebtCollect ML
**Classification:** HIGH-RISK

**Legal Basis:** Annex III, Category 5(b)

**Rationale:** Prioritizes debtors and calculates settlement offers. Could unfairly target disadvantaged groups without oversight.

**Obligations Triggered:**
- Conformity assessment (Art 43), Tech Doc (Art 11), Logging (Art 12), Oversight (Art 14)

**Current compliance gap:** Model has a high 'Manage' gap; no formal incident response plan for biased outcomes.

---

### ACM-AI-020 · LogiSense Supply
**Classification:** MINIMAL RISK

**Legal Basis:** Not listed in Annex III

**Rationale:** Demand forecasting for hardware supplies. Operational B2B system with no impact on natural persons.

**Obligations Triggered:**
- General GDPR and internal policy monitoring.

**Current compliance gap:** None. Mature operational system.

---

## 3. Summary Table

| ID | System | Classification | Status | Priority |
| :--- | :--- | :--- | :--- | :--- |
| ACM-AI-001 | CreditScore Pro | High-Risk | Partial | Critical |
| ACM-AI-002 | FraudGuard 360 | Limited Risk | Adequate | Medium |
| ACM-AI-003 | TalentMatch AI | High-Risk | Non-compliant | Critical |
| ACM-AI-004 | SupportBot Aria | Limited Risk | Partial | Low |
| ACM-AI-005 | MarketPersonaliser | Minimal Risk | Compliant | Monitor |
| ACM-AI-006 | DocIntel Underwriting | High-Risk | Pre-production | High |
| ACM-AI-007 | RegulatoryRadar | Minimal Risk | Compliant | Monitor |
| ACM-AI-008 | FaceID Onboard | High-Risk | Partial | High |
| ACM-AI-009 | AML-Sentry | Limited Risk | Adequate | Medium |
| ACM-AI-010 | StaffPulse | High-Risk | Non-compliant | Critical |
| ACM-AI-011 | ACME GPT | GPAI | Partial | Medium |
| ACM-AI-012 | ClaimLogic Health | High-Risk | Partial | High |
| ACM-AI-013 | TradeWatch | Limited Risk | Adequate | Medium |
| ACM-AI-014 | LimitOptimizer | High-Risk | Non-compliant | High |
| ACM-AI-015 | EcoScore | Minimal Risk | Compliant | Monitor |
| ACM-AI-016 | ChurnPredict | Minimal Risk | Adequate | Low |
| ACM-AI-017 | SmartVault Bio | High-Risk | Compliant | Medium |
| ACM-AI-018 | ACME-Write | GPAI | Partial | Low |
| ACM-AI-019 | DebtCollect ML | High-Risk | Non-compliant | Critical |
| ACM-AI-020 | LogiSense Supply | Minimal Risk | Compliant | Monitor |
