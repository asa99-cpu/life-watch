import streamlit as st
import math
from datetime import datetime, timedelta

# Set page configuration at the very beginning
st.set_page_config(page_title="Life Watch", layout="wide")

# Import the sidebar function
from sidebar import user_inputs


# Function to display the real watch
def real_watch():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    # Display all numbers on the watch
    st.markdown(
        f"""
        <div style="text-align: center; font-size: 20px; font-weight: bold; color: #4CAF50; border: 2px solid #4CAF50; border-radius: 10px; padding: 10px; width: 350px; margin: auto;">
            <h3 style="margin: 5px;">Real Watch</h3>
            <p style="margin: 5px;">Year: {year}</p>
            <p style="margin: 5px;">Month: {month:02d}</p>
            <p style="margin: 5px;">Day: {day:02d}</p>
            <p style="margin: 5px;">Hour: {hour:02d}</p>
            <p style="margin: 5px;">Minute: {minute:02d}</p>
            <p style="margin: 5px;">Second: {second:02d}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Main application
def main():
    # Get user inputs
    current_age, lifespan = user_inputs()

    # Calculate remaining years, months, days
    remaining_years = lifespan - current_age
    remaining_days = remaining_years * 365  # Approximate

    # Calculate percentage of life lived and left
    percentage_lived = (current_age / lifespan) * 100
    percentage_left = 100 - percentage_lived

    # Main title
    st.title("⏰ Your Life Watch")
    st.write("**Make every moment count.** This watch reminds you how precious life is.")

    # Real Watch Display
    st.subheader("🕒 Real Watch")
    real_watch()  # Display the real watch with full numbers
    st.markdown("---")

    # Visual representation
    col1, col2 = st.columns([2, 1])

    with col1:
        # Life Watch display
        st.subheader("🔵 Life Watch")
        st.markdown(
            f"""
            - **Current Age:** {current_age} years  
            - **Expected Lifespan:** {lifespan} years  
            - **Remaining Time:**  
                - **Years:** {remaining_years}  
                - **Days:** {remaining_days:,}  
            """
        )

    with col2:
        # Life Battery
        st.subheader("🔋 Life Battery")
        st.progress(math.floor(percentage_left))
        st.markdown(
            f"""
            - **Life Lived:** {percentage_lived:.2f}%  
            - **Life Left:** {percentage_left:.2f}%  
            """
        )

        # Charging Bar for Remaining Life
        st.subheader("🔌 Charging Bar (Remaining Life)")
        st.progress(math.floor(percentage_left))
        st.markdown(
            f"""
            - **Charging Status:** Remaining life at **{percentage_left:.2f}%**
            """
        )

    # Emotional message
    st.markdown(
        """
        ---
        ### Reflect on this
        Each passing second is an opportunity to live meaningfully. Spend your time wisely, cherish your moments, and embrace life to the fullest.
        """
    )


if __name__ == "__main__":
    main()
