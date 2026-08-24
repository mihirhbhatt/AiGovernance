class IncidentResponseGenerator:
    def __init__(self, meta, timeline, actions, rca_questions):
        self.meta = meta
        self.timeline = timeline
        self.actions = actions
        self.rca_questions = rca_questions

    def _build_table(self, title, rows):
        output = f"### {title}\n\n| Item | Responsible Party | Timeline |\n| :--- | :--- | :--- |\n"
        for row in rows:
            output += f"| {row[0]} | {row[1]} | {row[2]} |\n"
        return output + "\n"

    def generate_plan(self):
        m = self.meta
        doc = f"# AI Incident Response Plan\n\n"
        doc += f"**Incident ID:** {m['incident_id']}\n"
        doc += f"**Organisation:** {m['org_name']}\n"
        doc += f"**System:** {m['system_name']}\n"
        doc += f"**Severity:** {m['severity']}\n"
        doc += f"**Date Detected:** {m['date_detected']}\n"
        doc += f"**Incident Owner:** {m['owner']}\n"
        doc += f"**Current Status:** {m['status']}\n\n"
        doc += "---\n\n"
        doc += "## 1. Overview\n\n"
        doc += "This incident involved a material degradation in the quality and reliability of an AI-powered customer advisory system. The system was temporarily restricted after a spike in user complaints and an unexpected shift in recommendation patterns.\n\n"
        doc += "## 2. Incident Timeline\n\n"
        for item in self.timeline:
            doc += f"- **{item[0]}** — {item[1]}\n"
        doc += "\n"
        doc += "## 3. Immediate Containment Actions\n\n"
        doc += self._build_table("Urgent response actions", self.actions)
        doc += "## 4. Escalation Path\n\n"
        doc += "- AI Governance Office\n"
        doc += "- Chief Risk Officer\n"
        doc += "- Chief Compliance Officer\n"
        doc += "- Data Protection Officer and Legal\n"
        doc += "- Board Risk Committee if impact is sustained or material consumer harm is confirmed\n\n"
        doc += "## 5. Regulatory Follow-up\n\n"
        doc += "A regulator-facing summary will be prepared if it is determined that the error created customer detriment, unfair treatment, or a material failure in the governance control environment.\n\n"
        return doc

    def generate_rca(self):
        doc = "# Root-Cause Analysis Template\n\n"
        doc += "## 1. Context\n\n"
        doc += "Summarise the incident, timeline, affected users, and the business process impacted.\n\n"
        doc += "## 2. Event Description\n\n"
        doc += "Describe the actual failure, the detection signal, and the operational impact.\n\n"
        doc += "## 3. Human and Technical Findings\n\n"
        doc += "- What technical issue occurred?\n"
        doc += "- What control should have detected the issue?\n"
        doc += "- What were the decision-making gaps?\n\n"
        doc += "## 4. Questions to Answer\n\n"
        for q in self.rca_questions:
            doc += f"- {q}\n"
        doc += "\n"
        doc += "## 5. Corrective Actions\n\n"
        doc += "- Implement stronger model monitoring thresholds\n"
        doc += "- Require peer-review of model configuration changes\n"
        doc += "- Update escalation and escalation timing policies\n"
        doc += "- Re-test fairness, explainability, and output quality before reinstatement\n\n"
        doc += "## 6. Executive Summary\n\n"
        doc += "Provide a concise statement on whether the system can return to operation, under what conditions, and what governance changes are required before reinstatement.\n"
        return doc

    def generate(self):
        return {
            "plan": self.generate_plan(),
            "rca": self.generate_rca(),
        }
