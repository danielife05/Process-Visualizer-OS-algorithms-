def sjf_scheduling(processes):
    completed = []
    current_time = 0
    ready_queue = []

    while len(completed) < len(processes):
        for p in processes:
            if p.arrival_time <= current_time and p not in completed and p not in ready_queue:
                ready_queue.append(p)

        if not ready_queue:
            current_time += 1
            continue

        ready_queue.sort(key=lambda p: p.burst_time)
        p = ready_queue.pop(0)

        p.start_time = current_time
        p.completion_time = current_time + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.start_time - p.arrival_time
        current_time = p.completion_time
        completed.append(p)

    return completed
