import streamlit as st

def user_inputs():
    st.sidebar.title("⏳ Life Watch Settings")
    current_age = st.sidebar.number_input("Enter your current age:", min_value=0, max_value=120, value=25, step=1)
    lifespan = st.sidebar.number_input("Expected lifespan (years):", min_value=1, max_value=150, value=70, step=1)
    return current_age, lifespan
