def decide_workflow(data, issues):
    explanation = []

    # Fast-track rule
    try:
        amount = int(data["claim_amount"].replace(",", ""))
    except:
        amount = 99999  # Force manual

    if issues:
        explanation.append("Issues found → Sent to manual review.")
        return "manual_review", explanation

    if amount < 10000:
        explanation.append("Amount < 10000 → Fast-track approved.")
        return "fast_track", explanation

    explanation.append("Normal claim with no issues → Standard processing.")
    return "standard_processing", explanation
