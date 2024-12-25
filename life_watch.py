import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate remaining years
def calculate_remaining_years(expected_lifespan, current_age):
    return expected_lifespan - current_age

# Function to create the life watch (real watch style)
def plot_life_watch(expected_lifespan, current_age):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')

    # Create the watch face
    circle = plt.Circle((0, 0), 1, color='#f0f0f0', ec='black')
    ax.add_artist(circle)

    # Add markers for each year
    for year in range(1, expected_lifespan + 1):
        angle = 2 * np.pi * (year / expected_lifespan)
        x_outer = 0.9 * np.cos(angle)
        y_outer = 0.9 * np.sin(angle)
        x_inner = 0.8 * np.cos(angle)
        y_inner = 0.8 * np.sin(angle)
        ax.plot([x_inner, x_outer], [y_inner, y_outer], color='black', lw=1)

        # Add labels for specific intervals
        if year % (expected_lifespan // 12) == 0 or year == 1:  # Label at intervals
            x_label = 0.7 * np.cos(angle)
            y_label = 0.7 * np.sin(angle)
            ax.text(
                x_label,
                y_label,
                str(year),
                ha='center',
                va='center',
                fontsize=8,
                color='black',
            )

    # Add the current position as a needle
    current_angle = 2 * np.pi * (current_age / expected_lifespan)
    x_needle = 0.7 * np.cos(current_angle)
    y_needle = 0.7 * np.sin(current_angle)
    ax.plot([0, x_needle], [0, y_needle], color='#ff5733', lw=3)  # Needle in red

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
