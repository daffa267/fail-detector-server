from pydantic import BaseModel

class SensorData(BaseModel):
    type: float
    air_temperature: float
    process_temperature: float
    rotational_speed: float
    torque: float
    tool_wear: float