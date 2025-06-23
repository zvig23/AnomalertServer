import json
from pathlib import Path
from typing import List, Dict, Any

from modules.FlightPlot import FlightPlot
from modules.FlightTrack import FlightTrack
from modules.Waypoint import Waypoint, createWaypointList


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
            plot_record = record.copy()
            waypoint = (plot_record["Waypoints"][-1])
            plot_record["waypoint"] = Waypoint(**waypoint)
            plots.append(FlightPlot(**plot_record))
        return plots

    def get_flight_track_by_id(self, flight_id: int) -> FlightTrack | None:
        for record in self.db:
            if record["ID"] == flight_id:
                track_record = record.copy()
                track_record["Waypoints"] = createWaypointList(track_record["Waypoints"])
                track_record["Plots"] = [FlightPlot(waypoint=waypoint, **track_record) for waypoint in
                                        track_record["Waypoints"]]
                return FlightTrack(**track_record)
        return None
