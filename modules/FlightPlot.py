from typing import Optional

from pydantic import BaseModel, Field

from modules.Angle import Angle
from modules.Speed import Speed
from modules.Waypoint import Waypoint


class FlightPlot(BaseModel):
    trackID: int = Field(alias="ID", serialization_alias="trackID")
    waypoint: Waypoint = Field(alias="waypoint")
    current_speed: Speed = Field(alias="CurrentSpeed", serialization_alias="currentSpeed")
    heading: Angle = Field(alias="Heading", serialization_alias="heading")
    hasAnomaly: Optional[bool] = Field(None, alias="hasAnomaly")
