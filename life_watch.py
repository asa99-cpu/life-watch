import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

# Title of the app
st.title("Life Charging Bar ⚡")
st.subheader("Check Your Life's Charging Status Instead of Your Phone's!")

# Introduction
st.write("""
Every morning, we check our phone's battery to see if it needs charging. 
But what about our own lives? Are we charging ourselves with skills, positivity, and growth?
Use this app to reflect on your life and visualize your time with the **Life Clock**.
""")

# Sidebar for Age Input
st.sidebar.header("Life Clock Settings ⏳")
current_age = st.sidebar.number_input("What is your current age?", min_value=0, max_value=120, value=25)
desired_age = st.sidebar.number_input("What is the age you wish to live to?", min_value=current_age + 1, max_value=150, value=80)

# Calculate Passed and Remaining Time
passed_time = current_age
remaining_time = desired_age - current_age
total_time = desired_age

# Dropdown for selecting the watch style
st.header("Choose Your Life Clock Style")
watch_style = st.selectbox(
    "Select a style for your Life Clock:",
    ["Pie Chart", "Bar Chart", "Radial Bar", "Donut Chart", "Progress Ring"]
)

# Function to create the life clock visualization
def create_life_clock(style):
    if style == "Pie Chart":
        # Pie Chart Style
        fig, ax = plt.subplots(figsize=(6, 6))
        sizes = [passed_time, remaining_time]
        colors = ['red', 'green']
        wedges, texts, autotexts = ax.pie(
            sizes,
            colors=colors,
            startangle=90,
            counterclock=False,
            wedgeprops=dict(width=0.3, edgecolor='black'),
            autopct='%1.1f%%'
        )
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig.gca().add_artist(centre_circle)
        ax.axis('equal')
        st.pyplot(fig)

    elif style == "Bar Chart":
        # Bar Chart Style
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(['Passed Time', 'Remaining Time'], [passed_time, remaining_time], color=['red', 'green'])
        ax.set_xlabel('Years')
        ax.set_title('Life Clock (Bar Chart)')
        st.pyplot(fig)

    elif style == "Radial Bar":
        # Radial Bar Style
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        theta = np.linspace(0, 2 * np.pi, 100)
        ax.fill_between(theta, 0, passed_time / total_time * 100, color='red')
        ax.fill_between(theta, passed_time / total_time * 100, 100, color='green')
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.set_title('Life Clock (Radial Bar)')
        st.pyplot(fig)

    elif style == "Donut Chart":
        # Donut Chart Style
        fig, ax = plt.subplots(figsize=(6, 6))
        sizes = [passed_time, remaining_time]
        colors = ['red', 'green']
        wedges, texts, autotexts = ax.pie(
            sizes,
            colors=colors,
            startangle=90,
            counterclock=False,
            wedgeprops=dict(width=0.5, edgecolor='black'),
            autopct='%1.1f%%'
        )
        ax.axis('equal')
        st.pyplot(fig)

    elif style == "Progress Ring":
        # Progress Ring Style
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
        # Draw the background circle
        background_circle = plt.Circle((0.5, 0.5), 0.4, color='lightgray', fill=False, linewidth=10)
        ax.add_artist(background_circle)
        
        # Calculate the angle for the progress ring
        progress = passed_time / total_time
        end_angle = 360 * progress
        
        # Draw the progress ring using Wedge
        wedge = Wedge(
            center=(0.5, 0.5),
            r=0.4,
            theta1=0,
            theta2=end_angle,
            color='green',
            width=0.1,
            alpha=0.5
        )
        ax.add_artist(wedge)
        
        # Draw the remaining time ring
        remaining_wedge = Wedge(
            center=(0.5, 0.5),
            r=0.4,
            theta1=end_angle,
            theta2=360,
            color='red',
            width=0.1,
            alpha=0.5
        )
        ax.add_artist(remaining_wedge)
        
        ax.axis('off')
        st.pyplot(fig)

# Display the selected life clock style
create_life_clock(watch_style)

# Display Time Breakdown
st.write(f"**Passed Time (Red):** {passed_time} years")
st.write(f"**Remaining Time (Green):** {remaining_time} years")

# Footer
st.write("---")
st.write("Made with ❤️ by [Your Name]")
st.write("Inspired by the idea of focusing on life's charging bar instead of your phone's.")
