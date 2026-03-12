from pydantic import BaseModel


class RiskRequest(BaseModel):
    customer_id: str
    country: str
    document_valid: bool
    device_risk: float
    ip_risk: float


class RiskResponse(BaseModel):
    risk_score: float
    decisions: str
    explanation: list[str]