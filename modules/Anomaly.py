from typing import List

from pydantic import BaseModel

from modules.Waypoint import Waypoint


class Anomaly(BaseModel):
    anomaly: List[Waypoint]
    reason: str
    id: int