import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Life Watch", layout="wide")

# Sidebar Inputs
def user_inputs():
    st.sidebar.header("🌟 Life Inputs")
    current_age = st.sidebar.number_input(
        "Enter your current age:", min_value=0, max_value=120, value=25, step=1
    )
    lifespan = st.sidebar.number_input(
        "Enter your expected lifespan:", min_value=1, max_value=120, value=70, step=1
    )
    return current_age, lifespan

# Real-Time Clock Display
def real_time_clock():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    st.markdown("### 🕒 Real-Time Clock")
    st.markdown(f"**Current Date and Time:** {current_time}")
    st.markdown("---")

# Realistic Circular Life Watch
def draw_real_watch(current_age, lifespan):
    # Calculate percentage of life lived
    life_percentage = current_age / lifespan

    # Adjust theta to start from zero at the bottom of the clock (6 o'clock position)
    theta = np.linspace(0, 2 * np.pi, 1000) + np.pi / 2

    # Create the figure
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis("equal")

    # Create life segments: passed (red) and remaining (green)
    theta_passed = np.linspace(0, 2 * np.pi * life_percentage, 500) + np.pi / 2
    theta_remaining = np.linspace(2 * np.pi * life_percentage, 2 * np.pi, 500) + np.pi / 2
    ax.fill_between(np.cos(theta_passed), np.sin(theta_passed), color="red", alpha=0.6, label="Life Lived")
    ax.fill_between(np.cos(theta_remaining), np.sin(theta_remaining), color="green", alpha=0.6, label="Remaining Life")

    # Draw outer ring (clock border)
    outer_circle = plt.Circle((0, 0), 1.02, color="black", fill=False, linewidth=2)
    ax.add_artist(outer_circle)

    # Add tick marks for each year
    for i in range(lifespan + 1):
        angle = 2 * np.pi * i / lifespan + np.pi / 2
        x_start, y_start = np.cos(angle) * 0.95, np.sin(angle) * 0.95
        x_end, y_end = np.cos(angle), np.sin(angle)
        ax.plot([x_start, x_end], [y_start, y_end], color="black", linewidth=1)

    # Add labels every 5 years
    for i in range(0, lifespan + 1, 5):
        angle = 2 * np.pi * i / lifespan + np.pi / 2
        x, y = np.cos(angle) * 1.2, np.sin(angle) * 1.2
        ax.text(x, y, str(i), ha="center", va="center", fontsize=10, color="black")

    # Add clock hand for the current age
    angle = 2 * np.pi * current_age / lifespan + np.pi / 2
    ax.plot([0, np.cos(angle)], [0, np.sin(angle)], color="black", linewidth=3)

    # Add legend
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), fontsize=10, frameon=False)

    # Styling
    ax.set_title("⏳ Life Watch", fontsize=16, pad=20)
    ax.axis("off")  # Hide axes
    return fig

# Main Application
def main():
    # Get user inputs
    current_age, lifespan = user_inputs()

    # Calculate remaining life stats
    remaining_years = lifespan - current_age
    remaining_days = remaining_years * 365
    percentage_lived = (current_age / lifespan) * 100
    percentage_left = 100 - percentage_lived

    # Application layout
    st.title("⏰ Life Watch")
    st.write("### A daily reminder to cherish your life's moments.")
    real_time_clock()

    # Layout with columns
    col1, col2 = st.columns([2, 1])

    with col1:
        # Life Visualization
        st.markdown("#### 🕒 Life Visualization")
        fig = draw_real_watch(current_age, lifespan)
        st.pyplot(fig)

    with col2:
        # Life Stats
        st.markdown("#### 📊 Life Stats")
        st.markdown(
            f"""
            - **Current Age:** {current_age} years  
            - **Expected Lifespan:** {lifespan} years  
            - **Remaining Years:** {remaining_years} years  
            - **Remaining Days:** {remaining_days:,} days  
            """
        )
        st.markdown("#### 🔋 Life Battery")
        st.progress(math.floor(percentage_lived))
        st.markdown(f"**{percentage_lived:.2f}% Lived**  |  **{percentage_left:.2f}% Left**")

        # Motivational Message
        st.markdown("---")
        st.markdown(
            """
            ### 🌟 Reflect on This
            Life is precious. Use each moment to grow, connect, and make meaningful memories.
            """
        )

# Run the application
if __name__ == "__main__":
    main()
