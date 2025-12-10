import re

def extract_fields(text):
    data = {}

    patterns = {
        "policy_number": r"Policy Number:\s*(.*)",
        "name": r"Policyholder Name:\s*(.*)",
        "contact": r"Contact Number:\s*(.*)",
        "email": r"Email:\s*(.*)",
        "incident_date": r"Date of Incident:\s*(.*)",
        "incident_time": r"Time of Incident:\s*(.*)",
        "location": r"Location of Incident:\s*(.*)",
        "claim_type": r"Type of Claim:\s*(.*)",
        "vehicle_model": r"Make & Model:\s*(.*)",
        "vehicle_number": r"Registration Number:\s*(.*)",
        "year": r"Year of Manufacture:\s*(.*)",
        "description": r"Description of Incident:\s*([\s\S]*?)Estimated",
        "claim_amount": r"Estimated Claim Amount:\s*(.*) INR",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            data[key] = match.group(1).strip()
        else:
            data[key] = None

    return data
