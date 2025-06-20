from typing import Optional

from pydantic import BaseModel, Field

from modules.Angle import Angle
from modules.Speed import Speed
from modules.Waypoint import Waypoint


class FlightPlot(BaseModel):
    id: int = Field(alias="ID")
    waypoint: Waypoint = Field(alias="waypoint")
    current_speed: Speed = Field(alias="CurrentSpeed")
    heading: Angle = Field(alias="Heading")
    hasAnomaly: Optional[bool] = Field(None, alias="hasAnomaly")
