import tkinter as tk
from tkinter import ttk, messagebox
from src.models.process import Process
from src.algorithms.fcfs import run_fcfs
from src.algorithms.sjf import run_sjf
from src.algorithms.rr import run_round_robin
from src.utils.metrics import average_waiting_time, average_turnaround_time, average_response_time

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Visualizador de Planificación de Procesos")
        self.process_list = []

        self._create_form()
        self._create_algorithm_selector()
        self._create_simulation_button()
        self._create_canvas_gantt()
        self._create_metrics_panel()

    def _create_form(self):
        tk.Label(self, text="PID:").grid(row=0, column=0, pady=5)
        self.pid_entry = tk.Entry(self)
        self.pid_entry.grid(row=0, column=1)
        tk.Label(self, text="Tiempo de llegada:").grid(row=1, column=0)
        self.arrival_entry = tk.Entry(self)
        self.arrival_entry.grid(row=1, column=1)
        tk.Label(self, text="Ráfaga de CPU:").grid(row=2, column=0)
        self.burst_entry = tk.Entry(self)
        self.burst_entry.grid(row=2, column=1)
        add_btn = tk.Button(self, text="Agregar proceso", command=self._add_process)
        add_btn.grid(row=3, column=0, columnspan=2, pady=10)

    def _create_algorithm_selector(self):
        tk.Label(self, text="Algoritmo:").grid(row=4, column=0)
        self.alg_var = tk.StringVar()
        self.alg_dropdown = ttk.Combobox(self, textvariable=self.alg_var,
                                         values=["FCFS", "SJF", "Round Robin"])
        self.alg_dropdown.grid(row=4, column=1)
        self.quantum_label = tk.Label(self, text="Quantum:")
        self.quantum_entry = tk.Entry(self)
        self.quantum_label.grid_forget()
        self.quantum_entry.grid_forget()
        self.alg_var.trace("w", self._on_algorithm_change)

    def _on_algorithm_change(self, *args):
        if self.alg_var.get() == "Round Robin":
            self.quantum_label.grid(row=5, column=0)
            self.quantum_entry.grid(row=5, column=1)
        else:
            self.quantum_label.grid_forget()
            self.quantum_entry.grid_forget()

    def _add_process(self):
        pid = self.pid_entry.get().strip()
        try:
            at = int(self.arrival_entry.get())
            bt = int(self.burst_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Arrival y Burst deben ser enteros.")
            return

        if any(p.pid == pid for p in self.process_list):
            messagebox.showerror("Error", f"El PID '{pid}' ya existe.")
            return
        new_proc = Process(pid=pid, arrival_time=at, burst_time=bt)
        self.process_list.append(new_proc)
        messagebox.showinfo("Éxito", f"Proceso {pid} agregado.")

        self.pid_entry.delete(0, tk.END)
        self.arrival_entry.delete(0, tk.END)
        self.burst_entry.delete(0, tk.END)

    def _create_simulation_button(self):
        sim_btn = tk.Button(self, text="Simular", command=self._simulate)
        sim_btn.grid(row=6, column=0, columnspan=2, pady=10)

    def _create_canvas_gantt(self):
        self.gantt_canvas = tk.Canvas(self, width=600, height=200, bg="white")
        self.gantt_canvas.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def _create_metrics_panel(self):
        self.metrics_label = tk.Label(self, text="", justify="left")
        self.metrics_label.grid(row=8, column=0, columnspan=2, sticky="w", padx=10)

    def _simulate(self):
        alg = self.alg_var.get()
        if not alg:
            messagebox.showerror("Error", "Seleccione un algoritmo.")
            return
        if len(self.process_list) == 0:
            messagebox.showerror("Error", "Debe agregar al menos un proceso.")
            return

        procs_copy = [p for p in self.process_list]
        if alg == "FCFS":
            result = run_fcfs(procs_copy)
        elif alg == "SJF":
            result = run_sjf(procs_copy)
        else:  # Round Robin
            try:
                q = int(self.quantum_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Quantum debe ser entero.")
                return
            if q <= 0:
                messagebox.showerror(
                    "Error",
                    "Quantum inválido: debe ser un entero positivo mayor que 0."
                )
                return
            result = run_round_robin(procs_copy, quantum=q)

        self._draw_gantt(result)

        aws = average_waiting_time(result)
        ats = average_turnaround_time(result)
        ars = average_response_time(result)
        metrics_text = f"Tiempo de espera promedio: {aws:.2f}\n"
        metrics_text += f"Turnaround promedio: {ats:.2f}\n"
        metrics_text += f"Response time promedio: {ars:.2f}"
        self.metrics_label.config(text=metrics_text)

    def _draw_gantt(self, processes):
        self.gantt_canvas.delete("all")
        if not processes:
            return

        max_time = max(p.completion_time for p in processes)
        canvas_width = int(self.gantt_canvas["width"])
        canvas_height = int(self.gantt_canvas["height"])
        unit_width = canvas_width / (max_time + 1)

        for t in range(0, max_time + 1):
            x = t * unit_width
            self.gantt_canvas.create_line(x, canvas_height - 20, x, canvas_height - 15)
            self.gantt_canvas.create_text(x, canvas_height - 10, text=str(t), anchor="n", font=("Arial", 8))

        y_offset = 10
        for p in processes:
            x0 = p.start_time * unit_width
            x1 = p.completion_time * unit_width
            y0 = y_offset
            y1 = y_offset + 20
            self.gantt_canvas.create_rectangle(x0, y0, x1, y1, fill="skyblue", outline="black")
            self.gantt_canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2,
                                          text=p.pid, fill="black", font=("Arial", 10, "bold"))
            y_offset += 30

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
