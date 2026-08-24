import os

from data.incident_data import INCIDENT_META, INCIDENT_TIMELINE, IMMEDIATE_ACTIONS, RCA_QUESTIONS
from engine.incident_generator import IncidentResponseGenerator


def main():
    output_dir = "exports"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    generator = IncidentResponseGenerator(
        INCIDENT_META,
        INCIDENT_TIMELINE,
        IMMEDIATE_ACTIONS,
        RCA_QUESTIONS,
    )

    documents = generator.generate()

    plan_path = os.path.join(output_dir, "ai-incident-response-plan.md")
    rca_path = os.path.join(output_dir, "root-cause-analysis-template.md")

    with open(plan_path, "w", encoding="utf-8") as f:
        f.write(documents["plan"])

    with open(rca_path, "w", encoding="utf-8") as f:
        f.write(documents["rca"])

    print(f"Generated {plan_path} and {rca_path}")


if __name__ == "__main__":
    main()
