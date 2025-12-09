# oopFinalF25

<!--
README.md for F1 Lap Time Analyzer
-->

# F1 Lap Time Analyzer

<!-- A lightweight Formula 1 analytics tool built with FastF1, pandas, and matplotlib.  
This script compares two drivers’ average qualifying lap times using real F1 telemetry data. >

## Overview

<! F1 Lap Time Analyzer pulls official Formula 1 session data via the FastF1 API, processes it with pandas, and visualizes the results using matplotlib. This is an example of how data analytics and visualization can be applied to motorsport performance analysis. >

<! Pandas is a Python library for organizing, analyzing, and manipulating data. It’s used to handle tables of information (like spreadsheets) — cleaning data, calculating statistics, and preparing it for visualization.>

<! Matplotlib is a Python library for creating graphs and charts. It helps turn data into visual insights, such as bar charts or line graphs, making patterns and comparisons easy to see.>



### Key Features
<!-- 
- Real-time F1 data retrieval using FastF1
- Data cleaning and aggregation with pandas
- Visual storytelling through matplotlib
-->

## Example Usage

```bash
$ python f1_lap_analysis.py
F1 Lap Time Analyzer
# This demo compares two drivers in a qualifying session.
# A bar chart will appear showing both drivers’ average lap times.

## Installation
#F1 Lap Time Analyzer requires Python 3.9+ and an internet connection (FastF1 downloads session data on first run).
```bash
# Create and activate a virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

##Run Instructions
python f1_lap_analysis.py


## Future Work
# Planned extensions include:
# - Sector-by-sector split and best-lap delta analysis
# - Tyre compound tracking and stint pace evolution
# - Interactive dashboards using Plotly or Streamlit
# - Multi-race performance trend comparisons




# About

# F1 Lap Time Analyzer
# Developed by Khushi Anumalla; Rutgers University
# 2025 Khushi Anumalla · For educational use only

# Topics
# python • data-analytics • formula-1 • fastf1 • pandas • matplotlib • motorsport-data