from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Smart Campus — IoT Ingestion API",
    version="0.5.0",
    description="API chính gọi qua gọi lại trong Docker Compose"
)

class ReadingRequest(BaseModel):
    device_id: str = Field(..., min_length=3, examples=["ESP32-LAB-A01"])
    metric: str = Field("temperature", examples=["temperature"])
    value: float = Field(..., ge=-40.0, le=80.0, examples=[31.5])
    unit: str = Field("celsius", examples=["celsius"])
    timestamp: str = Field(..., examples=["2026-05-13T08:30:00+07:00"])

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "ok", "service": "iot-ingestion"}

@app.head("/health", status_code=status.HTTP_200_OK)
def health_check_head():
    return None

@app.post("/readings", status_code=status.HTTP_200_OK)
def create_reading(payload: ReadingRequest):
    return {
        "status": "success",
        "message": "Data ingested successfully via Docker Compose",
        "data": {
            "device_id": payload.device_id,
            "metric": payload.metric,
            "value": payload.value
        }
    }