from fastapi import APIRouter
from app.schemas.sensor import SensorData
from app.services.detector import predict_machine_status

router = APIRouter()

@router.post("/predict")
def predict_anomaly(data: SensorData):
    hasil = predict_machine_status(data.model_dump())
    return hasil
    