from typing import List
from src.models.process import Process

def run_sjf(process_list: List[Process]) -> List[Process]:
    processes = sorted(process_list, key=lambda p: p.arrival_time)
    time_elapsed = 0
    ready_queue = []
    result = []

    while processes or ready_queue:
        while processes and processes[0].arrival_time <= time_elapsed:
            ready_queue.append(processes.pop(0))
        if not ready_queue:

            time_elapsed = processes[0].arrival_time
            continue

        next_proc = min(ready_queue, key=lambda p: p.burst_time)
        ready_queue.remove(next_proc)
        next_proc.start_time = time_elapsed
        next_proc.completion_time = time_elapsed + next_proc.burst_time
        next_proc.turnaround_time = next_proc.completion_time - next_proc.arrival_time
        next_proc.waiting_time = next_proc.start_time - next_proc.arrival_time
        time_elapsed = next_proc.completion_time
        result.append(next_proc)

    return result