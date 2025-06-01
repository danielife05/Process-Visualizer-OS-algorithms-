import pytest
from src.models.process import Process
from src.algorithms.round_robin import run_round_robin

def test_rr_simple():
    p1 = Process(pid="P1", arrival_time=0, burst_time=4)
    p2 = Process(pid="P2", arrival_time=1, burst_time=3)
    # Quantum=2
    result = run_round_robin([p1, p2], quantum=2)
    for p in result:
        if p.pid == "P1":
            assert p.completion_time == 6
        if p.pid == "P2":
            assert p.completion_time == 7
