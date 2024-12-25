import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate remaining years
def calculate_remaining_years(expected_lifespan, current_age):
    return expected_lifespan - current_age

# Function to create the life watch with detailed intervals and counterclockwise rotation
def plot_life_watch(expected_lifespan, current_age):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')

    # Create the watch face
    circle = plt.Circle((0, 0), 1, color='#f0f0f0', ec='black')
    ax.add_artist(circle)

    # Add ticks for each year and sub-marks for months/weeks
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

    # Add smaller ticks for months (or weeks) within each year
    for sub_mark in range(expected_lifespan * 12):  # Adjust granularity as needed
        sub_angle = 2 * np.pi * (1 - (sub_mark / (expected_lifespan * 12)))
        x_outer = 0.88 * np.cos(sub_angle)
        y_outer = 0.88 * np.sin(sub_angle)
        x_inner = 0.85 * np.cos(sub_angle)
        y_inner = 0.85 * np.sin(sub_angle)
        ax.plot([x_inner, x_outer], [y_inner, y_outer], color='gray', lw=0.5)

    # Add the current position as a needle
    current_angle = 2 * np.pi * (1 - (current_age / expected_lifespan))
    x_needle = 0.7 * np.cos(current_angle)
    y_needle = 0.7 * np.sin(current_angle)
    ax.plot([0, x_needle], [0, y_needle], color='red', lw=3)  # Needle in red

    # Add center dot
    ax.plot(0, 0, 'o', color='black')

    # Set axis limits and remove ticks
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.axis('off')  # Hide axis

    st.pyplot(fig)

# Streamlit user inputs
st.title('Life Watch')
expected_lifespan = st.number_input("Enter your expected lifespan (in years):", min_value=1, value=80)
current_age = st.number_input("Enter your current age:", min_value=0, value=25)

# Display calculations and visuals
if st.button('Show My Life Watch'):
    remaining_years = calculate_remaining_years(expected_lifespan, current_age)
    
    st.write(f"You have lived {current_age} years.")
    st.write(f"You have {remaining_years} years remaining.")
    
    # Plot the life watch
    plot_life_watch(expected_lifespan, current_age)
