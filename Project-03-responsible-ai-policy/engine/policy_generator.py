class ResponsibleAIGenerator:
    def __init__(self, meta, principles, roles, operating_model, controls):
        self.meta = meta
        self.principles = principles
        self.roles = roles
        self.operating_model = operating_model
        self.controls = controls

    def _build_table(self, title, rows):
        output = f"### {title}\n\n| Item | Description |\n| :--- | :--- |\n"
        for row in rows:
            output += f"| {row[0]} | {row[1]} |\n"
        return output + "\n"

    def generate_policy(self):
        m = self.meta
        doc = f"# {m['policy_name']}\n\n"
        doc += f"**Organisation:** {m['org_name']}\n\n"
        doc += f"**Version:** {m['version']}\n"
        doc += f"**Effective Date:** {m['effective_date']}\n"
        doc += f"**Policy Owner:** {m['owner']}\n"
        doc += f"**Approved By:** {m['approved_by']}\n\n"
        doc += "---\n\n"
        doc += "## 1. Purpose\n\n"
        doc += f"This policy establishes the governance framework for the use of AI systems within {m['org_name']}. The purpose is to ensure that AI deployments are lawful, accountable, safe, and consistent with the organisation's risk appetite and regulatory obligations.\n\n"

        doc += "## 2. Principles\n\n"
        for i, principle in enumerate(self.principles, 1):
            doc += f"{i}. {principle}\n"
        doc += "\n"

        doc += "## 3. Permitted and Prohibited Uses\n\n"
        doc += "### Permitted\n\n"
        doc += "- AI may be used where the purpose, risk, and human oversight model are documented and approved.\n"
        doc += "- AI may support recommendations, triage, and productivity tasks if the organisation retains accountability for decisions.\n"
        doc += "- AI may be used with human review when suitable monitoring and documentation controls are in place.\n\n"
        doc += "### Prohibited\n\n"
        doc += "- Fully autonomous decisions that materially affect individuals without meaningful human review.\n"
        doc += "- Use of AI for discriminatory, manipulative, or covert profiling.\n"
        doc += "- Deployment of unassessed third-party models in regulated business processes.\n\n"

        doc += "## 4. Governance Structure\n\n"
        doc += self._build_table("Roles and Accountabilities", self.roles)

        doc += "## 5. Mandatory Control Requirements\n\n"
        for item in self.controls:
            doc += f"- {item}\n"
        doc += "\n"

        doc += "## 6. Incident Escalation and Review\n\n"
        doc += "Any material AI incident, model failure, misuse, or unexplained output quality problem must be reported to the AI Governance Office within 24 hours. The issue must be assessed for regulatory, legal, customer, and operational impact, and either remediated or suspended pending review.\n\n"

        doc += "## 7. Review and Compliance\n\n"
        doc += "The policy will be reviewed at least annually, and sooner if regulatory requirements or business use cases materially change. Compliance is monitored through control testing, internal audits, and quarterly governance reviews.\n\n"
        return doc

    def generate_operating_model(self):
        doc = "# AI Operating Model\n\n"
        doc += "## Lifecycle Governance Workflow\n\n"
        doc += self._build_table("Operating model stages", self.operating_model)
        doc += "## Decision Rules\n\n"
        doc += "- A system must not go live without documented purpose, controls, and accountable owner.\n"
        doc += "- High-impact systems require independent challenge and human oversight controls.\n"
        doc += "- If controls are not effective, use must be suspended or limited until remediation is complete.\n"
        doc += "- AI procurement must include model documentation, contractual governance rights, and escalation obligations.\n\n"
        doc += "## Governance Cadence\n\n"
        doc += "- Monthly monitoring review for production AI systems\n"
        doc += "- Quarterly governance review with executive stakeholders\n"
        doc += "- Annual policy review and update cycle\n"
        return doc

    def generate(self):
        return {
            "policy": self.generate_policy(),
            "operating_model": self.generate_operating_model(),
        }
