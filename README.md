📘 Autonomous Insurance Claims Processing Agent (Lite Version)

A lightweight, modular Python-based FNOL (First Notice of Loss) processing agent built as part of the Synapx Junior Software Developer Assessment (Assessment 1 & 2).

This project demonstrates how insurance claims can be automatically extracted, validated, and routed using clear business rules with human-readable explanations.

🚀 Project Overview

When an insurance incident occurs, companies receive a First Notice of Loss (FNOL).
Manually reviewing these claims is slow and error-prone.

This project simulates an autonomous claims processing agent that:

Extracts key structured fields from FNOL input

Identifies missing or inconsistent information

Classifies and routes claims into the correct workflow

Explains why a specific routing decision was made

The focus is on clarity, logic, and clean code rather than over-engineering.

✨ Key Features

✔ Extracts important FNOL fields
✔ Validates mandatory data
✔ Detects suspicious claim descriptions
✔ Applies rule-based workflow routing
✔ Generates clean, structured JSON output
✔ Simple, readable, beginner-friendly Python code

🧩 Processing Flow

The system follows a clear pipeline:

Extraction
Parses FNOL data and extracts policy, incident, asset, and claim details.

Validation
Checks for missing or inconsistent mandatory fields.

Routing Logic
Determines the correct workflow based on business rules.

Decision Explanation
Produces a short, human-readable explanation for each decision.

🚦 Routing Logic (Business Rules)

Routing is applied in the following priority order:

Investigation Flag
If the description contains suspicious keywords such as
fraud, inconsistent, or staged.

Specialist Queue
If the claim type involves injury.

Manual Review
If any mandatory fields are missing or inconsistent.

Fast-track
If the estimated damage is below 25,000 and no issues are found.

Default
Claims that do not qualify for fast-track are routed to manual review.

📤 Output Format

The final decision is generated in the following JSON structure:

{
  "extractedFields": {},
  "missingFields": [],
  "recommendedRoute": "",
  "reasoning": ""
}


This makes the output:

Easy to understand

Easy to integrate with downstream systems

Transparent in decision-making

🤖 AI Tools Usage

AI tools were used to:

Assist with structuring extraction and validation logic

Improve routing clarity

Generate concise, human-readable explanations

The emphasis was on clarity over complexity, as required by the assessment.

▶️ How to Run the Project

Navigate to the project directory:

cd fnol_claims_agent


Run the application:

python main.py


View the generated output:

output.json

📂 Project Structure
fnol_claims_agent/
│
├── main.py        # Entry point
├── extractor.py   # FNOL field extraction
├── validator.py   # Validation logic
├── workflow.py    # Routing decision logic
├── output.json    # Generated output
└── README.md      # Project documentation

🧠 What This Project Demonstrates

Strong problem breakdown

Clear business logic implementation

Clean and modular Python code

Practical use of AI-assisted development

Real-world insurance domain understanding

👤 Author

Bharathi Bonam
Aspiring Software Engineer
Python • SQL • Problem Solving • Data & Logic-Driven Development

🎯 Final Note

This is a lightweight implementation designed to showcase:

Logical thinking

Clean engineering practices

Explainable decision-making

Clarity was intentionally prioritized over complexity.
