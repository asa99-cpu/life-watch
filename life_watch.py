import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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

# Create the Life Clock Visualization
st.header("Your Life Clock ⏰")

# Create a pie chart to represent the life clock
fig, ax = plt.subplots(figsize=(6, 6))

# Data for the pie chart
sizes = [passed_time, remaining_time]
colors = ['red', 'green']
labels = ['Passed Time', 'Remaining Time']

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    sizes,
    colors=colors,
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.3, edgecolor='black'),
    autopct='%1.1f%%'
)

# Add a circle in the center to make it look like a watch
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie chart is circular
ax.axis('equal')

# Display the pie chart in Streamlit
st.pyplot(fig)

# Display Time Breakdown
st.write(f"**Passed Time (Red):** {passed_time} years")
st.write(f"**Remaining Time (Green):** {remaining_time} years")

# Footer
st.write("---")
st.write("Made with ❤️ by [Your Name]")
st.write("Inspired by the idea of focusing on life's charging bar instead of your phone's.")
