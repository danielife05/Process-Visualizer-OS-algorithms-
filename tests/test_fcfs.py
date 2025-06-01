import pytest
from src.models.process import Process
from src.algorithms.fcfs import run_fcfs

def test_fcfs_simple():
    p1 = Process(pid="P1", arrival_time=0, burst_time=3)
    p2 = Process(pid="P2", arrival_time=1, burst_time=2)
    p3 = Process(pid="P3", arrival_time=2, burst_time=1)
    result = run_fcfs([p1, p2, p3])

    assert [p.pid for p in result] == ["P1", "P2", "P3"]

    assert result[0].start_time == 0
    assert result[0].completion_time == 3
    assert result[1].start_time == 3
    assert result[1].completion_time == 5
    assert result[2].start_time == 5
    assert result[2].completion_time == 6

    assert result[0].waiting_time == 0
    assert result[1].waiting_time == 2
    assert result[2].waiting_time == 3
