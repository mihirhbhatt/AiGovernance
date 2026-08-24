class ConformityPackGenerator:
    def __init__(self, meta, risk_summary, technical_summary, oversight_controls, data_controls, conformity_items):
        self.meta = meta
        self.risk_summary = risk_summary
        self.technical_summary = technical_summary
        self.oversight_controls = oversight_controls
        self.data_controls = data_controls
        self.conformity_items = conformity_items

    def _make_table(self, title, rows):
        text = f"### {title}\n\n| Item | Details |\n| :--- | :--- |\n"
        for row in rows:
            text += f"| {row[0]} | {row[1]} |\n"
        return text + "\n"

    def generate_risk_management(self):
        m = self.meta
        doc = f"# AI System Risk Management Summary\n\n"
        doc += f"**System:** {m['system_name']} ({m['system_id']})\n"
        doc += f"**Organisation:** {m['org_name']}\n"
        doc += f"**Assessment Date:** {m['assessment_date']}\n"
        doc += f"**Classification:** {m['classification']}\n\n"
        doc += "---\n\n"
        doc += "## Risk Summary\n\n"
        doc += self._make_table("Residual risk areas", self.risk_summary)
        doc += "## Risk Treatment\n\n"
        doc += "- Risks are treated through documented controls, monitoring, and escalation pathways.\n"
        doc += "- High residual risk items require executive approval before continued deployment.\n"
        doc += "- Periodic review will confirm whether residual risk remains within policy boundaries.\n\n"
        return doc

    def generate_technical_documentation(self):
        m = self.meta
        doc = f"# Technical Documentation\n\n"
        doc += f"**System:** {m['system_name']}\n"
        doc += f"**Provider:** {m['provider']}\n"
        doc += f"**Owner:** {m['owner']}\n\n"
        doc += self._make_table("System characteristics", self.technical_summary)
        doc += "## Validation and Testing\n\n"
        doc += "- Backtesting results reviewed against candidate quality and fairness metrics.\n"
        doc += "- Thresholds and acceptance criteria documented and approved before deployment.\n"
        doc += "- Monitoring plans include drift, output quality, and adverse incidents.\n\n"
        return doc

    def generate_human_oversight(self):
        doc = "# Human Oversight Plan\n\n"
        doc += "## Scope\n\n"
        doc += "The system supports recruiting decisions but does not replace human decision-making. Recruitment decisions remain the responsibility of the hiring team and Human Resources.\n\n"
        doc += self._make_table("Oversight controls", self.oversight_controls)
        doc += "## Governance Expectations\n\n"
        doc += "- Human intervention is mandatory for final candidate disposition decisions.\n"
        doc += "- Overrides must be logged, reviewed, and used to improve system performance.\n"
        return doc

    def generate_data_governance(self):
        doc = "# Data Governance Plan\n\n"
        doc += self._make_table("Data governance controls", self.data_controls)
        doc += "## Additional Requirements\n\n"
        doc += "- Data quality metrics must be reviewed before each retraining cycle.\n"
        doc += "- Data provenance, consent, and lawful use notices must be retained.\n"
        doc += "- Sensitive personal data must be protected through policy, access control, and minimum necessary use.\n\n"
        return doc

    def generate_conformity_summary(self):
        m = self.meta
        doc = f"# Conformity Summary\n\n"
        doc += f"**System:** {m['system_name']} ({m['system_id']})\n"
        doc += f"**Organisation:** {m['org_name']}\n"
        doc += f"**Review Cycle:** {m['review_cycle']}\n\n"
        doc += "## Required Evidence\n\n"
        for item in self.conformity_items:
            doc += f"- {item}\n"
        doc += "\n"
        doc += "## Conformity Position\n\n"
        doc += "The system has formal governance documentation, risk control frameworks, and oversight mechanisms in place. Ongoing monitoring and periodic reviews are required to maintain conformity and to demonstrate compliance with the organisation's broader governance commitments.\n"
        return doc

    def generate(self):
        return {
            "risk_management": self.generate_risk_management(),
            "technical": self.generate_technical_documentation(),
            "oversight": self.generate_human_oversight(),
            "data": self.generate_data_governance(),
            "summary": self.generate_conformity_summary(),
        }
