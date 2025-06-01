import pytest
from src.models.process import Process
from src.algorithms.sjf import run_sjf

def test_sjf_simple():
    p1 = Process(pid="P1", arrival_time=0, burst_time=5)
    p2 = Process(pid="P2", arrival_time=2, burst_time=1)
    p3 = Process(pid="P3", arrival_time=4, burst_time=2)
    result = run_sjf([p1, p2, p3])

    assert [p.pid for p in result] == ["P1", "P2", "P3"]
    assert result[1].start_time == 5
    assert result[1].completion_time == 6
    assert result[2].start_time == 6
    assert result[2].completion_time == 8
