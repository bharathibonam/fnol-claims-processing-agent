def decide_workflow(data, issues):
    explanation = []

    description = data.get("description", "").lower()
    claim_type = data.get("claim_type", "").lower()

    try:
        amount = int(data.get("claim_amount", "0").replace(",", ""))
    except:
        amount = 99999

    # 1️⃣ Investigation Flag
    if any(word in description for word in ["fraud", "inconsistent", "staged"]):
        explanation.append("Suspicious keywords found in claim description.")
        return "investigation_flag", explanation

    # 2️⃣ Specialist Queue
    if claim_type == "injury":
        explanation.append("Injury-related claim requires specialist handling.")
        return "specialist_queue", explanation

    # 3️⃣ Manual Review
    if issues:
        explanation.append("Mandatory fields missing or inconsistent.")
        return "manual_review", explanation

    # 4️⃣ Fast-track
    if amount < 25000:
        explanation.append("Estimated damage below 25,000 → Fast-track.")
        return "fast_track", explanation

    # Default
    explanation.append("Claim requires manual review.")
    return "manual_review", explanation
