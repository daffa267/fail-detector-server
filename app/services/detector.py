import pandas as pd
import joblib
import os

# Memastikan path model terbaca dari mana pun server dijalankan
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")

# Load model di awal agar ringan
model = joblib.load(MODEL_PATH)

def predict_machine_status(data: dict) -> dict:
    input_df = pd.DataFrame([data])
    prediksi = model.predict(input_df)
    
    status = int(prediksi[0]) 
    pesan = "Anomali Terdeteksi!" if status == 1 else "Mesin Normal"
    
    return {"status_kode": status, "pesan": pesan}