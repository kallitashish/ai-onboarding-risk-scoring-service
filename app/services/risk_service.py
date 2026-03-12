from app.utils.scoring_logic import calculate_score, make_decision


def evaluate_risk(request):
    score = calculate_score(
        request.device_risk,
        request.ip_risk,
        request.document_valid
    )

    decision = make_decision(score)
    explanation = []

    if request.device_risk > 0.5:
        explanation.append("high device risk")

    if request.ip_risk > 0.5:
        explanation.append("high IP risk")

    if not request.document_valid:
        explanation.append("invalid document")

    return {
        "risk_score": score,
        "decision": decision,
        "explanation": explanation
    }