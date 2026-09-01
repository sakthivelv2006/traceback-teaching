import subprocess
import sys


def run_program(program_path):
    result = subprocess.run(
        [sys.executable, program_path],
        capture_output=True,
        text=True
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }