import matplotlib.pyplot as plt

def plot_gantt(processes):
    fig, ax = plt.subplots()
    for p in processes:
        ax.broken_barh([(p.start_time, p.burst_time)], (10 * p.pid, 9), facecolors='tab:blue')
        ax.text(p.start_time + p.burst_time / 2, 10 * p.pid + 4, f"P{p.pid}", ha='center', va='center', color='white')
    ax.set_xlabel('Tiempo')
    ax.set_yticks([10 * p.pid + 4 for p in processes])
    ax.set_yticklabels([f"P{p.pid}" for p in processes])
    plt.title("Diagrama de Gantt")
    plt.show()
