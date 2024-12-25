import streamlit as st

# Function to capture inputs from the sidebar
def sidebar_inputs():
    # User inputs for expected lifespan and current age
    expected_lifespan = st.sidebar.number_input('Expected Lifespan (years)', min_value=1, max_value=150, value=80)
    current_age = st.sidebar.number_input('Your Current Age (years)', min_value=0, max_value=expected_lifespan, value=25)
    
    return expected_lifespan, current_age
