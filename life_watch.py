import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from sidebar import sidebar_inputs  # Import the sidebar module

# Function to calculate real-time progress for year, month, and day
def get_time_fractions():
    now = time.localtime()
    # Year progress
    day_of_year = now.tm_yday  # Day of the year (1-365 or 366)
    total_days_in_year = 366 if now.tm_year % 4 == 0 else 365  # Check for leap year
    year_fraction = day_of_year / total_days_in_year

    # Month progress
    day_of_month = now.tm_mday  # Day of the month
    days_in_month = {
        1: 31,
        2: 29 if now.tm_year % 4 == 0 else 28,
        3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    month_fraction = day_of_month / days_in_month[now.tm_mon]

    # Day progress
    hours_fraction = now.tm_hour / 24
    day_fraction = hours_fraction

    return year_fraction, month_fraction, day_fraction

# Function to create the life watch
def plot_life_watch(year_fraction, month_fraction, day_fraction):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')

    # Draw the background circle
    ax.add_artist(plt.Circle((0, 0), 1, color='#f0f0f0', ec='black'))

    # Year progress ring (outermost ring)
    theta_year = 2 * np.pi * (1 - year_fraction)  # Counterclockwise rotation
    ax.plot(
        [0, 0.8 * np.cos(theta_year)],
        [0, 0.8 * np.sin(theta_year)],
        color='red',
        lw=3,
        label='Year Progress'
    )

    # Month progress ring (middle ring)
    theta_month = 2 * np.pi * (1 - month_fraction)
    ax.plot(
        [0, 0.6 * np.cos(theta_month)],
        [0, 0.6 * np.sin(theta_month)],
        color='blue',
        lw=3,
        label='Month Progress'
    )

    # Day progress ring (innermost ring)
    theta_day = 2 * np.pi * (1 - day_fraction)
    ax.plot(
        [0, 0.4 * np.cos(theta_day)],
        [0, 0.4 * np.sin(theta_day)],
        color='green',
        lw=3,
        label='Day Progress'
    )

    # Add labels
    ax.legend(loc='upper left', fontsize=10)
    ax.plot(0, 0, 'o', color='black')  # Center dot

    # Remove axes
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.axis('off')

    return fig

# Main application
st.title('Life Watch: Day, Month, and Year Progress')

# Get inputs from the sidebar
expected_lifespan, current_age = sidebar_inputs()

if st.button('Start Life Watch'):
    remaining_years = expected_lifespan - current_age
    st.write(f"You have lived {current_age} years.")
    st.write(f"You have {remaining_years} years remaining.")

    # Placeholder for the real-time watch
    watch_placeholder = st.empty()

    # Real-time updates
    while True:
        # Calculate the current year, month, and day fractions
        year_fraction, month_fraction, day_fraction = get_time_fractions()

        # Plot the life watch
        fig = plot_life_watch(year_fraction, month_fraction, day_fraction)

        # Update the placeholder with the new plot
        watch_placeholder.pyplot(fig)

        # Sleep for a short duration to reduce CPU usage
        time.sleep(1)
