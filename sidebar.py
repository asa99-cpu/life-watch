import streamlit as st

def sidebar_inputs():
    """
    Display input fields in the sidebar for current age and desired age.
    """
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

def display_dropdown():
    """
    Display a dropdown menu to select the visualization style.
    """
    return st.sidebar.selectbox(
        "Select a style for your Life Clock:",
        options=[
            "Life Watch",  # Make "Life Watch" the first option
            "Pie Chart", "Bar Chart", "Radial Bar",
            "Donut Chart", "Progress Ring", "Timeline"
        ],
        index=0  # Default to the first option ("Life Watch")
    )

def display_theme_selector():
    """
    Display a theme selector for light/dark mode.
    """
    theme = st.sidebar.selectbox(
        "Choose a theme:",
        options=["Light", "Dark"],
        help="Switch between light and dark themes."
    )
    return theme

def display_about_section():
    """
    Display the 'About' section in the sidebar.
    """
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        **About This App**  
        This app helps you visualize your life as a clock, showing how much time you've spent and how much you have left.  
        Reflect on your life and make the most of your time! ⏳
        """
    )

def display_footer():
    """
    Display the footer in the sidebar.
    """
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        Made with ❤️ by [Your Name]  
        Inspired by the idea of focusing on life's charging bar instead of your phone's.
        """
    )
