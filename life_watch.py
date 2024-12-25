import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from sidebar import sidebar_inputs  # Import the sidebar module

# Function to calculate time fractions
def get_time_fractions():
    now = time.localtime()
    
    # Year progress
    day_of_year = now.tm_yday
    total_days_in_year = 366 if now.tm_year % 4 == 0 else 365
    year_fraction = day_of_year / total_days_in_year
    
    # Month progress
    day_of_month = now.tm_mday
    days_in_month = {
        1: 31, 2: 29 if now.tm_year % 4 == 0 else 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    month_fraction = day_of_month / days_in_month[now.tm_mon]
    
    # Day progress
    hour_fraction = now.tm_hour / 24
    day_fraction = hour_fraction
    
    # Hour and minute progress
    minute_fraction = now.tm_min / 60
    second_fraction = now.tm_sec / 60
    
    return year_fraction, month_fraction, day_fraction, minute_fraction, second_fraction

# Function to draw the life watch
def plot_life_watch(year_fraction, month_fraction, day_fraction, hour_fraction, minute_fraction):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')

    # Draw the clock background
    for i in range(12):
        angle = 2 * np.pi * i / 12
        x, y = np.sin(angle), np.cos(angle)
        ax.text(
            x * 1.1, y * 1.1, str(i * 5), 
            ha='center', va='center', fontsize=12
        )

    # Year needle (outermost)
    theta_year = 2 * np.pi * (1 - year_fraction)
    ax.plot([0, 0.8 * np.sin(theta_year)], [0, 0.8 * np.cos(theta_year)], color='red', lw=2, label="Year Progress")
    
    # Month needle
    theta_month = 2 * np.pi * (1 - month_fraction)
    ax.plot([0, 0.6 * np.sin(theta_month)], [0, 0.6 * np.cos(theta_month)], color='blue', lw=2, label="Month Progress")
    
    # Day needle
    theta_day = 2 * np.pi * (1 - day_fraction)
    ax.plot([0, 0.4 * np.sin(theta_day)], [0, 0.4 * np.cos(theta_day)], color='green', lw=2, label="Day Progress")

    # Minute needle
    theta_minute = 2 * np.pi * (1 - minute_fraction)
    ax.plot([0, 0.2 * np.sin(theta_minute)], [0, 0.2 * np.cos(theta_minute)], color='purple', lw=2, label="Minute Progress")
    
    # Add a legend
    ax.legend(loc="upper right", fontsize=10)
    
    return fig

# Main application
st.title('Life Watch: Real-Time Day, Month, and Year Progress')

# Get inputs from the sidebar
expected_lifespan, current_age = sidebar_inputs()

if st.button('Start Life Watch'):
    remaining_years = expected_lifespan - current_age
    st.write(f"You have lived {current_age} years.")
    st.write(f"You have {remaining_years} years remaining.")

    # Placeholder for the watch
    watch_placeholder = st.empty()

    # Real-time updates
    while True:
        # Get time fractions
        year_fraction, month_fraction, day_fraction, minute_fraction, _ = get_time_fractions()

        # Plot the watch
        fig = plot_life_watch(year_fraction, month_fraction, day_fraction, minute_fraction, _)

        # Update the Streamlit placeholder
        watch_placeholder.pyplot(fig)

        # Reduce CPU usage
        time.sleep(1)
