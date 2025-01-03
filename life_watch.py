import streamlit as st

# Title of the app
st.title("Life Charging Bar ⚡")
st.subheader("Check Your Life's Charging Status Instead of Your Phone's!")

# Introduction
st.write("""
Every morning, we check our phone's battery to see if it needs charging. 
But what about our own lives? Are we charging ourselves with skills, positivity, and growth?
Use this app to reflect on your life, skills, and personality. Let's check your **Life Charging Bar**!
""")

# Section 1: Life Reflection
st.header("1. Reflect on Your Life")
life_energy = st.slider("How energized do you feel about your life right now? (0 = Empty, 100 = Fully Charged)", 0, 100, 50)
st.write(f"Your Life Energy: **{life_energy}%**")

# Section 2: Skills and Abilities
st.header("2. Assess Your Skills and Abilities")
skill_level = st.slider("How confident are you in your current skills and abilities? (0 = Not Confident, 100 = Very Confident)", 0, 100, 50)
st.write(f"Your Skill Confidence: **{skill_level}%**")

# Section 3: Personality and Growth
st.header("3. Evaluate Your Personality and Growth")
growth_level = st.slider("How much do you feel you've grown as a person in the last year? (0 = No Growth, 100 = Significant Growth)", 0, 100, 50)
st.write(f"Your Personal Growth: **{growth_level}%**")

# Calculate Overall Life Charging Bar
overall_charge = (life_energy + skill_level + growth_level) // 3
st.header("Your Life Charging Bar")
st.progress(overall_charge)
st.write(f"Your Overall Life Charge: **{overall_charge}%**")

# Feedback and Suggestions
st.header("4. Suggestions to Recharge Your Life")
if overall_charge < 30:
    st.error("Your life charge is low. Consider taking time to reflect, learn new skills, and focus on personal growth.")
elif overall_charge < 70:
    st.warning("Your life charge is moderate. Keep pushing forward, but don't forget to take breaks and recharge.")
else:
    st.success("Your life charge is high! You're doing great. Keep up the good work and continue growing!")

# Footer
st.write("---")
st.write("Made with ❤️ by [Your Name]")
st.write("Inspired by the idea of focusing on life's charging bar instead of your phone's.")
