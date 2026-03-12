from pydantic_settings import  BaseSettings


class Settings(BaseSettings):
    risk_threshold_approve: float = 0.3
    risk_threshold_review: float = 0.7

    service_name: str = "Risk Scoring Service"


settings = Settings()