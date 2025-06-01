from typing import List
from src.models.process import Process

def average_waiting_time(processes: List[Process]) -> float:
    total = sum(p.waiting_time for p in processes)
    return total / len(processes) if processes else 0.0

def average_turnaround_time(processes: List[Process]) -> float:
    total = sum(p.turnaround_time for p in processes)
    return total / len(processes) if processes else 0.0

def average_response_time(processes: List[Process]) -> float:
    total = sum(p.start_time - p.arrival_time for p in processes)
    return total / len(processes) if processes else 0.0
