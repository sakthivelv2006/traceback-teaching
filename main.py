from runner import run_program
from parser import parse_traceback
from agent import teach


PROGRAMS = {
    "1": "programs/program1.py",
    "2": "programs/program2.py",
    "3": "programs/program3.py"
}

def main():

    print("========================================")
    print("       TRACEBACK READING AGENT")
    print("========================================")

    print("\nChoose a broken program:")
    print("1. NameError")
    print("2. TypeError")
    print("3. IndexError")

    choice = input("\nEnter your choice: ")

    if choice not in PROGRAMS:
        print("Invalid choice.")
        return

    program = PROGRAMS[choice]

    print("\nRunning program...")
    print("----------------------------------------")

    result = run_program(program)

    if result["returncode"] == 0:
        print(result["stdout"])
        return

    traceback = result["stderr"]

    parsed_error = parse_traceback(traceback)

    teach(parsed_error)


if __name__ == "__main__":
    main()