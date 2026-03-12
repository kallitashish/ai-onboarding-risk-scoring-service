from fastapi import APIRouter
from app.models.risk_models import RiskRequest
from app.services.risk_service import evaluate_risk

router = APIRouter(prefix="/risk", tags=["Risk"])


@router.post("/score")
def score(request: RiskRequest):
    return evaluate_risk(request)
