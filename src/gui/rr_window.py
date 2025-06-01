import tkinter as tk
from tkinter import messagebox
from algorithms.rr import round_robin
from models.process import Process
from gui.result_window import show_result_window

def get_sample_processes():
    return [
        Process(1, 0, 5, priority=2),
        Process(2, 2, 3, priority=1),
        Process(3, 4, 1, priority=3),
    ]

def open_rr_input_window():
    win = tk.Toplevel()
    win.title("Round Robin Quantum")
    tk.Label(win, text="Enter Quantum:").pack(pady=5)
    entry = tk.Entry(win)
    entry.pack(pady=5)

    def run_rr():
        try:
            q = int(entry.get())
            if q <= 0:
                raise ValueError
            win.destroy()
            procs = get_sample_processes()
            result = round_robin(procs, q)
            show_result_window(result, f"Round Robin (Q={q})")
        except:
            messagebox.showerror("Invalid", "Quantum must be a positive integer.")

    tk.Button(win, text="Run", command=run_rr).pack(pady=5)
