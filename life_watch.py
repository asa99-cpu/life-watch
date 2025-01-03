import streamlit as st
from sidebar import sidebar_inputs, display_dropdown
from visualizations import create_pie_chart
from utils import calculate_time, initialize_session_state, display_intro, display_footer

# Title of the app
st.title("Life Charging Bar ⚡")
st.subheader("Check Your Life's Charging Status Instead of Your Phone's!")

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

# Display dropdown menu
watch_style = display_dropdown()

# Create and display the selected life clock style
if watch_style == "Pie Chart":
    fig = create_pie_chart(passed_time, remaining_time)
    st.pyplot(fig)

# Display Time Breakdown
st.write(f"**Passed Time (Red):** {passed_time} years")
st.write(f"**Remaining Time (Green):** {remaining_time} years")

# Display footer
display_footer()
