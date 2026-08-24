import os

from data.document_pack import (
    DOCUMENT_META,
    RISK_MANAGEMENT_SUMMARY,
    TECHNICAL_SUMMARY,
    HUMAN_OVERSIGHT_CONTROLS,
    DATA_GOVERNANCE_CONTROLS,
    CONFORMITY_ITEMS,
)
from engine.document_pack_generator import ConformityPackGenerator


def main():
    output_dir = "exports"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    generator = ConformityPackGenerator(
        DOCUMENT_META,
        RISK_MANAGEMENT_SUMMARY,
        TECHNICAL_SUMMARY,
        HUMAN_OVERSIGHT_CONTROLS,
        DATA_GOVERNANCE_CONTROLS,
        CONFORMITY_ITEMS,
    )

    docs = generator.generate()

    files = {
        "ai-system-risk-management.md": docs["risk_management"],
        "technical-documentation.md": docs["technical"],
        "human-oversight-plan.md": docs["oversight"],
        "data-governance-plan.md": docs["data"],
        "conformity-summary.md": docs["summary"],
    }

    for file_name, content in files.items():
        path = os.path.join(output_dir, file_name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {path}")


if __name__ == "__main__":
    main()
