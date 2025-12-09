import streamlit as st
import matplotlib.pyplot as plt
from f1_analyzer import F1LapAnalyzer

# Configure the Streamlit page with title, icon, and layout
st.set_page_config(page_title="F1 Lap Time Dashboard", page_icon="🏎️", layout="centered")
st.title("🏎️ F1 Lap Time Dashboard")

# Sidebar inputs for session settings
with st.sidebar:
    st.header("Session settings")
    # Year input (numeric range from 2018 to 2025)
    year = st.number_input("Year", min_value=2018, max_value=2025, value=2024, step=1)
    # Grand Prix name input (string)
    gp = st.text_input("Grand Prix (e.g., Monaco, Bahrain, Italy)", value="Monaco")
    # Session type selector (Qualifying, Race, Practice sessions)
    session_type = st.selectbox("Session Type", ["Q", "R", "FP1", "FP2", "FP3"])

# Driver codes input (converted to uppercase for consistency)
driver1 = st.text_input("Driver 1 (code like VER, LEC, HAM)", value="VER").upper()
driver2 = st.text_input("Driver 2 (code like VER, LEC, HAM)", value="LEC").upper()

# Button to trigger analysis
if st.button("Load session and compare"):
    try:
        # Initialize analyzer with selected session details
        analyzer = F1LapAnalyzer(year, gp, session_type)
        with st.spinner("Loading session data..."):
            analyzer.load()  # Load session data (downloads if not cached)

        # Compare drivers and display average lap times
        df = analyzer.compare_drivers(driver1, driver2)
        st.subheader("Average lap times")
        st.dataframe(df, use_container_width=True)  # Show results in a table

        # Plot bar chart of average lap times
        fig = analyzer.plot_bar(df, f"{year} {gp} {session_type} • Average Quick Lap Times")
        st.pyplot(fig)

        # Show per-lap times for each driver side by side
        st.subheader("Per-lap times (quick laps)")
        col1, col2 = st.columns(2)
        with col1:
            laps1 = analyzer.get_driver_laps(driver1)
            st.caption(f"{driver1} per-lap times")
            st.line_chart(laps1.set_index("LapNumber")["LapTime (s)"])  # Line chart of lap times
        with col2:
            laps2 = analyzer.get_driver_laps(driver2)
            st.caption(f"{driver2} per-lap times")
            st.line_chart(laps2.set_index("LapNumber")["LapTime (s)"])

        # Button to download average lap times as CSV
        st.download_button(
            label="Download averages as CSV",
            data=df.to_csv(index=False),
            file_name=f"{year}_{gp}_{session_type}_averages.csv",
            mime="text/csv",
        )

    except Exception as e:
        # Error handling if session fails to load or process
        st.error(f"Failed to load or process session: {e}")
        st.info("Check the Grand Prix spelling and that the session exists for the selected year.")
