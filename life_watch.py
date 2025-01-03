import streamlit as st
from sidebar import sidebar_inputs, display_dropdown, display_theme_selector, display_about_section, display_footer
from visualizations import (
    create_pie_chart, create_bar_chart,
    create_radial_bar, create_donut_chart, create_progress_ring, create_life_watch
)
from utils import (
    calculate_time, calculate_time_breakdown,
    initialize_session_state, display_intro,
    display_time_breakdown
)

# Set page configuration
st.set_page_config(
    page_title="Life Charging Bar ⚡",
    page_icon="⏳",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #4F8BF9;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 24px;
        color: #666666;
        text-align: center;
        margin-bottom: 40px;
    }
    .time-breakdown {
        font-size: 18px;
        color: #333333;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown('<div class="main-title">Life Charging Bar ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Check Your Life\'s Charging Status Instead of Your Phone\'s!</div>', unsafe_allow_html=True)

# Display introduction
display_intro()

# Initialize session state
initialize_session_state()

# Run the sidebar inputs
sidebar_inputs()

# Calculate Passed and Remaining Time
passed_time, remaining_time, total_time = calculate_time(
    st.session_state.current_age, st.session_state.desired_age
)

# Display theme selector
theme = display_theme_selector()
if theme == "Dark":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Display dropdown menu
watch_style = display_dropdown()

# Create and display the selected life clock style
if watch_style == "Pie Chart":
    fig = create_pie_chart(passed_time, remaining_time)
elif watch_style == "Bar Chart":
    fig = create_bar_chart(passed_time, remaining_time)
elif watch_style == "Radial Bar":
    fig = create_radial_bar(passed_time, total_time)
elif watch_style == "Donut Chart":
    fig = create_donut_chart(passed_time, remaining_time)
elif watch_style == "Progress Ring":
    fig = create_progress_ring(passed_time, total_time)
elif watch_style == "Life Watch":
    fig = create_life_watch(passed_time, remaining_time, st.session_state.desired_age)

# Display the visualization
st.pyplot(fig)

# Display detailed time breakdown
st.markdown("### Time Breakdown")
passed_breakdown, remaining_breakdown = calculate_time_breakdown(
    st.session_state.current_age, st.session_state.desired_age
)
display_time_breakdown(passed_breakdown, remaining_breakdown)

# Display about section
display_about_section()

# Display footer
display_footer()
