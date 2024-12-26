import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from sidebar import user_inputs  # Importing the updated sidebar script

# Set page configuration at the very beginning
st.set_page_config(page_title="Life Watch", layout="wide")

# Real-Time Clock Display
def real_time_clock():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    st.subheader("🕒 Real-Time Clock")
    st.markdown(f"**Current Date and Time:** {current_time}")
    st.markdown("---")

# Circular Life Watch with different colors for passed and remaining life
def draw_life_watch(current_age, lifespan):
    life_percentage = current_age / lifespan
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis("equal")

    # Create the "clock"
    theta = np.linspace(0, 2 * np.pi, 1000)

    # Create the passed life (red)
    ax.fill_between(np.cos(theta), np.sin(theta), where=(theta <= 2 * np.pi * life_percentage), color="red", alpha=0.6)

    # Create the remaining life (green)
    ax.fill_between(np.cos(theta), np.sin(theta), where=(theta > 2 * np.pi * life_percentage), color="green", alpha=0.6)

    # Add labels
    for i in range(0, lifespan + 1, 5):  # Tick every 5 years
        angle = 2 * np.pi * i / lifespan
        x, y = np.cos(angle), np.sin(angle)
        ax.text(x * 1.1, y * 1.1, f"{i}", ha="center", va="center", fontsize=10, color="#555")

    # Add the "hand" of the clock
    angle = 2 * np.pi * current_age / lifespan
    ax.plot([0, np.cos(angle)], [0, np.sin(angle)], color="red", linewidth=2, label="Current Age")

    # Styling
    ax.set_title("Circular Life Watch", fontsize=16)
    ax.legend(loc="upper right")
    ax.axis("off")  # Remove axes
    return fig

# Main application
def main():
    # Get user inputs
    current_age, lifespan, desired_age = user_inputs()
    remaining_years = lifespan - current_age
    remaining_days = remaining_years * 365
    percentage_lived = (current_age / lifespan) * 100
    percentage_left = 100 - percentage_lived

    # Calculate stats for desired age
    desired_remaining_years = lifespan - desired_age
    desired_remaining_days = desired_remaining_years * 365
    desired_percentage_lived = (desired_age / lifespan) * 100
    desired_percentage_left = 100 - desired_percentage_lived

    # Title and Clock
    st.title("⏰ Your Life Watch")
    st.write("**A reminder of how precious time is.**")
    real_time_clock()

    # Life Watch Visualizations
    col1, col2 = st.columns([2, 1])

    with col1:
        # Circular Life Watch
        st.subheader("🕒 Circular Life Watch (Real Age)")
        fig_real = draw_life_watch(current_age, lifespan)
        st.pyplot(fig_real)

        st.subheader("🌟 Circular Life Watch (Desired Age)")
        fig_desired = draw_life_watch(desired_age, lifespan)
        st.pyplot(fig_desired)

    with col2:
        # Life Summary Stats for Real Age
        st.subheader("🔵 Life Stats (Real Age)")
        st.markdown(
            f"""
            - **Current Age:** {current_age} years  
            - **Expected Lifespan:** {lifespan} years  
            - **Remaining Time:**  
                - **Years:** {remaining_years}  
                - **Days:** {remaining_days:,}  
            """
        )
        st.progress(math.floor(percentage_left))
        st.markdown(
            f"""
            - **Life Lived:** {percentage_lived:.2f}%  
            - **Life Left:** {percentage_left:.2f}%  
            """
        )

        # Life Summary Stats for Desired Age
        st.subheader("🌟 Life Stats (Desired Age)")
        st.markdown(
            f"""
            - **Desired Age:** {desired_age} years  
            - **Expected Lifespan:** {lifespan} years  
            - **Remaining Time:**  
                - **Years:** {desired_remaining_years}  
                - **Days:** {desired_remaining_days:,}  
            """
        )
        st.progress(math.floor(desired_percentage_left))
        st.markdown(
            f"""
            - **Life Lived (Desired):** {desired_percentage_lived:.2f}%  
            - **Life Left (Desired):** {desired_percentage_left:.2f}%  
            """
        )

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
