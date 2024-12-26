import streamlit as st
import math
from datetime import timedelta

# Import the sidebar function
from sidebar import user_inputs

# Main application
def main():
    st.set_page_config(page_title="Life Watch", layout="wide")
    
    # Get user inputs
    current_age, lifespan = user_inputs()
    
    # Calculate remaining years, months, days
    remaining_years = lifespan - current_age
    remaining_days = remaining_years * 365  # Approximate
    
    # Calculate percentage of life lived
    percentage_lived = (current_age / lifespan) * 100
    percentage_left = 100 - percentage_lived
    
    # Main title
    st.title("⏰ Your Life Watch")
    st.write("**Make every moment count.** This watch reminds you how precious life is.")
    
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
