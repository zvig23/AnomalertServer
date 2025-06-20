from pydantic import BaseModel, Field


class Speed(BaseModel):
    value: float = Field(alias="Value")
    units: str = Field(alias="Units")

