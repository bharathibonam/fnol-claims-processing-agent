def validate_data(data):
    issues = []

    # Missing fields
    for field, value in data.items():
        if not value:
            issues.append(f"Missing value for: {field}")

    # Basic Inconsistency checks
    if data["claim_type"] == "Motor Accident" and not data["vehicle_number"]:
        issues.append("Vehicle number missing for motor claim")

    try:
        amount = int(data["claim_amount"].replace(",", ""))
        if amount <= 0:
            issues.append("Invalid claim amount")
    except:
        issues.append("Claim amount not readable")

    return issues
