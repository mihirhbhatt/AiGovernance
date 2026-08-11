import pandas as pd
import os
from datetime import datetime
from data.inventory import ACME_INVENTORY

class GovernanceEngine:
    def __init__(self, data):
        self.data = data
        if not os.path.exists("exports"):
            os.makedirs("exports")

    def export_csv(self):
        """Creates a queryable spreadsheet of all systems."""
        df = pd.DataFrame(self.data)
        df['nist_avg'] = df['scores'].apply(lambda x: sum(x.values())/4)
        df.to_csv("exports/ai-system-inventory.csv", index=False, encoding="utf-8")
        print("✅ Exported CSV Inventory.")

    def export_classification(self):
        """Creates the detailed Legal/EU AI Act report."""
        with open("exports/eu-ai-act-classification.md", "w", encoding="utf-8") as f:
            f.write("# EU AI Act Risk Classification — Acme Financial Services\n")
            f.write(f"**Classification Date:** {datetime.now().strftime('%B %Y')} | **Review Due:** September 2026\n\n")
            
            f.write("## 1. Classification Framework\n")
            f.write("| Tier | Regulatory Treatment |\n| :--- | :--- |\n")
            f.write("| **High Risk** | Strict pre-deployment obligations. Conformity assessment required. |\n")
            f.write("| **Limited Risk** | Transparency obligations (Art 52). |\n")
            f.write("| **Minimal Risk** | No specific AI Act obligations. |\n\n")

            f.write("## 2. Classification Decisions\n\n")
            for sys in self.data:
                f.write(f"### {sys['id']} · {sys['name']}\n")
                f.write(f"**Classification:** {sys['tier'].upper()}\n\n")
                f.write(f"**Legal Basis:** {sys['legal_basis']}\n\n")
                f.write(f"**Rationale:** {sys['rationale']}\n\n")
                
                f.write("**Obligations Triggered:**\n")
                if sys['tier'] == "High-Risk":
                    f.write("- Conformity assessment (Art 43), Tech Doc (Art 11), Logging (Art 12), Oversight (Art 14)\n")
                elif sys['tier'] == "Limited Risk" or sys['tier'] == "GPAI":
                    f.write("- Transparency & AI disclosure to end users (Art 52/53)\n")
                else:
                    f.write("- General GDPR and internal policy monitoring.\n")
                
                f.write(f"\n**Current compliance gap:** {sys['gaps']}\n\n---\n\n")

            f.write("## 3. Summary Table\n\n| ID | System | Classification | Status | Priority |\n| :--- | :--- | :--- | :--- | :--- |\n")
            for s in self.data:
                f.write(f"| {s['id']} | {s['name']} | {s['tier']} | {s['status']} | {s['priority']} |\n")
        print("✅ Exported Classification Report.")

    def export_nist_gap(self):
        """Creates the technical NIST RMF maturity report."""
        with open("exports/nist-rmf-mapping.md", "w", encoding="utf-8") as f:
            f.write("# NIST AI RMF Gap Analysis\n\n")
            for sys in self.data:
                avg = sum(sys['scores'].values())/4
                status = "🟢 COMPLIANT" if avg >= 3 else "🔴 GAP"
                f.write(f"## {sys['id']} - {sys['name']} [{status}]\n")
                f.write(f"| GOVERN | MAP | MEASURE | MANAGE |\n| :---: | :---: | :---: | :---: |\n")
                s = sys['scores']
                f.write(f"| {s['gov']} | {s['map']} | {s['mea']} | {s['man']} |\n\n")
        print("✅ Exported NIST Gap Analysis.")

    def export_dashboard(self):
        """Creates the high-level summary for Executives."""
        total = len(self.data)
        high_risk = len([s for s in self.data if s['tier'] == "High-Risk"])
        with open("exports/governance-dashboard.md", "w", encoding="utf-8") as f:
            f.write("# 📊 ACME AI Executive Dashboard\n\n")
            f.write(f"- **Total Systems:** {total}\n")
            f.write(f"- **High-Risk Systems:** {high_risk}\n")
            f.write("## 🚩 Critical Remediation Items\n")
            for s in self.data:
                if s['priority'] == "Critical":
                    f.write(f"- [{s['id']}] {s['name']}: {s['gaps']}\n")
        print("✅ Exported Executive Dashboard.")

if __name__ == "__main__":
    
    engine = GovernanceEngine(ACME_INVENTORY)
    
    
    engine.export_csv()
    engine.export_classification()
    engine.export_nist_gap()
    engine.export_dashboard()
    
    print(f"\n🚀 Success! All 4 governance reports are ready in the /exports/ folder.")