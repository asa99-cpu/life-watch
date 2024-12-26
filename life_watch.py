import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.patches import Wedge

# Set page configuration at the very beginning
st.set_page_config(page_title="Life Watch", layout="wide")

# Sidebar inputs
def user_inputs():
    st.sidebar.header("Life Inputs")
    current_age = st.sidebar.number_input("Enter your current age:", min_value=0, max_value=120, value=25, step=1)
    lifespan = st.sidebar.number_input("Enter your expected lifespan:", min_value=1, max_value=120, value=70, step=1)
    return current_age, lifespan

# Real-Time Clock Display
def real_time_clock():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    st.subheader("🕒 Real-Time Clock")
    st.markdown(f"**Current Date and Time:** {current_time}")
    st.markdown("---")

# Circular Life Watch with filled wedges
def draw_life_watch(current_age, lifespan):
    life_percentage = current_age / lifespan
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis("equal")

    # Create the background of the clock (light gray circle)
    circle = plt.Circle((0, 0), 1, color='#f0f0f0', ec='black', lw=1)
    ax.add_artist(circle)

    # Draw the passed life part in red (filled wedge)
    passed_angle = 360 * life_percentage
    passed_wedge = Wedge(center=(0, 0), r=1, theta1=0, theta2=passed_angle, facecolor='red')
    ax.add_artist(passed_wedge)

    # Draw the remaining life part in green (filled wedge)
    remaining_angle = 360 * (1 - life_percentage)
    remaining_wedge = Wedge(center=(0, 0), r=1, theta1=passed_angle, theta2=passed_angle + remaining_angle, facecolor='green')
    ax.add_artist(remaining_wedge)

    # Add labels for passed life in red and remaining life in green
    for i in range(0, lifespan + 1, 5):  # Tick every 5 years
        angle = 360 * i / lifespan
        x, y = np.cos(np.radians(angle)), np.sin(np.radians(angle))
        ax.text(x * 1.15, y * 1.15, f"{i}", ha="center", va="center", fontsize=10, color="#555")

    # Add the "hand" of the clock (red color)
    angle = 360 * current_age / lifespan
    ax.plot([0, np.cos(np.radians(angle))], [0, np.sin(np.radians(angle))], color="blue", linewidth=2, label="Current Age")

    # Styling
    ax.set_title("Circular Life Watch", fontsize=16)
    ax.legend(loc="upper right")
    ax.axis("off")  # Remove axes
    return fig

# Main application
def main():
    # Get user inputs
    current_age, lifespan = user_inputs()
    remaining_years = lifespan - current_age
    remaining_days = remaining_years * 365
    percentage_lived = (current_age / lifespan) * 100
    percentage_left = 100 - percentage_lived

    # Title and Clock
    st.title("⏰ Your Life Watch")
    st.write("**A reminder of how precious time is.**")
    real_time_clock()

    # Life Watch Visualizations
    col1, col2 = st.columns([2, 1])

    with col1:
        # Circular Life Watch
        st.subheader("🕒 Circular Life Watch")
        fig = draw_life_watch(current_age, lifespan)
        st.pyplot(fig)

    with col2:
        # Life Summary Stats
        st.subheader("🔵 Life Stats")
        st.markdown(
            f"""
            - **Current Age:** {current_age} years  
            - **Expected Lifespan:** {lifespan} years  
            - **Remaining Time:**  
                - **Years:** {remaining_years}  
                - **Days:** {remaining_days:,}  
            """
        )

        # Life Battery Bar
        st.subheader("🔋 Life Battery")
        st.progress(math.floor(percentage_left))
        st.markdown(
            f"""
            - **Life Lived:** {percentage_lived:.2f}%  
            - **Life Left:** {percentage_left:.2f}%  
            """
        )

        # Charging Bar for Remaining Life
        st.subheader("🔌 Charging Bar (Remaining Life)")
        st.progress(math.floor(percentage_left))
        st.markdown(f"**Charging Status:** Remaining life at **{percentage_left:.2f}%**")

    # Motivational Message
    st.markdown(
        """
        --- 
        ### Reflect on this
        Every second is precious. Use your time wisely, make meaningful connections, and embrace life's journey.
        """
    )

# Run the main application
if __name__ == "__main__":
    main()
