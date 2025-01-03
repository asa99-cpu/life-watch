import streamlit as st
from datetime import datetime, timedelta

def calculate_time(current_age, desired_age):
    """
    Calculate passed time, remaining time, and total time based on current and desired age.
    """
    passed_time = current_age
    remaining_time = desired_age - current_age
    total_time = desired_age
    return passed_time, remaining_time, total_time

def calculate_time_breakdown(current_age, desired_age):
    """
    Calculate a detailed breakdown of passed and remaining time in years, months, days, hours, minutes, and seconds.
    """
    now = datetime.now()
    birth_year = now.year - current_age
    target_year = now.year + (desired_age - current_age)

    # Calculate passed time
    passed_time = {
        "years": current_age,
        "months": current_age * 12,
        "days": current_age * 365,
        "hours": current_age * 365 * 24,
        "minutes": current_age * 365 * 24 * 60,
        "seconds": current_age * 365 * 24 * 60 * 60,
    }

    # Calculate remaining time
    remaining_time = {
        "years": desired_age - current_age,
        "months": (desired_age - current_age) * 12,
        "days": (desired_age - current_age) * 365,
        "hours": (desired_age - current_age) * 365 * 24,
        "minutes": (desired_age - current_age) * 365 * 24 * 60,
        "seconds": (desired_age - current_age) * 365 * 24 * 60 * 60,
    }

    return passed_time, remaining_time

def initialize_session_state():
    """
    Initialize session state variables with default values.
    """
    if "current_age" not in st.session_state:
        st.session_state.current_age = 25  # Default value
    if "desired_age" not in st.session_state:
        st.session_state.desired_age = 80  # Default value

def display_intro():
    """
    Display the introduction section of the app with styled text.
    """
    st.markdown(
        """
        <style>
        .intro-text {
            font-size: 18px;
            line-height: 1.6;
            color: #4F8BF9;
        }
        </style>
        <div class="intro-text">
        Every morning, we check our phone's battery to see if it needs charging. 
        But what about our own lives? Are we charging ourselves with skills, positivity, and growth?
        Use this app to reflect on your life and visualize your time with the <strong>Life Clock</strong>.
        </div>
        """,
        unsafe_allow_html=True
    )

def display_footer():
    """
    Display the footer section of the app with styled text.
    """
    st.markdown("---")
    st.markdown(
        """
        <style>
        .footer-text {
            font-size: 14px;
            text-align: center;
            color: #666666;
        }
        </style>
        <div class="footer-text">
        Made with ❤️ by <strong>[Your Name]</strong><br>
        Inspired by the idea of focusing on life's charging bar instead of your phone's.
        </div>
        """,
        unsafe_allow_html=True
    )

def display_time_breakdown(passed_time, remaining_time):
    """
    Display a detailed breakdown of passed and remaining time in a visually appealing way.
    """
    st.markdown("### Time Breakdown")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Passed Time")
        st.write(f"**Years:** {passed_time['years']}")
        st.write(f"**Months:** {passed_time['months']}")
        st.write(f"**Days:** {passed_time['days']}")
        st.write(f"**Hours:** {passed_time['hours']}")
        st.write(f"**Minutes:** {passed_time['minutes']}")
        st.write(f"**Seconds:** {passed_time['seconds']}")

    with col2:
        st.markdown("#### Remaining Time")
        st.write(f"**Years:** {remaining_time['years']}")
        st.write(f"**Months:** {remaining_time['months']}")
        st.write(f"**Days:** {remaining_time['days']}")
        st.write(f"**Hours:** {remaining_time['hours']}")
        st.write(f"**Minutes:** {remaining_time['minutes']}")
        st.write(f"**Seconds:** {remaining_time['seconds']}")
