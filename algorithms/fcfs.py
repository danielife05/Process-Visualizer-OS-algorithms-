def fcfs_scheduling(processes):
    processes.sort(key=lambda p: p.arrival_time)
    current_time = 0

    for p in processes:
        if current_time < p.arrival_time:
            current_time = p.arrival_time
        p.start_time = current_time
        p.completion_time = current_time + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.start_time - p.arrival_time
        current_time = p.completion_time

    return processes