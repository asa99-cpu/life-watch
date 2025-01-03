import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge, Circle
from matplotlib.colors import LinearSegmentedColormap

# Custom colors for visualizations
PASSED_COLOR = "#FF6B6B"  # Red
REMAINING_COLOR = "#4ECDC4"  # Green
BACKGROUND_COLOR = "#F0F0F0"  # Light gray

# Create a custom colormap for gradient effects
gradient_colors = [PASSED_COLOR, REMAINING_COLOR]
gradient_cmap = LinearSegmentedColormap.from_list("custom_gradient", gradient_colors)

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

def create_radial_bar(passed_time, total_time):
    """
    Create a radial bar chart to visualize passed and remaining time.
    """
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True), facecolor=BACKGROUND_COLOR)
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.fill_between(theta, 0, passed_time / total_time * 100, color=PASSED_COLOR, alpha=0.8)
    ax.fill_between(theta, passed_time / total_time * 100, 100, color=REMAINING_COLOR, alpha=0.8)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.title("Life Clock (Radial Bar)", fontsize=16, pad=20)
    return fig

def create_donut_chart(passed_time, remaining_time):
    """
    Create a donut chart to visualize passed and remaining time.
    """
    fig, ax = plt.subplots(figsize=(6, 6), facecolor=BACKGROUND_COLOR)
    sizes = [passed_time, remaining_time]
    colors = [PASSED_COLOR, REMAINING_COLOR]
    wedges, texts, autotexts = ax.pie(
        sizes,
        colors=colors,
        startangle=90,
        counterclock=False,
        wedgeprops=dict(width=0.5, edgecolor='black', linewidth=2),
        autopct='%1.1f%%',
        textprops=dict(color="black", fontsize=12)
    )
    ax.axis('equal')
    plt.title("Life Clock (Donut Chart)", fontsize=16, pad=20)
    return fig

def create_progress_ring(passed_time, total_time):
    """
    Create a progress ring to visualize passed and remaining time.
    """
    fig, ax = plt.subplots(figsize=(6, 6), facecolor=BACKGROUND_COLOR)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Draw the background circle
    background_circle = plt.Circle((0.5, 0.5), 0.4, color='lightgray', fill=False, linewidth=10)
    ax.add_artist(background_circle)
    
    # Calculate the angle for the progress ring
    progress = passed_time / total_time
    end_angle = 360 * progress
    
    # Draw the progress ring using Wedge
    wedge = Wedge(
        center=(0.5, 0.5),
        r=0.4,
        theta1=0,
        theta2=end_angle,
        color=REMAINING_COLOR,
        width=0.1,
        alpha=0.8
    )
    ax.add_artist(wedge)
    
    # Draw the remaining time ring
    remaining_wedge = Wedge(
        center=(0.5, 0.5),
        r=0.4,
        theta1=end_angle,
        theta2=360,
        color=PASSED_COLOR,
        width=0.1,
        alpha=0.8
    )
    ax.add_artist(remaining_wedge)
    
    ax.axis('off')
    plt.title("Life Clock (Progress Ring)", fontsize=16, pad=20)
    return fig

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

def create_gradient_visualization(passed_time, total_time):
    """
    Create a gradient-based visualization to show passed and remaining time.
    """
    fig, ax = plt.subplots(figsize=(6, 6), facecolor=BACKGROUND_COLOR)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Create a gradient background
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack((gradient, gradient))
    ax.imshow(gradient, aspect='auto', cmap=gradient_cmap, extent=[0, 1, 0, 1])
    
    # Add a progress bar
    progress = passed_time / total_time
    ax.barh(0.5, progress, height=0.2, color=PASSED_COLOR, edgecolor='black', linewidth=2)
    ax.barh(0.5, 1 - progress, height=0.2, left=progress, color=REMAINING_COLOR, edgecolor='black', linewidth=2)
    
    ax.axis('off')
    plt.title("Life Clock (Gradient Visualization)", fontsize=16, pad=20)
    return fig

def create_timeline(passed_time, remaining_time):
    """
    Create a timeline visualization to show passed and remaining time.
    """
    fig, ax = plt.subplots(figsize=(10, 2), facecolor=BACKGROUND_COLOR)
    total_time = passed_time + remaining_time
    
    # Draw the timeline
    ax.barh(0, passed_time, height=0.5, color=PASSED_COLOR, edgecolor='black', linewidth=2)
    ax.barh(0, remaining_time, height=0.5, left=passed_time, color=REMAINING_COLOR, edgecolor='black', linewidth=2)
    
    # Add labels
    ax.text(passed_time / 2, 0.25, f"Passed: {passed_time} years", fontsize=12, ha="center", va="center", color="black")
    ax.text(passed_time + remaining_time / 2, 0.25, f"Remaining: {remaining_time} years", fontsize=12, ha="center", va="center", color="black")
    
    ax.set_xlim(0, total_time)
    ax.set_ylim(-0.5, 0.5)
    ax.axis('off')
    plt.title("Life Clock (Timeline)", fontsize=16, pad=20)
    return fig
