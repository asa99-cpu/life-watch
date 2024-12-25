import streamlit as st

def sidebar_inputs():
    st.sidebar.title("Life Watch Settings")
    expected_lifespan = st.sidebar.number_input(
        "Enter your expected lifespan (in years):",
        min_value=1,
        value=80,
    )
    current_age = st.sidebar.number_input(
        "Enter your current age:",
        min_value=0,
        value=25,
    )
    return expected_lifespan, current_age
