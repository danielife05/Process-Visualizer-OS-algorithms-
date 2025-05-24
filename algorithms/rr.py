from collections import deque

def round_robin(processes, quantum):
    queue = deque()
    current_time = 0
    completed = []
    remaining = processes[:]

    while remaining or queue:
        for p in remaining[:]:
            if p.arrival_time <= current_time and p not in queue:
                queue.append(p)
                remaining.remove(p)

        if not queue:
            current_time += 1
            continue

        p = queue.popleft()
        if p.start_time is None:
            p.start_time = current_time

        exec_time = min(p.remaining_time, quantum)
        p.remaining_time -= exec_time
        current_time += exec_time

        for new_p in remaining[:]:
            if new_p.arrival_time <= current_time and new_p not in queue:
                queue.append(new_p)
                remaining.remove(new_p)

        if p.remaining_time > 0:
            queue.append(p)
        else:
            p.completion_time = current_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            completed.append(p)

    return completed
