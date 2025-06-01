def is_positive_int(value: str) -> bool:
    try:
        return int(value) >= 0
    except ValueError:
        return False

def format_pid(pid: str) -> str:
    return pid.strip().upper()
