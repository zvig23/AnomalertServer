import json
from pathlib import Path
from typing import List, Dict, Any

from modules.FlightPlot import FlightPlot
from modules.Waypoint import Waypoint


class FlightDB:
    _instance = None

    def __new__(cls, path: str = "db.json"):
        if cls._instance is None:
            cls._instance = super(FlightDB, cls).__new__(cls)
            cls._instance._load_data(path)
        return cls._instance

    def _load_data(self, path: str):
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        with open(file_path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        self.db: List[Dict[str, Any]] = raw.get("DB", [])

    def get_all_flights(self) -> List[Dict[str, Any]]:
        return self.db

    def get_flight_plots(self) -> list[FlightPlot]:
        plots: List[FlightPlot] = []
        for record in self.db:
            waypoint = (record["Waypoints"][-1])
            record["waypoint"] = Waypoint(**waypoint)
            plots.append(FlightPlot(**record))

        return plots

    def get_flight_by_id(self, flight_id: int) -> Dict[str, Any] | None:
        return next((f for f in self.db if f["ID"] == flight_id), None)
