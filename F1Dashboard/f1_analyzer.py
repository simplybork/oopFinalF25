import os
import fastf1
import pandas as pd
import matplotlib.pyplot as plt

class F1LapAnalyzer:
    def __init__(self, year: int, gp: str, session_type: str = "Q"):
        # Store session details (year, Grand Prix name, session type)
        self.year = year
        self.gp = gp
        self.session_type = session_type

        # Ensure FastF1 cache folder exists for storing downloaded data
        os.makedirs(".fastf1cache", exist_ok=True)
        fastf1.Cache.enable_cache(".fastf1cache")

        # Initialize the FastF1 session object
        self.session = fastf1.get_session(year, gp, session_type)

    def load(self):
        """Load session data (downloads on first run; cached afterward)."""
        self.session.load()

    def compare_drivers(self, driver1: str, driver2: str) -> pd.DataFrame:
        """
        Compare average quick lap times between two drivers.

        Args:
            driver1 (str): First driver code (e.g., 'VER').
            driver2 (str): Second driver code (e.g., 'LEC').

        Returns:
            pd.DataFrame: DataFrame with drivers and their average lap times.
        """
        # Select quick laps for each driver (ignores in/out laps)
        laps1 = self.session.laps.pick_driver(driver1).pick_quicklaps()
        laps2 = self.session.laps.pick_driver(driver2).pick_quicklaps()

        # Calculate average lap times in seconds (handle empty DataFrames)
        avg1 = laps1["LapTime"].mean().total_seconds() if not laps1.empty else float("nan")
        avg2 = laps2["LapTime"].mean().total_seconds() if not laps2.empty else float("nan")

        # Return results as a summary DataFrame
        return pd.DataFrame({
            "Driver": [driver1.upper(), driver2.upper()],
            "Average Lap Time (s)": [avg1, avg2]
        })

    def plot_bar(self, df: pd.DataFrame, title: str):
        """
        Create a bar chart comparing drivers' average lap times.

        Args:
            df (pd.DataFrame): DataFrame with driver averages.
            title (str): Title for the chart.

        Returns:
            matplotlib.figure.Figure: Bar chart figure object.
        """
        fig, ax = plt.subplots(figsize=(6, 4))
        # Plot bar chart with driver names and average lap times
        ax.bar(df["Driver"], df["Average Lap Time (s)"], color=["red", "blue"])
        ax.set_title(title)
        ax.set_ylabel("Average Lap Time (s)")
        ax.grid(axis="y", linestyle="--", alpha=0.6)
        fig.tight_layout()
        return fig

    def get_driver_laps(self, driver: str) -> pd.DataFrame:
        """
        Get per-lap times (in seconds) for a driver's quick laps.

        Args:
            driver (str): Driver code (e.g., 'VER').

        Returns:
            pd.DataFrame: DataFrame with lap numbers and lap times in seconds.
        """
        # Select quick laps for the driver
        laps = self.session.laps.pick_driver(driver).pick_quicklaps()
        if laps.empty:
            # Return empty DataFrame if no laps available
            return pd.DataFrame(columns=["LapNumber", "LapTime (s)"])
        
        # Copy lap number and lap time columns
        df = laps[["LapNumber", "LapTime"]].copy()
        # Convert timedelta LapTime to seconds for easier plotting
        df["LapTime (s)"] = df["LapTime"].dt.total_seconds()
        return df[["LapNumber", "LapTime (s)"]]
