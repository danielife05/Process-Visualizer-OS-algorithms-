import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox, simpledialog
from models.process import Process
from algorithms.fcfs import fcfs_scheduling
from algorithms.sjf import sjf_scheduling
from algorithms.rr import round_robin
from algorithms.priority import priority_scheduling
from gui.result_window import show_result_window

process_list = []

def open_custom_input_window():
    win = tk.Toplevel()
    win.title("Custom Process Input")
    win.geometry("400x400")
    win.configure(bg="#1e1e2f")

    # Listbox to display processes
    listbox = tk.Listbox(win, width=50, height=10, bg="#2c2c3c", fg="white", selectbackground="#444")
    listbox.pack(pady=10)

    # Entry for quantum
    tk.Label(win, text="Quantum (RR):", bg="#1e1e2f", fg="white").pack()
    quantum_entry = tk.Entry(win)
    quantum_entry.insert(0, "2")
    quantum_entry.pack(pady=5)

    def refresh_listbox():
        listbox.delete(0, tk.END)
        for p in process_list:
            listbox.insert(tk.END, f"PID {p.pid} - Arrival {p.arrival_time} - Burst {p.burst_time} - Priority {p.priority}")

    def add_process():
        form_process(win, refresh_listbox)

    def edit_process():
        idx = listbox.curselection()
        if not idx:
            return messagebox.showwarning("Select", "Please select a process to edit.")
        process = process_list[idx[0]]
        form_process(win, refresh_listbox, process, idx[0])

    def delete_process():
        idx = listbox.curselection()
        if not idx:
            return messagebox.showwarning("Select", "Please select a process to delete.")
        del process_list[idx[0]]
        refresh_listbox()

    def form_process(parent, refresh_callback, process=None, index=None):
        form = tk.Toplevel(parent)
        form.title("Process Form")
        form.configure(bg="#1e1e2f")
        form.geometry("300x250")

    def save_to_file():
        if not process_list:
            return messagebox.showwarning("Empty", "No processes to save.")
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["PID", "ArrivalTime", "BurstTime", "Priority"])
            for p in process_list:
                writer.writerow([p.pid, p.arrival_time, p.burst_time, p.priority])
        messagebox.showinfo("Saved", "Process list saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file:\n{e}")

def load_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            loaded = []
            for row in reader:
                loaded.append(Process(
                    int(row["PID"]),
                    int(row["ArrivalTime"]),
                    int(row["BurstTime"]),
                    int(row["Priority"])
                ))
        process_list.clear()
        process_list.extend(loaded)
        refresh_listbox()
        messagebox.showinfo("File Loaded")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file:\n{e}")

    # Fields
    entries = {}
    for i, (label, default) in enumerate([
        ("PID", process.pid if process else ""),
        ("Arrival Time", process.arrival_time if process else ""),
        ("Burst Time", process.burst_time if process else ""),
        ("Priority", process.priority if process else 1),
    ]):
        tk.Label(form, text=label, bg="#1e1e2f", fg="white").pack()
        entry = tk.Entry(form)
        entry.insert(0, str(default))
        entry.pack()
        entries[label] = entry

    def save():
        try:
            pid = int(entries["PID"].get())
            at = int(entries["Arrival Time"].get())
            bt = int(entries["Burst Time"].get())
            pr = int(entries["Priority"].get())
            new_proc = Process(pid, at, bt, pr)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            return

        if index is not None:
            process_list[index] = new_proc
        else:
            process_list.append(new_proc)

        refresh_callback()
        form.destroy()

    tk.Button(form, text="Save", command=save, bg="#3a3a5c", fg="white").pack(pady=10)


    def run_all():
        if not process_list:
            return messagebox.showerror("Error", "No processes to run.")
        try:
            quantum = int(quantum_entry.get())
            if quantum <= 0:
                raise ValueError
        except:
            return messagebox.showerror("Error", "Quantum must be a positive integer.")

        # Run all algorithms using copies
        show_result_window(fcfs_scheduling([p.copy() for p in process_list]), "FCFS")
        show_result_window(sjf_scheduling([p.copy() for p in process_list]), "SJF")
        show_result_window(round_robin([p.copy() for p in process_list], quantum), f"Round Robin (Q={quantum})")
        show_result_window(priority_scheduling([p.copy() for p in process_list]), "Priority")

    # Buttons
    btn_frame = tk.Frame(win, bg="#1e1e2f")
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="Add", width=10, command=add_process, bg="#3a3a5c", fg="white").grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Edit", width=10, command=edit_process, bg="#3a3a5c", fg="white").grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Delete", width=10, command=delete_process, bg="#8b1e1e", fg="white").grid(row=0, column=2, padx=5)
    tk.Button(win, text="Run All", width=20, command=run_all, bg="#2d885d", fg="white").pack(pady=15)
    file_frame = tk.Frame(win, bg="#1e1e2f")
    file_frame.pack(pady=5)
    tk.Button(file_frame, text="Save to File", command=save_to_file, bg="#1b5e20", fg="white").grid(row=0, column=0, padx=5)
    tk.Button(file_frame, text="Load from File", command=load_from_file, bg="#0d47a1", fg="white").grid(row=0, column=1, padx=5)

