from extractor import extract_fields
from validator import validate_data
from workflow import decide_workflow
import json

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def main():
    text = read_file("sample_fnol.txt")

    extracted = extract_fields(text)
    issues = validate_data(extracted)
    workflow, explanation = decide_workflow(extracted, issues)

    result = {
        "extracted_data": extracted,
        "validation_issues": issues,
        "workflow_decision": workflow,
        "explanation": explanation
    }

    with open("output.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Processing complete. Check output.json")

if __name__ == "__main__":
    main()
