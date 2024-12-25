import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from sidebar import sidebar_inputs  # Import the sidebar module

# Function to calculate real-time fractions for day, hours, minutes, and seconds
def get_time_fractions():
    now = time.localtime()  # Get the current local time
    seconds_fraction = now.tm_sec / 60
    minutes_fraction = (now.tm_min + seconds_fraction) / 60
    hours_fraction = (now.tm_hour + minutes_fraction) / 24
    day_fraction = hours_fraction
    return seconds_fraction, minutes_fraction, hours_fraction, day_fraction

# Function to create the life watch
def plot_life_watch(expected_lifespan, current_age, real_time_fraction):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')

    # Create the watch face
    ax.add_artist(plt.Circle((0, 0), 1, color='#f0f0f0', ec='black'))

    # Add ticks for each year (outer ring)
    for year in range(expected_lifespan):
        angle = 2 * np.pi * (1 - (year / expected_lifespan))  # Counterclockwise rotation
        x_outer = 0.9 * np.cos(angle)
        y_outer = 0.9 * np.sin(angle)
        x_inner = 0.8 * np.cos(angle)
        y_inner = 0.8 * np.sin(angle)
        ax.plot([x_inner, x_outer], [y_inner, y_outer], color='black', lw=1)

        # Add labels for intervals (e.g., every 5 years)
        if year % 5 == 0 or year == 0:
            x_label = 0.7 * np.cos(angle)
            y_label = 0.7 * np.sin(angle)
            ax.text(
                x_label,
                y_label,
                str(year),
                ha='center',
                va='center',
                fontsize=10,
                color='black',
            )

    # Add the year needle
    year_angle = 2 * np.pi * (1 - real_time_fraction)  # Counterclockwise rotation
    ax.plot([0, 0.7 * np.cos(year_angle)], [0, 0.7 * np.sin(year_angle)], color='red', lw=3)

    # Add the day progress (inner ring)
    day_fraction = get_time_fractions()[-1]
    day_angle = 2 * np.pi * (1 - day_fraction)
    ax.plot([0, 0.5 * np.cos(day_angle)], [0, 0.5 * np.sin(day_angle)], color='blue', lw=2)

    # Add ticks for hours, minutes, and seconds (like a clock face)
    for hour in range(12):
        angle = 2 * np.pi * (1 - hour / 12)  # Counterclockwise rotation
        x_outer = 0.6 * np.cos(angle)
        y_outer = 0.6 * np.sin(angle)
        x_inner = 0.55 * np.cos(angle)
        y_inner = 0.55 * np.sin(angle)
        ax.plot([x_inner, x_outer], [y_inner, y_outer], color='black', lw=1)

    # Real-time second, minute, and hour needles
    seconds_fraction, minutes_fraction, hours_fraction, _ = get_time_fractions()

    second_angle = 2 * np.pi * (1 - seconds_fraction)
    minute_angle = 2 * np.pi * (1 - minutes_fraction)
    hour_angle = 2 * np.pi * (1 - hours_fraction)

    # Second needle
    ax.plot([0, 0.4 * np.cos(second_angle)], [0, 0.4 * np.sin(second_angle)], color='green', lw=1)

    # Minute needle
    ax.plot([0, 0.3 * np.cos(minute_angle)], [0, 0.3 * np.sin(minute_angle)], color='orange', lw=2)

    # Hour needle
    ax.plot([0, 0.2 * np.cos(hour_angle)], [0, 0.2 * np.sin(hour_angle)], color='purple', lw=3)

    # Add center dot
    ax.plot(0, 0, 'o', color='black')

    # Set axis limits and remove ticks
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.axis('off')  # Hide axis

    return fig

# Main application
st.title('Real-Time Life Watch')

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
        # Calculate the real-time fraction of the current year
        current_time = time.time()  # Current time in seconds since epoch
        seconds_per_year = 365.25 * 24 * 60 * 60
        total_seconds_lived = current_age * seconds_per_year
        current_year_fraction = (current_time % seconds_per_year) / seconds_per_year

        # Calculate the needle position based on total life progress
        total_progress_fraction = (current_age + current_year_fraction) / expected_lifespan

        # Plot the life watch
        fig = plot_life_watch(expected_lifespan, current_age, total_progress_fraction)

        # Update the placeholder with the new plot
        watch_placeholder.pyplot(fig)

        # Sleep for a short duration to reduce CPU usage
        time.sleep(1)
