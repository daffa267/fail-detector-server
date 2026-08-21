from fastapi import APIRouter
from app.schemas.sensor import SensorData
from app.services.detector import predict_machine_status

router = APIRouter()

@router.post("/predict")
def predict_anomaly(data: SensorData):
    # Eksekusi fungsi AI dan kembalikan hasilnya
    hasil = predict_machine_status(data.model_dump()) # Gunakan .model_dump() untuk Pydantic v2
    return hasil