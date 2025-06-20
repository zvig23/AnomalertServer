from pydantic import BaseModel, Field


class Angle(BaseModel):
    value: float = Field(alias="Value")
    units: str = Field(alias="Units")
