import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Daily Life Battery", layout="wide")

# Sidebar Inputs
def user_inputs():
    st.sidebar.title("🔋 Life Battery Assessment")
    st.sidebar.markdown("Rate yourself on the following aspects (0–100):")
    
    physical = st.sidebar.slider("Physical Energy:", 0, 100, 50)
    mental = st.sidebar.slider("Mental Energy:", 0, 100, 50)
    emotional = st.sidebar.slider("Emotional Balance:", 0, 100, 50)
    skills = st.sidebar.slider("Skill Utilization:", 0, 100, 50)
    
    return physical, mental, emotional, skills

# Draw Battery Visualization
def draw_battery(physical, mental, emotional, skills):
    labels = ["Physical", "Mental", "Emotional", "Skills"]
    values = [physical, mental, emotional, skills]
    
    # Calculate overall score
    overall = np.mean(values)
    
    # Create figure
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#FF6F61", "#6B8E23", "#FFD700", "#4682B4"],
    )
    
    # Title and styling
    ax.set_title("🔋 Life Battery Breakdown", fontsize=16)
    for text in texts + autotexts:
        text.set_color("black")
        text.set_fontsize(12)
    
    return fig, overall

# Suggestions for Users
def provide_suggestions(overall):
    st.markdown("### Suggestions for Today 🌟")
    
    if overall > 80:
        st.success("Your life battery is charged! Keep up the great work and maintain your habits.")
    elif 50 <= overall <= 80:
        st.info("You're doing well, but consider focusing on areas with lower scores to recharge further.")
    else:
        st.warning("Your life battery is low. Take time for self-care, relaxation, and skill-building.")

    st.markdown(
        """
        #### Tips for Improvement:
        - **Physical Energy:** Try exercise, hydration, or a healthy meal.  
        - **Mental Energy:** Take breaks, meditate, or tackle a challenging task.  
        - **Emotional Balance:** Spend time with loved ones, journal, or practice gratitude.  
        - **Skill Utilization:** Work on a personal project or learn something new.  
        """
    )

# Real-Time Clock
def display_clock():
    now = datetime.now()
    st.markdown(f"**🕒 Current Time:** {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Main Function
def main():
    # Inputs
    physical, mental, emotional, skills = user_inputs()
    
    # Main Dashboard
    st.title("🔋 Daily Life Battery Dashboard")
    st.write("**Reflect on your life energy and take meaningful actions to recharge!**")
    display_clock()
    
    # Visualization and Insights
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🔋 Life Battery Visualization")
        fig, overall = draw_battery(physical, mental, emotional, skills)
        st.pyplot(fig)
    
    with col2:
        st.subheader("📊 Your Scores")
        st.markdown(
            f"""
            - **Physical Energy:** {physical}%  
            - **Mental Energy:** {mental}%  
            - **Emotional Balance:** {emotional}%  
            - **Skill Utilization:** {skills}%  
            - **Overall Life Battery:** {overall:.2f}%  
            """
        )
    
    # Suggestions
    provide_suggestions(overall)
    
    # Motivational Quote
    st.markdown(
        """
        ---
        ### 🌈 Daily Motivation  
        _"The key is not to prioritize what's on your schedule, but to schedule your priorities."_  
        """
    )

# Run the App
if __name__ == "__main__":
    main()
