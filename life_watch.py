import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate remaining years
def calculate_remaining_years(expected_lifespan, current_age):
    return expected_lifespan - current_age

# Function to create life watch visualization
def plot_life_watch(expected_lifespan, current_age):
    remaining_years = calculate_remaining_years(expected_lifespan, current_age)
    total_years = expected_lifespan
    
    # Create the life watch as a pie chart
    labels = ['Lived Years', 'Remaining Years']
    sizes = [current_age, remaining_years]
    colors = ['#00bfae', '#ffcc00']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig)

# Function to create life battery visualization
def plot_life_battery(expected_lifespan, current_age):
    remaining_years = calculate_remaining_years(expected_lifespan, current_age)
    total_years = expected_lifespan
    
    # Life battery as a bar chart
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.barh(['Life'], current_age, color='#00bfae', edgecolor='black', height=0.5)
    ax.barh(['Life'], remaining_years, left=current_age, color='#ffcc00', edgecolor='black', height=0.5)
    
    ax.set_xlim(0, total_years)
    ax.set_title("Life Battery")
    ax.set_xlabel("Years")
    ax.set_yticks([])  # Remove the y-axis ticks
    
    st.pyplot(fig)

# Streamlit user inputs
st.title('Life Watch')
expected_lifespan = st.number_input("Enter your expected lifespan (in years):", min_value=1, value=70)
current_age = st.number_input("Enter your current age:", min_value=0, value=25)

# Display calculations and visuals
if st.button('Show My Life Watch'):
    remaining_years = calculate_remaining_years(expected_lifespan, current_age)
    
    st.write(f"You have lived {current_age} years.")
    st.write(f"You have {remaining_years} years remaining.")
    
    # Plot the life watch and life battery
    plot_life_watch(expected_lifespan, current_age)
    plot_life_battery(expected_lifespan, current_age)
