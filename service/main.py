from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

app = FastAPI()

# ---------- MODELS FOR REQUESTS ----------

class PredictRequest(BaseModel):
    x: float

class DriftRequest(BaseModel):
    ref: list
    current: list

# ---------- ENDPOINTS ----------

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: PredictRequest):
    # simple mock model: multiply by 2
    prediction = req.x * 2
    return {"prediction": prediction}

@app.post("/drift")
def drift(req: DriftRequest):
    df_ref = pd.DataFrame({"x": req.ref})
    df_current = pd.DataFrame({"x": req.current})

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=df_ref, current_data=df_current)

    result = report.as_dict()
    return result
