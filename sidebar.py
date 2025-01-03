def display_dropdown():
    return st.sidebar.selectbox(
        "Select a style for your Life Clock:",
        ["Pie Chart", "Bar Chart", "Radial Bar", "Donut Chart", "Progress Ring", "Life Watch"],
        help="Choose how you want to visualize your life clock."
    )
