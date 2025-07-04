class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time

        # Results
        self.start_time = None
        self.completion_time = None
        self.turnaround_time = None
        self.waiting_time = None

    def copy(self):
        return Process(self.pid, self.arrival_time, self.burst_time, self.priority)