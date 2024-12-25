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

    # Minute progress (update every minute)
    minute_fraction = now.tm_min / 60

    return year_fraction, month_fraction, hour_fraction, minute_fraction


# Function to draw the life watch
def plot_life_watch(year_fraction, month_fraction, hour_fraction, minute_fraction):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')

    # Draw the clock outline
    circle = plt.Circle((0, 0), 1, color='black', fill=False, lw=2)
    ax.add_artist(circle)

    # Add clock numbers (12, 3, 6, 9 as major markers)
    for i in range(12):
        angle = np.pi / 2 - i * np.pi / 6  # Adjust for clockwise rotation
        x, y = 0.9 * np.cos(angle), 0.9 * np.sin(angle)
        ax.text(x, y, str(i if i != 0 else 12), ha='center', va='center', fontsize=14, fontweight='bold')

    # Draw ticks for seconds and minutes
    for i in range(60):
        angle = np.pi / 2 - i * np.pi / 30
        x1, y1 = np.cos(angle), np.sin(angle)
        x2, y2 = 0.95 * x1, 0.95 * y1
        ax.plot([x1, x2], [y1, y2], color='black', lw=0.5)

    # Year hand (longest, outermost)
    theta_year = np.pi / 2 - 2 * np.pi * year_fraction
    ax.plot([0, 0.6 * np.cos(theta_year)], [0, 0.6 * np.sin(theta_year)], color='red', lw=3, label='Year Progress')

    # Month hand
    theta_month = np.pi / 2 - 2 * np.pi * month_fraction
    ax.plot([0, 0.5 * np.cos(theta_month)], [0, 0.5 * np.sin(theta_month)], color='blue', lw=3, label='Month Progress')

    # Day hand
    theta_day = np.pi / 2 - 2 * np.pi * hour_fraction
    ax.plot([0, 0.4 * np.cos(theta_day)], [0, 0.4 * np.sin(theta_day)], color='green', lw=3, label='Day Progress')

    # Minute hand
    theta_minute = np.pi / 2 - 2 * np.pi * minute_fraction
    ax.plot([0, 0.3 * np.cos(theta_minute)], [0, 0.3 * np.sin(theta_minute)], color='purple', lw=3, label='Minute Progress')

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
        year_fraction, month_fraction, hour_fraction, minute_fraction = get_time_fractions()

        # Plot the watch
        fig = plot_life_watch(year_fraction, month_fraction, hour_fraction, minute_fraction)

        # Update the Streamlit placeholder
        watch_placeholder.pyplot(fig)

        # Update every minute
        time.sleep(60)
