from pydantic import BaseModel

from modules.FlightTrack import FlightTrack
from modules.Preidction import Prediction


class AIInput(BaseModel):
    input: FlightTrack


class AIOutput(BaseModel):
    output: Prediction
