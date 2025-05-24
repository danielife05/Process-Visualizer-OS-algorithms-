from models.process import Process
from algorithms.fcfs import fcfs_scheduling
from utils.visualizer import plot_gantt

def main():
    processes = [
        Process(1, 0, 5),
        Process(2, 2, 3),
        Process(3, 4, 1),
    ]

    scheduled = fcfs_scheduling(processes)

    for p in scheduled:
        print(f"PID {p.pid}: Start={p.start_time}, Completion={p.completion_time}, Waiting={p.waiting_time}")

    plot_gantt(scheduled)

if __name__ == "__main__":
    main()
