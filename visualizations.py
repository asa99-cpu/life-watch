import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge, Circle

# Custom colors for visualizations
PASSED_COLOR = "#FF6B6B"  # Red
REMAINING_COLOR = "#4ECDC4"  # Green
BACKGROUND_COLOR = "#F0F0F0"  # Light gray

def create_pie_chart(passed_time, remaining_time):
    """
    Create a pie chart to visualize passed and remaining time.
    """
    fig, ax = plt.subplots(figsize=(6, 6), facecolor=BACKGROUND_COLOR)
    sizes = [passed_time, remaining_time]
    colors = [PASSED_COLOR, REMAINING_COLOR]
    wedges, texts, autotexts = ax.pie(
        sizes,
        colors=colors,
        startangle=90,
        counterclock=False,
        wedgeprops=dict(width=0.3, edgecolor='black', linewidth=2),
        autopct='%1.1f%%',
        textprops=dict(color="black", fontsize=12)
    )
    # Add a white circle in the center to make it a donut chart
    centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='black', linewidth=2)
    fig.gca().add_artist(centre_circle)
    ax.axis('equal')
    plt.title("Life Clock (Pie Chart)", fontsize=16, pad=20)
    return fig

def create_bar_chart(passed_time, remaining_time):
    """
    Create a horizontal bar chart to visualize passed and remaining time.
    """
    fig, ax = plt.subplots(figsize=(8, 4), facecolor=BACKGROUND_COLOR)
    categories = ['Passed Time', 'Remaining Time']
    values = [passed_time, remaining_time]
    colors = [PASSED_COLOR, REMAINING_COLOR]
    ax.barh(categories, values, color=colors, edgecolor='black', linewidth=2)
    ax.set_xlabel('Years', fontsize=14)
    ax.set_title('Life Clock (Bar Chart)', fontsize=16, pad=20)
    ax.tick_params(axis='both', labelsize=12)
    return fig

def create_life_watch(passed_time, remaining_time, desired_age):
    """
    Create a watch-like visualization to show passed and remaining time.
    """
    fig, ax = plt.subplots(figsize=(6, 6), facecolor=BACKGROUND_COLOR)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis("off")  # Hide axes

    # Draw the outer circle (background)
    outer_circle = Circle((0, 0), 1, color="lightgray", alpha=0.3)
    ax.add_artist(outer_circle)

    # Calculate angles for passed and remaining time
    total_time = passed_time + remaining_time
    passed_angle = 360 * (passed_time / total_time)
    remaining_angle = 360 * (remaining_time / total_time)

    # Draw the passed time (red)
    passed_wedge = Wedge(
        center=(0, 0),
        r=1,
        theta1=90,  # Start at the top (12 o'clock position)
        theta2=90 - passed_angle,  # Move clockwise
        color=PASSED_COLOR,
        alpha=0.8
    )
    ax.add_artist(passed_wedge)

    # Draw the remaining time (green)
    remaining_wedge = Wedge(
        center=(0, 0),
        r=1,
        theta1=90 - passed_angle,  # Start where passed time ends
        theta2=90 - 360,  # Move clockwise to complete the circle
        color=REMAINING_COLOR,
        alpha=0.8
    )
    ax.add_artist(remaining_wedge)

    # Add a white inner circle to make it look like a watch
    inner_circle = Circle((0, 0), 0.8, color="white", edgecolor="black", linewidth=2)
    ax.add_artist(inner_circle)

    # Add labels for passed and remaining time
    ax.text(0, 1.1, f"Desired Age: {desired_age}", fontsize=14, ha="center", va="center", color="black")
    ax.text(0, -1.1, f"Passed: {passed_time} years", fontsize=12, ha="center", va="center", color=PASSED_COLOR)
    ax.text(0, -1.25, f"Remaining: {remaining_time} years", fontsize=12, ha="center", va="center", color=REMAINING_COLOR)

    return fig
