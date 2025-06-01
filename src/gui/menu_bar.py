import csv
from src.models.process import Process

def load_processes_from_csv(filepath: str) -> List[Process]:
    proceso_list = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pid = row["PID"]
            at = int(row["Arrival"])
            bt = int(row["Burst"])
            proceso_list.append(Process(pid, at, bt))
    return proceso_list

def save_results_to_csv(filepath: str, processes: List[Process]):
    with open(filepath, 'w', newline='') as csvfile:
        fieldnames = ["PID", "Arrival", "Burst", "Start", "Completion", "Waiting", "Turnaround"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for p in processes:
            writer.writerow({
                "PID": p.pid,
                "Arrival": p.arrival_time,
                "Burst": p.burst_time,
                "Start": p.start_time,
                "Completion": p.completion_time,
                "Waiting": p.waiting_time,
                "Turnaround": p.turnaround_time
            })
