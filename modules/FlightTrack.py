from typing import List, Optional

from pydantic import BaseModel, Field

from modules.Waypoint import Waypoint

from modules.Anomaly import Anomaly


class FlightTrack(BaseModel):
    id: int = Field(..., alias="ID")
    waypoints: List[Waypoint] = Field(..., alias="WP")
    Anomaly: Optional[Anomaly] = Field(None, alias="Anomaly")
