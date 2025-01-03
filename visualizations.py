import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

def create_pie_chart(passed_time, remaining_time):
    fig, ax = plt.subplots(figsize=(6, 6))
    sizes = [passed_time, remaining_time]
    colors = ['red', 'green']
    wedges, texts, autotexts = ax.pie(
        sizes,
        colors=colors,
        startangle=90,
        counterclock=False,
        wedgeprops=dict(width=0.3, edgecolor='black'),
        autopct='%1.1f%%'
    )
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    ax.axis('equal')
    return fig

def create_bar_chart(passed_time, remaining_time):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(['Passed Time', 'Remaining Time'], [passed_time, remaining_time], color=['red', 'green'])
    ax.set_xlabel('Years')
    ax.set_title('Life Clock (Bar Chart)')
    return fig

def create_radial_bar(passed_time, total_time):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.fill_between(theta, 0, passed_time / total_time * 100, color='red')
    ax.fill_between(theta, passed_time / total_time * 100, 100, color='green')
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_title('Life Clock (Radial Bar)')
    return fig

def create_donut_chart(passed_time, remaining_time):
    fig, ax = plt.subplots(figsize=(6, 6))
    sizes = [passed_time, remaining_time]
    colors = ['red', 'green']
    wedges, texts, autotexts = ax.pie(
        sizes,
        colors=colors,
        startangle=90,
        counterclock=False,
        wedgeprops=dict(width=0.5, edgecolor='black'),
        autopct='%1.1f%%'
    )
    ax.axis('equal')
    return fig

def create_progress_ring(passed_time, total_time):
    fig, ax = plt.subplots(figsize=(6, 6))
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
        color='green',
        width=0.1,
        alpha=0.5
    )
    ax.add_artist(wedge)
    
    # Draw the remaining time ring
    remaining_wedge = Wedge(
        center=(0.5, 0.5),
        r=0.4,
        theta1=end_angle,
        theta2=360,
        color='red',
        width=0.1,
        alpha=0.5
    )
    ax.add_artist(remaining_wedge)
    
    ax.axis('off')
    return fig
