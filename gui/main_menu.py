import tkinter as tk
from algorithms.fcfs import fcfs_scheduling
from algorithms.sjf import sjf_scheduling
from models.process import Process
from gui.result_window import show_result_window
from gui.rr_window import open_rr_input_window

def get_sample_processes():
    return [
        Process(1, 0, 5),
        Process(2, 2, 3),
        Process(3, 4, 1),
    ]

def launch_main_menu():
    root = tk.Tk()
    root.title("Process Scheduler")
    root.geometry("300x250")

    tk.Label(root, text="Choose Scheduling Algorithm:", font=("Arial", 12)).pack(pady=15)

    def run_fcfs():
        procs = get_sample_processes()
        result = fcfs_scheduling(procs)
        show_result_window(result, "FCFS Scheduling")

    def run_sjf():
        procs = get_sample_processes()
        result = sjf_scheduling(procs)
        show_result_window(result, "SJF Scheduling")

    tk.Button(root, text="FCFS", width=20, command=run_fcfs).pack(pady=5)
    tk.Button(root, text="SJF", width=20, command=run_sjf).pack(pady=5)
    tk.Button(root, text="Round Robin", width=20, command=open_rr_input_window).pack(pady=5)
    tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=20)

    root.mainloop()
