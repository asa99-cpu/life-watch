import streamlit as st

# Sidebar to get user inputs
def sidebar_inputs():
    # User inputs for expected lifespan and current age
    expected_lifespan = st.number_input("Expected Lifespan (Years)", min_value=1, value=80, step=1)
    current_age = st.number_input("Current Age (Years)", min_value=1, value=25, step=1)
    
    return expected_lifespan, current_age
