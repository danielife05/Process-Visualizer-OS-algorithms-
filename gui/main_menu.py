import tkinter as tk
from algorithms.fcfs import fcfs_scheduling
from algorithms.sjf import sjf_scheduling
from algorithms.priority import priority_scheduling
from models.process import Process
from gui.result_window import show_result_window
from gui.rr_window import open_rr_input_window

def get_sample_processes():
    return [
        Process(1, 0, 5, priority=2),
        Process(2, 2, 3, priority=1),
        Process(3, 4, 1, priority=3),
    ]

def launch_main_menu():
    root = tk.Tk()
    window_width = 300
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.title("Process Scheduler")
    root.geometry("350x320")
    root.configure(bg="#1e1e2f")  # Fondo oscuro, puedes usar otro color hex
    root.resizable(False, False)
    root.iconbitmap("utils/icons/logo.ico")  # Asegúrate de tener el archivo en la misma carpeta que main.py

    tk.Label(root, text="Choose Scheduling Algorithm:", font=("Arial", 12)).pack(pady=15)

    def run_fcfs():
        procs = get_sample_processes()
        result = fcfs_scheduling(procs)
        show_result_window(result, "FCFS Scheduling")

    def run_sjf():
        procs = get_sample_processes()
        result = sjf_scheduling(procs)
        show_result_window(result, "SJF Scheduling")
    
    def run_priority():
        procs = get_sample_processes()
        result = priority_scheduling(procs)
        show_result_window(result, "Priority Scheduling")

    tk.Button(root, text="FCFS", width=20, command=run_fcfs, bg="#3a3a5c", fg="white").pack(pady=5)
    tk.Button(root, text="SJF", width=20, command=run_sjf, bg="#3a3a5c", fg="white").pack(pady=5)
    tk.Button(root, text="Round Robin", width=20, command=open_rr_input_window, bg="#3a3a5c", fg="white").pack(pady=5)
    tk.Button(root, text="Priority", width=20, command=run_priority, bg="#3a3a5c", fg="white").pack(pady=5)
    tk.Button(root, text="Exit", width=20, command=root.destroy, bg="#8b1e1e", fg="white").pack(pady=20)

    root.mainloop()