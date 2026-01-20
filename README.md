# Timesheet

A simple command-line timesheet application written in Python that records work hours into a CSV file.
It calculates total hours worked, rounds time down to the nearest 15 minutes, and supports overnight shifts.

This project demonstrates:
A. File handling with CSV
B. Object-Oriented Programming (OOP)
C. Date & time calculations
D. User input validation

Key Features:
- Add daily work time entries
- Automatically creates a CSV file if it doesn’t exist
- Calculates total hours worked
- Rounds time down to the nearest quarter hour
- Handles overnight shifts (e.g., 22:00 – 06:00)
- Displays total payable hours at the end of a session

How It Works
1. Enter a date
2. Enter Time In and Time Out in HH:MM format
3. The program:
    a. Calculates total hours
    b. Rounds down to the nearest 15 minutes
    c. Saves the entry to a CSV file
    d. You can continue adding entries or exit to see the total hours worked

Time Rounding Rule:
*** 8.12 hours → 8.00
*** 8.26 hours → 8.25
*** 8.99 hours → 8.75
Rounding is always down to the nearest quarter hour.

Notes
1. Time format must be HH:MM (24-hour format)
2. The program does not validate dates (user input assumed correct)
3. Data persists between runs in the same CSV file
