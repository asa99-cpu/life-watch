import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge, Circle

def create_life_watch(passed_time, remaining_time, desired_age):
    """
    Create a watch-like visualization to show passed and remaining time.
    """
    fig, ax = plt.subplots(figsize=(6, 6), facecolor="#F0F0F0")
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
        color="#FF6B6B",  # Red
        alpha=0.8
    )
    ax.add_artist(passed_wedge)

    # Draw the remaining time (green)
    remaining_wedge = Wedge(
        center=(0, 0),
        r=1,
        theta1=90 - passed_angle,  # Start where passed time ends
        theta2=90 - 360,  # Move clockwise to complete the circle
        color="#4ECDC4",  # Green
        alpha=0.8
    )
    ax.add_artist(remaining_wedge)

    # Add a white inner circle to make it look like a watch
    inner_circle = Circle((0, 0), 0.8, color="white", edgecolor="black", linewidth=2)
    ax.add_artist(inner_circle)

    # Add labels for passed and remaining time
    ax.text(0, 1.1, f"Desired Age: {desired_age}", fontsize=14, ha="center", va="center", color="black")
    ax.text(0, -1.1, f"Passed: {passed_time} years", fontsize=12, ha="center", va="center", color="#FF6B6B")
    ax.text(0, -1.25, f"Remaining: {remaining_time} years", fontsize=12, ha="center", va="center", color="#4ECDC4")

    return fig
