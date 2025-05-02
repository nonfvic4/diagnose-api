from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AnalyzeInput(BaseModel):
    patient_id: str
    face_front_url: str
    face_side_url: str
    posture_front_url: str
    posture_side_url: str
    posture_back_url: str

@app.post("/analyze")
async def analyze(input_data: AnalyzeInput):
    # 仮のJSONを返す（画像解析なし）
    return {
        "face": {
            "score": 78,
            "il_value": 33,
            "e_line": "+3mm",
            "vertical_ratio": "1:1:1.5"
        },
        "posture": {
            "score": 76,
            "cva": 46.2,
            "shoulder_diff": 1.3
        },
        "foot": {
            "score": 72,
            "left_weight": 45,
            "right_weight": 55
        }
    }
