from typing import List, Optional

from pydantic import BaseModel, Field

from modules.FlightPlot import FlightPlot

from modules.Preidction import Prediction


class FlightTrack(BaseModel):
    id: int = Field(..., alias="ID", serialization_alias="trackID")
    plots: List[FlightPlot] = Field(..., alias="Plots", serialization_alias="plots")
    anomaly: Optional[Prediction] = Field(None, alias="Anomaly", serialization_alias="anomaly")
