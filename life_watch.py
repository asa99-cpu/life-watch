import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Life Watch", layout="wide")

# Sidebar inputs
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

# Circular Life Watch visualization
def draw_life_watch(current_age, lifespan):
    life_percentage = current_age / lifespan
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis("equal")

    # Create the passed life section (red)
    theta_passed = np.linspace(0, 2 * np.pi * life_percentage, 500)
    ax.fill_between(np.cos(theta_passed), np.sin(theta_passed), color="red", alpha=0.6)

    # Create the remaining life section (green)
    theta_remaining = np.linspace(2 * np.pi * life_percentage, 2 * np.pi, 500)
    ax.fill_between(np.cos(theta_remaining), np.sin(theta_remaining), color="green", alpha=0.6)

    # Add labels for every 5 years
    for i in range(0, lifespan + 1, 5):
        angle = 2 * np.pi * i / lifespan
        x, y = np.cos(angle), np.sin(angle)
        ax.text(x * 1.2, y * 1.2, str(i), ha="center", va="center", fontsize=10, color="#555")

    # Add the "hand" of the clock
    angle = 2 * np.pi * current_age / lifespan
    ax.plot([0, np.cos(angle)], [0, np.sin(angle)], color="black", linewidth=3)

    # Styling
    ax.set_title("⏳ Circular Life Watch", fontsize=16)
    ax.axis("off")  # Hide axes
    return fig

# Main application
def main():
    current_age, lifespan = user_inputs()
    remaining_years = lifespan - current_age
    remaining_days = remaining_years * 365
    percentage_lived = (current_age / lifespan) * 100
    percentage_left = 100 - percentage_lived

    st.title("⏰ Life Watch")
    st.write("### A daily reminder to cherish your life's moments.")
    real_time_clock()

    # Layout
    col1, col2 = st.columns([2, 1])

    with col1:
        # Circular Life Watch visualization
        st.markdown("#### 🕒 Life Visualization")
        fig = draw_life_watch(current_age, lifespan)
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
