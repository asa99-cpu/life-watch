import streamlit as st

def calculate_time(current_age, desired_age):
    passed_time = current_age
    remaining_time = desired_age - current_age
    total_time = desired_age
    return passed_time, remaining_time, total_time

def initialize_session_state():
    if "current_age" not in st.session_state:
        st.session_state.current_age = 25  # Default value
    if "desired_age" not in st.session_state:
        st.session_state.desired_age = 80  # Default value

def display_intro():
    st.write("""
    Every morning, we check our phone's battery to see if it needs charging. 
    But what about our own lives? Are we charging ourselves with skills, positivity, and growth?
    Use this app to reflect on your life and visualize your time with the **Life Clock**.
    """)

def display_footer():
    st.write("---")
    st.write("Made with ❤️ by [Your Name]")
    st.write("Inspired by the idea of focusing on life's charging bar instead of your phone's.")
