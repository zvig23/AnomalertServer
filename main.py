from fastapi import FastAPI
from typing import List
import uvicorn

from FlightDB import FlightDB
from modules.FlightPlot import FlightPlot
from modules.FlightTrack import FlightTrack
from modules.ModelIO import AIInput
from modules.Preidction import Prediction
from requests import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["http://localhost:3000"] for security
    allow_credentials=True,
    allow_methods=["*"],  # or specific methods like ["GET"]
    allow_headers=["*"],
)
db = FlightDB("data/db.json")

anomaly_threshold = 0.5

@app.get("/get_flights_plots", response_model=List[FlightPlot])
def get_flights_plots():
    plots: List[FlightPlot] = db.get_flight_plots()
    for plot in plots:
        track: FlightTrack = db.get_flight_track_by_id(plot.trackID)
        prediction: Prediction = predict(AIInput(input=track)).output
        plot.hasAnomaly = prediction.proba > anomaly_threshold
    return plots

@app.get("/get_track_info/{track_id}", response_model=FlightTrack)
def get_track_info(track_id: int):
    track : FlightTrack = db.get_flight_track_by_id(track_id)
    prediction : Prediction = predict(AIInput(input=track)).output
    track.anomaly = prediction
    return track


if __name__ == "__main__":
    # Use this for debugging purposes only
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")