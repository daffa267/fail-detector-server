from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Mesin Anomaly API")

# Mengizinkan Frontend (Next.js) berkomunikasi dengan Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Memuat model AI
model = joblib.load('model.pkl')

# Menentukan struktur data yang akan diterima dari web
class SensorData(BaseModel):
    type: float
    air_temperature: float
    process_temperature: float
    rotational_speed: float
    torque: float
    tool_wear: float

@app.post("/predict")
def predict_anomaly(data: SensorData):
    # Mengubah data JSON menjadi DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Melakukan prediksi
    prediksi = model.predict(input_df)
    
    # Menentukan hasil
    status = int(prediksi[0]) 
    pesan = "Anomali Terdeteksi!" if status == 1 else "Mesin Normal"
    
    return {"status_kode": status, "pesan": pesan}