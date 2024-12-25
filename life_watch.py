import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from sidebar import sidebar_inputs  # Import sidebar inputs
import matplotlib.animation as animation

# Function to calculate time fractions for year, month, day, and minute
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

# Optimized function to draw the life watch with animation
def plot_life_watch(year_fraction, month_fraction, hour_fraction, minute_fraction, ax):
    ax.clear()  # Clear previous plots

    ax.set_aspect('equal')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')

    # Draw the clock outline once
    circle = plt.Circle((0, 0), 1, color='black', fill=False, lw=2)
    ax.add_artist(circle)

    # Draw clock numbers (12, 3, 6, 9)
    for i in range(12):
        angle = np.pi / 2 - i * np.pi / 6
        x, y = 0.9 * np.cos(angle), 0.9 * np.sin(angle)
        ax.text(x, y, str(i if i != 0 else 12), ha='center', va='center', fontsize=14, fontweight='bold')

    # Draw ticks for seconds and minutes only
    for i in range(60):
        angle = np.pi / 2 - i * np.pi / 30
        x1, y1 = np.cos(angle), np.sin(angle)
        x2, y2 = 0.95 * x1, 0.95 * y1
        ax.plot([x1, x2], [y1, y2], color='black', lw=0.5)

    # Plot hands for year, month, day, and minute progress
    ax.plot([0, 0.6 * np.cos(np.pi / 2 - 2 * np.pi * year_fraction)], 
            [0, 0.6 * np.sin(np.pi / 2 - 2 * np.pi * year_fraction)], 
            color='red', lw=3, label='Year Progress')

    ax.plot([0, 0.5 * np.cos(np.pi / 2 - 2 * np.pi * month_fraction)], 
            [0, 0.5 * np.sin(np.pi / 2 - 2 * np.pi * month_fraction)], 
            color='blue', lw=3, label='Month Progress')

    ax.plot([0, 0.4 * np.cos(np.pi / 2 - 2 * np.pi * hour_fraction)], 
            [0, 0.4 * np.sin(np.pi / 2 - 2 * np.pi * hour_fraction)], 
            color='green', lw=3, label='Day Progress')

    ax.plot([0, 0.3 * np.cos(np.pi / 2 - 2 * np.pi * minute_fraction)], 
            [0, 0.3 * np.sin(np.pi / 2 - 2 * np.pi * minute_fraction)], 
            color='purple', lw=3, label='Minute Progress')

    # Add legend to explain colors
    ax.legend(loc="upper right", fontsize=10)

# Main application logic
st.title('Life Watch: Real-Time Day, Month, and Year Progress')

# Get inputs from the sidebar
expected_lifespan, current_age = sidebar_inputs()

# Show life statistics
remaining_years = expected_lifespan - current_age
st.write(f"You have lived {current_age} years.")
st.write(f"You have {remaining_years} years remaining.")

# Add a button to start the Life Watch
if st.button('Start Life Watch'):
    # Placeholder for the watch
    watch_placeholder = st.empty()

    # Create figure and axis for animation
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Create an animation function
    def update(frame):
        # Get time fractions
        year_fraction, month_fraction, hour_fraction, minute_fraction = get_time_fractions()

        # Update the life watch plot
        plot_life_watch(year_fraction, month_fraction, hour_fraction, minute_fraction, ax)
        
    # Create the animation
    ani = animation.FuncAnimation(fig, update, interval=60000)  # Update every 60 seconds (minute)

    # Display the animated plot in Streamlit
    watch_placeholder.pyplot(fig)

    # Wait for the animation to continue
    plt.show()
