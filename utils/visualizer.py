import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

def generate_color_map(processes):
    colors = {}
    random.seed(42)
    for p in processes:
        if p.pid not in colors:
            colors[p.pid] = "#" + ''.join(random.choices('0123456789ABCDEF', k=6))
    return colors

def plot_gantt_in_tk(processes, title, frame):
    fig, ax = plt.subplots(figsize=(6, 2))
    color_map = generate_color_map(processes)

    for p in processes:
        ax.broken_barh([(p.start_time, p.burst_time)], (10 * p.pid, 9),
                       facecolors=color_map[p.pid])
        ax.text(p.start_time + p.burst_time / 2, 10 * p.pid + 4, f"P{p.pid}",
                ha='center', va='center', color='white', fontsize=9, weight='bold')

    ax.set_xlabel('Time')
    ax.set_yticks([10 * p.pid + 4 for p in processes])
    ax.set_yticklabels([f"P{p.pid}" for p in processes])
    ax.set_title(title)
    plt.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=True)