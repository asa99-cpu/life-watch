import streamlit as st

def user_inputs():
    # Sidebar title
    st.sidebar.title("⏳ Life Watch Settings")
    
    # Real-life inputs
    st.sidebar.header("Real-Life Inputs")
    current_age = st.sidebar.number_input("Enter your current age:", min_value=0, max_value=120, value=25, step=1)
    lifespan = st.sidebar.number_input("Expected lifespan (years):", min_value=1, max_value=150, value=70, step=1)
    
    # Lifestyle assessment
    st.sidebar.header("Lifestyle Assessment")
    reading_books = st.sidebar.selectbox("Do you read books regularly?", ["Yes", "No"])
    active_person = st.sidebar.selectbox("Are you physically active?", ["Yes", "No"])
    certifications = st.sidebar.selectbox("Have you earned certifications or pursued new skills recently?", ["Yes", "No"])
    hobbies = st.sidebar.selectbox("Do you engage in hobbies or creative activities?", ["Yes", "No"])

    # Calculate the desired age based on lifestyle choices
    score = 0
    if reading_books == "Yes":
        score += 2
    if active_person == "Yes":
        score += 2
    if certifications == "Yes":
        score += 2
    if hobbies == "Yes":
        score += 2

    desired_age = max(0, current_age - score)
    
    return current_age, lifespan, desired_age
