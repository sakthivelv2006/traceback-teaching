# Traceback Reading Agent

## 1. Problem Statement

Build an agent that helps a beginner understand Python errors by teaching them how to read a traceback before modifying the code.

The system demonstrates this using three intentionally broken Python programs.

---

## 2. Objective

The main goal is not to automatically fix the program.

The goal is to teach the beginner how to:

1. Identify the error type.
2. Find the file where the error occurred.
3. Find the line number.
4. Understand the statement that caused the error.
5. Read the error message.
6. Understand the root cause.
7. Only then think about the fix.

---

## 3. Three Broken Programs

### Program 1 - NameError

A variable is used without being defined.

Example:

```python
price = 100
return priice * quantity