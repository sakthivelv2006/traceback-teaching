import re


def parse_traceback(traceback):
    lines = traceback.strip().splitlines()

    error_type = "UnknownError"
    message = traceback
    file_name = None
    line_number = None
    code_line = None

    for line in lines:

        # Find file and line
        match = re.search(r'File "(.+)", line (\d+)', line)

        if match:
            file_name = match.group(1)
            line_number = int(match.group(2))

        # Find the actual code line
        if line.strip() and not line.startswith("Traceback"):
            if not line.startswith("File"):
                code_line = line.strip()

        # Find error type
        error_match = re.search(
            r'(\w+(?:Error|Exception|Warning)):\s*(.*)',
            line
        )

        if error_match:
            error_type = error_match.group(1)
            message = error_match.group(2)

    return {
        "error_type": error_type,
        "message": message,
        "file": file_name,
        "line": line_number,
        "code": code_line
    }