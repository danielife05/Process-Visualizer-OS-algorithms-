def priority_scheduling(processes):
    processes.sort(key=lambda p: (p.arrival_time, p.priority))
    time = 0
    completed = []

    while len(completed) < len(processes):
        ready = [p for p in processes if p.arrival_time <= time and p not in completed]
        if not ready:
            time += 1
            continue
        ready.sort(key=lambda p: p.priority)
        p = ready[0]

        p.start_time = time
        time += p.burst_time
        p.completion_time = time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        completed.append(p)

    return completed