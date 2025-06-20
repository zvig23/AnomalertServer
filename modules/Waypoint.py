from pydantic import BaseModel, Field


class Waypoint(BaseModel):
    lat: float = Field(alias="Lat")
    lon: float = Field(alias="Lon")
    alt: float = Field(alias="Alt")
