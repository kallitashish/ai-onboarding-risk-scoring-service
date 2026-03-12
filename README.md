**AI Customer Onboarding – Risk Scoring Microservice**

<img width="3358" height="722" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/01e319a1-aa37-4912-bec2-5babc67c1c15" />

**Overview**
This project demonstrates a microservice responsible for calculating onboarding risk scores in an AI-enabled customer onboarding platform.

The service evaluates risk using:
    rule-based scoring    
    explainable decision logic    
    configurable risk thresholds

It is implemented using:
    FastAPI
    Python 3.10+

The architecture is designed so that the scoring logic can later be extended with machine learning models for fraud detection and risk prediction.

**Architecture Context**
In a typical onboarding platform, this service would sit between document verification and the decision engine.

**Customer Onboarding Flow**

            Customer Application
                        │
                        ▼
            Document Verification Service
                        │
                        ▼
            Risk Scoring Service (this project)
                        │
                        ▼
            Decision Engine
                        │
                 ┌──────┴───────────┐
                 ▼                  ▼
            Auto Approve     Manual Review

The service produces:
    risk score
    onboarding decision
    explanation for auditability

**Project Structure**

  <img width="343" height="405" alt="project-structure" src="https://github.com/user-attachments/assets/43e5d2df-6ac4-48af-9333-656dbea0920b" />



**Architecture follows a layered microservice design**:
        API Layer → Service Layer → Domain Logic

**Running the Service**
        1. Install dependencies
        pip install -r requirements.txt
        2. Start the application
                uvicorn app.main:app --reload
        3. Access API documentation
                FastAPI automatically generates API documentation.
                http://localhost:8000/docs

**API Endpoints**
  Health Check
  GET /health
            Response
            
                    {
                    "status": "service healthy"
                    }
   Risk Scoring
   POST /risk/score

 **Sample Request**

                {
                    "customer_id": "12345",
                    "country": "IN",
                    "document_valid": true,
                    "device_risk": 0.2,
                    "ip_risk": 0.4
                }

  **Sample Response**

            {
                "risk_score": 0.3,
                "decision": "manual_review",
                "explanation": []
            }
The service includes structured request logging with unique request identifiers.
Configuration is managed using environment-based settings.
