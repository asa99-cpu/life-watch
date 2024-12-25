
---

### **life_watch.py**
```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Life Watch")

# Inputs
lifespan = st.number_input("Expected Lifespan (in years)", min_value=1, value=70)
current_age = st.number_input("Your Current Age (in years)", min_value=0, value=30)

# Calculate remaining years
remaining_years = lifespan - current_age
elapsed_percentage = (current_age / lifespan) * 100

# Display results
st.write(f"Remaining Years: **{remaining_years} years**")
st.write(f"You've lived **{elapsed_percentage:.2f}%** of your life.")

# Create a watch visual
theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, color="gray")  # Outer circle
ax.fill_between(x, y, where=(theta <= elapsed_percentage * 2 * np.pi / 100), color="blue", alpha=0.5)
ax.set_aspect('equal', 'box')
ax.set_title("Your Life Watch")
ax.axis("off")
st.pyplot(fig)

# Life battery
battery_level = 100 - elapsed_percentage
st.write(f"Life Battery: **{battery_level:.2f}% remaining**")
battery_color = "green" if battery_level > 50 else "orange" if battery_level > 20 else "red"
st.progress(int(battery_level), text=f"{int(battery_level)}%", color=battery_color)
