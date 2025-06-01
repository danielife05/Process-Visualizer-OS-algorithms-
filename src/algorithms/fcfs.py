from typing import List
from src.models.process import Process

def run_fcfs(process_list: List[Process]) -> List[Process]:
    processes = sorted(process_list, key=lambda p: p.arrival_time)
    time_elapsed = 0

    for p in processes:
        if time_elapsed < p.arrival_time:
            time_elapsed = p.arrival_time
        p.start_time = time_elapsed
        p.completion_time = time_elapsed + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.start_time - p.arrival_time
        time_elapsed = p.completion_time

    return processes