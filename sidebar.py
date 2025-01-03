import streamlit as st

# Sidebar for Age Input
def sidebar_inputs():
    st.sidebar.header("Life Clock Settings ⏳")
    
    # Input for current age
    current_age = st.sidebar.number_input(
        "What is your current age?",
        min_value=0,
        max_value=120,
        value=25,
        key="current_age_input"
    )
    
    # Input for desired age
    desired_age = st.sidebar.number_input(
        "What is the age you wish to live to?",
        min_value=current_age + 1,
        max_value=150,
        value=80,
        key="desired_age_input"
    )
    
    # Store values in session state
    st.session_state.current_age = current_age
    st.session_state.desired_age = desired_age

# Run the sidebar inputs
if __name__ == "__main__":
    sidebar_inputs()
