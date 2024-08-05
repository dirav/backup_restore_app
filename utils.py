import subprocess

def get_current_date():
    return subprocess.check_output(["date", "+%F"]).decode("utf-8").strip()
