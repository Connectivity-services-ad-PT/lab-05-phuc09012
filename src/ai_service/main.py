from fastapi import FastAPI, status
import random

app = FastAPI(title="Smart Campus - AI Mock Service", version="0.1.0")

# Endpoint GET để Docker Compose check trạng thái sống chết
@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "ok", "service": "ai-service"}

# Endpoint HEAD để vượt qua bài test wait-on của GitHub Actions
@app.head("/health", status_code=status.HTTP_200_OK)
def health_check_head():
    return None

# Endpoint giả lập AI dự đoán dữ liệu
@app.post("/predict")
def predict_data(payload: dict):
    return {
        "status": "success",
        "confidence": round(random.uniform(0.75, 0.99), 2), # Random độ tin cậy từ 75% đến 99%
        "prediction": "normal_state"
    }