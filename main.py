from fastapi import FastAPI
from typing import List
import uvicorn

from FlightDB import FlightDB
from modules.FlightPlot import FlightPlot

# FastAPI app
app = FastAPI()
db = FlightDB("data/db.json")


@app.get("/get_flights_plots", response_model=List[FlightPlot])
def get_flights_plots():
    return db.get_flight_plots()

# @app.get("/Get_track_info", response_model=FlightTrack)
# def get_track_info(id: int):
#     for flight in flights_db:
#         if flight.id == id:
#             return flight
#     raise HTTPException(status_code=404, detail="Track not found")

if __name__ == "__main__":
    # Use this for debugging purposes only
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")