import streamlit as st

def sidebar_inputs():
    st.sidebar.header("Life Watch Settings")
    expected_lifespan = st.sidebar.number_input(
        "Expected Lifespan (Years)", min_value=1, max_value=120, value=80, step=1
    )
    current_age = st.sidebar.number_input(
        "Current Age (Years)", min_value=0, max_value=120, value=25, step=1
    )
    return expected_lifespan, current_age
