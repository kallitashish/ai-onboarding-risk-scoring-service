from fastapi import FastAPI
from app.api.risk_routes import router
from app.core.logging import log_requests

app = FastAPI(
            title="AI Onboarding Risk Scoring Service",
            version="1.0"
)


app.include_router(router)
app.middleware("http")(log_requests)


@app.get("/health")
def health():
    return {"status": "service healthy"}