from app.core.config import settings


def calculate_score(device_risk, ip_risk, document_valid):
    score = (device_risk + ip_risk) / 2

    if not document_valid:
        score += 0.4

    return min(score, 1.0)


def make_decision(score):
    if score < settings.risk_threshold_approve:
        return "approve"

    if score < settings.risk_threshold_review:
        return "Manual Review"

    return "reject"
