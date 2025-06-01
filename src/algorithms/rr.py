from typing import List, Tuple
from src.models.process import Process
import copy

def run_round_robin(process_list: List[Process], quantum: int) -> List[Process]:
    processes = sorted([copy.copy(p) for p in process_list], key=lambda p: p.arrival_time)
    time_elapsed = 0
    ready_queue = []
    resultado = []

    idx = 0
    while idx < len(processes) or ready_queue:
        while idx < len(processes) and processes[idx].arrival_time <= time_elapsed:
            processes[idx].remaining_burst = processes[idx].burst_time
            ready_queue.append(processes[idx])
            idx += 1
        if not ready_queue:
            time_elapsed = processes[idx].arrival_time
            continue
        current = ready_queue.pop(0)

        if not hasattr(current, 'start_time') or current.start_time is None:
            current.start_time = time_elapsed

        executed = min(current.remaining_burst, quantum)
        time_elapsed += executed
        current.remaining_burst -= executed

        while idx < len(processes) and processes[idx].arrival_time <= time_elapsed:
            processes[idx].remaining_burst = processes[idx].burst_time
            ready_queue.append(processes[idx])
            idx += 1
        if current.remaining_burst > 0:
            ready_queue.append(current)
        else:
            current.completion_time = time_elapsed
            current.turnaround_time = current.completion_time - current.arrival_time
            current.waiting_time = current.turnaround_time - current.burst_time
            resultado.append(current)
            
    return resultado