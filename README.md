📘 Autonomous Insurance Claims Processing Agent (Lite Version)

A simple, modular Python-based agent that extracts key fields from FNOL documents, validates missing or inconsistent information, and determines workflow routing (fast-track, manual review, or standard processing).

🚀 Project Overview

Insurance companies receive a First Notice of Loss (FNOL) when a customer reports an incident.
This project simulates an autonomous claim-processing agent that can:

Extract structured fields from an FNOL document

Validate the extracted details

Identify missing or inconsistent information

Decide the routing workflow

Generate an explanation for the decision

This project was developed as part of the Synapx Junior Software Engineer assessment.

🧩 Key Features

✔ Extracts FNOL data using regex
✔ Validates field completeness & consistency
✔ Applies simple rule-based workflow logic
✔ Generates clean JSON output
✔ Modular, beginner-friendly Python code
✔ Easy to extend with ML or APIs

📂 Project Structure
fnol_claims_processing_agent/
│
├── main.py               # Main script that runs the entire agent
├── extractor.py          # Extract key fields from FNOL text file
├── validator.py          # Validate missing and inconsistent fields
├── workflow.py           # Workflow decision logic
├── sample_fnol.txt       # Sample FNOL document used for testing
└── output.json           # Auto-generated output from main.py

▶️ How to Run the Project
1️⃣ Install Python

Download from: https://www.python.org/downloads/

2️⃣ Clone the Repository
git clone https://github.com/bharathibonam/fnol-claims-processing-agent.git
cd fnol-claims-processing-agent

3️⃣ Run the Script
python main.py

4️⃣ View the Output

A file named output.json will be created.

📝 Sample FNOL Document

The FNOL includes:

Policy number

Policyholder details

Incident date & location

Claim type

Vehicle info

Description

Estimated claim amount

⚙️ How It Works
1. extractor.py

Extracts text using regular expressions.

2. validator.py

Checks for:

Missing fields

Invalid values

Inconsistencies

3. workflow.py

Decides:

manual_review → if issues

fast_track → if amount < 10,000

standard_processing → otherwise

🔮 Possible Enhancements

Add OCR to read PDFs

Use ML for risk prediction

Build API using FastAPI

Add UI with Streamlit

👤 Author

Bharathi Bonam
Python Developer • SQL • Problem Solving • Aspiring Software Engineer

🎉 Thank you for reviewing this project!
