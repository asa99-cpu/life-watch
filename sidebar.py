import streamlit as st

def sidebar_inputs():
    # Sidebar header with emoji and styling
    st.sidebar.markdown(
        """
        <style>
        .sidebar-header {
            font-size: 24px;
            font-weight: bold;
            color: #4F8BF9;
        }
        </style>
        <div class="sidebar-header">⏳ Life Clock Settings</div>
        """,
        unsafe_allow_html=True
    )

    # Input for current age
    current_age = st.sidebar.number_input(
        "What is your current age?",
        min_value=0,
        max_value=120,
        value=25,
        key="current_age_input",
        help="Enter your current age in years."
    )
    
    # Input for desired age
    desired_age = st.sidebar.number_input(
        "What is the age you wish to live to?",
        min_value=current_age + 1,
        max_value=150,
        value=80,
        key="desired_age_input",
        help="Enter the age you wish to live to in years."
    )
    
    # Store values in session state
    st.session_state.current_age = current_age
    st.session_state.desired_age = desired_age

    # Add a separator for better visual organization
    st.sidebar.markdown("---")

def display_dropdown():
    # Dropdown for selecting visualization style
    return st.sidebar.selectbox(
        "Select a style for your Life Clock:",
        ["Pie Chart", "Bar Chart", "Radial Bar", "Donut Chart", "Progress Ring"],
        help="Choose how you want to visualize your life clock."
    )

def display_theme_selector():
    # Theme selector for light/dark mode
    theme = st.sidebar.selectbox(
        "Choose a theme:",
        ["Light", "Dark"],
        help="Switch between light and dark themes."
    )
    return theme

def display_about_section():
    # About section in the sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        **About This App**  
        This app helps you visualize your life as a clock, showing how much time you've spent and how much you have left.  
        Reflect on your life and make the most of your time! ⏳
        """
    )

def display_footer():
    # Footer in the sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        Made with ❤️ by [Your Name]  
        Inspired by the idea of focusing on life's charging bar instead of your phone's.
        """
    )
