import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

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

# Circular Life Watch
def draw_life_watch(current_age, lifespan):
    life_percentage = current_age / lifespan
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis("equal")

    # Create the "clock"
    theta = np.linspace(0, 2 * np.pi, 1000)
    ax.fill_between(np.cos(theta), np.sin(theta), color="#f0f0f0")  # Background color of the clock

    # Draw the passed life part in red
    passed_angle = 2 * np.pi * life_percentage
    ax.fill_between(theta[:int(passed_angle * 1000 / (2 * np.pi))], np.sin(theta[:int(passed_angle * 1000 / (2 * np.pi))]), 
                    color="red")

    # Draw the remaining life part in green
    ax.fill_between(theta[int(passed_angle * 1000 / (2 * np.pi)):], np.sin(theta[int(passed_angle * 1000 / (2 * np.pi)):]), 
                    color="green")

    # Add labels
    for i in range(0, lifespan + 1, 5):  # Tick every 5 years
        angle = 2 * np.pi * i / lifespan
        x, y = np.cos(angle), np.sin(angle)
        ax.text(x * 1.1, y * 1.1, f"{i}", ha="center", va="center", fontsize=10, color="#555")

    # Add the "hand" of the clock
    angle = 2 * np.pi * current_age / lifespan
    ax.plot([0, np.cos(angle)], [0, np.sin(angle)], color="blue", linewidth=2, label="Current Age")

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
