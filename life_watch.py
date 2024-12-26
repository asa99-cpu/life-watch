import streamlit as st
import math
from datetime import datetime, timedelta
import time  # Required for real-time updates

# Set page configuration at the very beginning
st.set_page_config(page_title="Life Watch", layout="wide")

# Import the sidebar function
from sidebar import user_inputs

# Function to display the real-time clock
def real_time_clock():
    # Get the current time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Display the clock
    st.subheader("🕒 Real-Time Clock")
    st.markdown(f"**Current Date and Time:** {current_time}")
    st.markdown("---")

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
    
    # Real-Time Clock Display
    real_time_clock()
    
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

# Run the main application
if __name__ == "__main__":
    main()
