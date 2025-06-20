from typing import List
from pydantic import BaseModel

from modules import FlightTrack, Waypoint


class AIInput(BaseModel):
    input: FlightTrack


class AIOutput(BaseModel):
    output: List[Waypoint]