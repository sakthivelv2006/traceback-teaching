def teach(parsed_error):

    error_type = parsed_error["error_type"]
    message = parsed_error["message"]
    file_name = parsed_error["file"]
    line_number = parsed_error["line"]
    code = parsed_error["code"]

    print("\n========================================")
    print("        TRACEBACK TEACHER AGENT")
    print("========================================")

    print("\nSTEP 1 — IDENTIFY THE ERROR")
    print("----------------------------------------")
    print(f"Error type : {error_type}")

    print("\nSTEP 2 — FIND WHERE IT HAPPENED")
    print("----------------------------------------")
    print(f"File       : {file_name}")
    print(f"Line       : {line_number}")

    print("\nSTEP 3 — LOOK AT THE STATEMENT")
    print("----------------------------------------")
    print(f"Code       : {code}")

    print("\nSTEP 4 — UNDERSTAND THE MESSAGE")
    print("----------------------------------------")
    print(f"Python says: {message}")

    print("\nSTEP 5 — WHAT DOES IT MEAN?")
    print("----------------------------------------")

    if error_type == "NameError":
        print(
            "Python tried to use a variable or name that "
            "has not been defined."
        )

    elif error_type == "TypeError":
        print(
            "Python tried to perform an operation using "
            "incompatible data types."
        )

    elif error_type == "IndexError":
        print(
            "Python tried to access an index that does "
            "not exist in the sequence."
        )

    else:
        print(
            "The program raised an error. "
            "Use the traceback location and message "
            "to investigate the root cause."
        )

    print("\nSTEP 6 — THINK BEFORE FIXING")
    print("----------------------------------------")
    print(
        "First understand why this statement failed. "
        "Only after understanding the cause should "
        "we modify the code."
    )

    print("\n========================================")