from typing import List

from pydantic import BaseModel

from modules.FlightPlot import FlightPlot


class Prediction(BaseModel):
    plots: List[FlightPlot]
    proba: float
    reason: str
    id: int
