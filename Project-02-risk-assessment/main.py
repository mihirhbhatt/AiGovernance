# main.py
import os
from data.talentmatch_audit import AUDIT_METADATA, REMEDIATION_PLAN
from engine.report_generator import MemoGenerator

def run_audit():
    # 1. Initialize
    output_dir = "exports"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 2. Run Engine
    generator = MemoGenerator(AUDIT_METADATA, REMEDIATION_PLAN)
    memo_content = generator.generate()

    # 3. Save to file (UTF-8 to support emojis/special characters)
    file_name = "risk-assessment.md"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(memo_content)

    if not memo_content or not memo_content.strip():
        raise RuntimeError(f"No content generated for {file_path}.")

    print(f"🚀 Success: {file_path} created with risk assessment content.")

if __name__ == "__main__":
    run_audit()

