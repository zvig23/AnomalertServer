from typing import List

from pydantic import BaseModel, Field


class Waypoint(BaseModel):
    lat: float = Field(alias="Lat", serialization_alias="lat")
    lon: float = Field(alias="Lon", serialization_alias="lon")
    alt: float = Field(alias="Alt", serialization_alias="alt")


def createWaypointList(data: List[dict[str:float]]) -> List[Waypoint]:
    return [Waypoint(**raw_waypoint) for raw_waypoint in data]
