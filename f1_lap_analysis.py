"""
F1 Lap Time Analyzer
Author: Khushi Anumalla
Description:
    This program uses the FastF1 library to compare average qualifying lap times
    between two Formula 1 drivers. It fetches session data, processes it with
    pandas, and visualizes results using matplotlib.
"""

import os
import fastf1
import pandas as pd
import matplotlib.pyplot as plt


def compare_drivers(session, driver1, driver2):
    """
    Compares average lap times between two drivers.

    Args:
        session (fastf1.core.Session): The loaded FastF1 session object.
        driver1 (str): Three-letter driver code (e.g., 'VER', 'LEC').
        driver2 (str): Three-letter driver code.

    Returns:
        pd.DataFrame: Summary DataFrame of lap averages.
    """
    # Pick quick laps (ignores in/out laps)
    laps1 = session.laps.pick_driver(driver1).pick_quicklaps()
    laps2 = session.laps.pick_driver(driver2).pick_quicklaps()

    # Calculate average lap time in seconds
    avg1 = laps1["LapTime"].mean().total_seconds() if not laps1.empty else float("nan")
    avg2 = laps2["LapTime"].mean().total_seconds() if not laps2.empty else float("nan")

    # Return a summary table
    data = {"Driver": [driver1, driver2],
            "Average Lap Time (s)": [avg1, avg2]}

    return pd.DataFrame(data)


def plot_comparison(df, event_name):
    """
    Plots a bar chart comparing drivers' average lap times.

    Args:
        df (pd.DataFrame): DataFrame from compare_drivers()
        event_name (str): Race/session name for the title
    """
    plt.figure(figsize=(6, 4))
    plt.bar(df["Driver"], df["Average Lap Time (s)"], color=["red", "blue"])
    plt.title(f"Average Qualifying Lap Times - {event_name}")
    plt.ylabel("Average Lap Time (seconds)")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


# --- Main Execution ---
if __name__ == "__main__":
    print("🏎️  F1 Lap Time Analyzer")
    print("This demo compares two drivers in a qualifying session.\n")

    # Ensure FastF1 cache folder exists
    os.makedirs(".fastf1cache", exist_ok=True)
    fastf1.Cache.enable_cache(".fastf1cache")

    # Choose session details
    year, gp, session_type = 2024, "Monaco", "Q"
    print(f"Loading session: {year} {gp} {session_type} ...")

    session = fastf1.get_session(year, gp, session_type)
    session.load()  # Downloads data on first run; cached afterward

    # User input for driver codes
    driver1 = input("Enter first driver code (e.g., VER): ").upper()
    driver2 = input("Enter second driver code (e.g., LEC): ").upper()

    # Basic control flow for validation
    if driver1 == driver2:
        print("Drivers must be different! Please rerun and try again.")
        exit()

    # Compare and display results
    df = compare_drivers(session, driver1, driver2)
    print("\nAverage Lap Times (seconds):\n", df)

    # Plot results visually
    plot_comparison(df, f"{year} {gp} GP Qualifying")