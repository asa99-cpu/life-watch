import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Set page configuration at the very beginning
st.set_page_config(page_title="Life Watch", layout="wide")

# Import the sidebar function
def user_inputs():
    st.sidebar.header("Life Inputs")
    current_age = st.sidebar.number_input("Enter your current age:", min_value=0, max_value=120, value=25, step=1)
    lifespan = st.sidebar.number_input("Enter your expected lifespan:", min_value=1, max_value=120, value=70, step=1)
    return current_age, lifespan

# Function to create the circular life clock
def draw_life_watch(current_age, lifespan):
    # Calculate the percentage of life lived
    life_percentage = current_age / lifespan

    # Create the circular "life clock"
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis("equal")  # Make it circular

    # Create the "clock" as a pie chart
    theta = np.linspace(0, 2 * np.pi, 1000)
    ax.fill_between(np.cos(theta), np.sin(theta), color="#f0f0f0")

    # Add labels for each "year" on the clock
    for i in range(0, lifespan + 1, 5):  # Add ticks every 5 years
        angle = 2 * np.pi * i / lifespan
        x, y = np.cos(angle), np.sin(angle)
        ax.text(
            x * 1.1, y * 1.1, f"{i}",
            ha="center", va="center", fontsize=10, color="#555"
        )

    # Plot the "hand" of the clock
    angle = 2 * np.pi * current_age / lifespan
    ax.plot([0, np.cos(angle)], [0, np.sin(angle)], color="red", linewidth=2, label="Current Age")

    # Add styling and labels
    ax.set_title("Circular Life Watch", fontsize=16)
    ax.legend(loc="upper right")
    ax.axis("off")  # Remove axes
    return fig

# Main application
def main():
    # Get user inputs
    current_age, lifespan = user_inputs()

    # Display the life clock
    st.title("⏰ Your Circular Life Watch")
    st.write("**A visual representation of your life's timeline.**")

    st.subheader("🕒 Life Clock")
    fig = draw_life_watch(current_age, lifespan)
    st.pyplot(fig)

    # Additional stats
    remaining_years = lifespan - current_age
    percentage_lived = (current_age / lifespan) * 100
    percentage_left = 100 - percentage_lived

    st.markdown("---")
    st.subheader("📊 Life Summary")
    st.markdown(
        f"""
        - **Current Age:** {current_age} years  
        - **Expected Lifespan:** {lifespan} years  
        - **Remaining Years:** {remaining_years}  
        - **Life Lived:** {percentage_lived:.2f}%  
        - **Life Left:** {percentage_left:.2f}%
        """
    )

if __name__ == "__main__":
    main()
