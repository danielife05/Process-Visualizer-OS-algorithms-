import tkinter as tk
from tkinter import ttk
from utils.visualizer import plot_gantt_in_tk

def show_result_window(processes, title):
    window = tk.Toplevel()
    window.title(title)
    window.geometry("600x400")

    table_frame = ttk.Frame(window)
    table_frame.pack(pady=10)

    columns = ("PID", "Arrival", "Burst", "Start", "Completion", "Waiting", "Turnaround")
    tree = ttk.Treeview(table_frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=80, anchor="center")
    tree.pack()

    for p in processes:
        tree.insert('', 'end', values=(
            p.pid, p.arrival_time, p.burst_time, p.start_time,
            p.completion_time, p.waiting_time, p.turnaround_time
        ))

    plot_gantt_in_tk(processes, title, window)
