class MemoGenerator:
    def __init__(self, meta, plan):
        self.meta = meta
        self.plan = plan

    def generate(self):
        m = self.meta
        p = self.plan
        
        doc = f"# Governance Review Memo\n\n"
        doc += f"**To:** Chief Executive Officer · Board Risk & Audit Committee\n"
        doc += f"**From:** {m['prepared_by']}\n"
        doc += f"**Subject:** {m['system_name']} — Governance Review and Deployment Decision\n"
        doc += f"**Classification:** Confidential\n"
        doc += f"**Date:** {m['assessment_date']}\n\n---\n\n"

        doc += "## Purpose\n\n"
        doc += f"This memo presents the outcome of a governance review of {m['system_name']} ({m['system_id']}), {m['org_name']}'s AI-assisted recruitment tool. "
        doc += f"The review was triggered by the EU AI Act classification exercise completed in February 2026, which identified this system as high-risk with no conformity assessment in place.\n\n"
        
        doc += "--- \n\n## Executive Summary\n\n"
        doc += f"{m['system_name']} has been in production since November 2023. The review has identified that the system is operating in material non-compliance with the EU AI Act. Specifically:\n\n"
        doc += "- No conformity assessment has been performed (Annex III requirement)\n"
        doc += "- Candidate rejections are communicated without mandatory human review (Art 14 violation)\n"
        doc += "- No independent bias audit has been conducted\n"
        doc += f"- Vendor documentation from {m['provider']} has not been obtained\n\n"
        doc += "**The recommended Board decision is: continue operation under strictly enhanced human oversight (90-day remediation), or suspend use until remediation is complete.**\n\n"

        doc += "--- \n\n## Findings in Detail\n\n"
        doc += "### 1. Classification and Regulatory Exposure\n"
        doc += f"{m['system_name']} is classified as high-risk under EU AI Act Annex III, Category 4(a). The system directly influences employment outcomes without the structures the Act requires.\n\n"
        
        doc += "### 2. The Autonomous Rejection Problem\n"
        doc += "AI-generated shortlists are currently used to send automated rejection emails without human review. This is a material employment law risk and an Art 14 compliance failure.\n\n"
        
        doc += "### 3. Bias Risk — Unknown, Therefore Unacceptable\n"
        doc += f"We do not currently know whether {m['system_name']} exhibits discriminatory behavior. {m['provider']} has not supplied training data documentation.\n\n"

        doc += "## Recommended Actions\n\n"
        
        # Helper to build table
        def build_table(title, rows):
            t = f"### {title}\n\n| Action | Owner | Timeline |\n|--------|-------|---------|\n"
            for row in rows:
                t += f"| {row[0]} | {row[1]} | {row[2]} |\n"
            return t + "\n"

        doc += build_table("Immediate (before next hiring cycle)", p['immediate'])
        doc += build_table("Within 60 Days", p['sixty_day'])
        doc += build_table("Within 90 Days", p['ninety_day'])

        doc += "## Decision Requested\n\n"
        doc += "**Option A — Continue with enhanced oversight (Recommended)**\n"
        doc += "Permit operation subject to mandatory human review controls and a 90-day remediation roadmap.\n\n"
        doc += "**Option B — Suspend pending remediation**\n"
        doc += "Suspend use until conformity assessment is complete. Revert to manual CV screening.\n\n"
        
        doc += f"**The AI Governance Programme Office recommends Option A.**\n\n"
        
        doc += "--- \n\n## Escalation if Controls Not Implemented\n"
        doc += "If immediate controls are not implemented within two weeks, the Office will recommend immediate suspension to the Chief Compliance Officer.\n\n"
        
        doc += f"---\n\n*Attachments: AI Risk Assessment — {m['system_name']} ({m['assessment_date']})*\n\n"
        doc += f"*Prepared by: {m['prepared_by']}*\n"
        doc += f"*Contact: [{m['contact_email']}]*"
        
        return doc