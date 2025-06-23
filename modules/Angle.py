from pydantic import BaseModel, Field


class Angle(BaseModel):
    value: float = Field(alias="Value", serialization_alias="value")
    units: str = Field(alias="Units",serialization_alias="units"   )
