import os

from data.policy_data import POLICY_META, PRINCIPLES, GOVERNANCE_ROLES, OPERATING_MODEL, CONTROL_REQUIREMENTS
from engine.policy_generator import ResponsibleAIGenerator


def main():
    output_dir = "exports"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    generator = ResponsibleAIGenerator(
        POLICY_META,
        PRINCIPLES,
        GOVERNANCE_ROLES,
        OPERATING_MODEL,
        CONTROL_REQUIREMENTS,
    )

    documents = generator.generate()

    policy_path = os.path.join(output_dir, "responsible-ai-policy.md")
    operating_path = os.path.join(output_dir, "operating-model.md")

    with open(policy_path, "w", encoding="utf-8") as f:
        f.write(documents["policy"])

    with open(operating_path, "w", encoding="utf-8") as f:
        f.write(documents["operating_model"])

    print(f"Generated {policy_path} and {operating_path}")


if __name__ == "__main__":
    main()
