import os
import joblib
import pandas as pd
import pygame

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
AUDIO_PATH = os.path.join(BASE_DIR, "assets", "buzzer.mp3") 

model = joblib.load(MODEL_PATH)
pygame.mixer.init()

def trigger_emergency_stop():
    if os.path.exists(AUDIO_PATH):
        pygame.mixer.music.load(AUDIO_PATH)
        pygame.mixer.music.play(loops=3)

def predict_machine_status(data: dict) -> dict:
    input_df = pd.DataFrame([data])
    prediksi = model.predict(input_df)
    
    status = int(prediksi[0]) 
    
    if status == 1:
        trigger_emergency_stop()
        pesan = "Anomali Detection!"
        print("Stop the machine!")
    else:
        pesan = "Normal"
    
    return {"status_kode": status, "pesan": pesan}