import csv
import os
from datetime import datetime, timedelta

class Timesheet:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_exists = os.path.isfile(file_path)
        self.grand_total_hours = 0.0

        if not self.file_exists:
            with open(self.file_path, mode = "w", newline = "") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Time In", "Time Out", "Total Hours"])
            self.file_exists = True

    def get_time(self, prompt):
        while True:
            time_input = input(prompt)
            try:
                return datetime.strptime(time_input, "%H:%M")
            except ValueError:
                print("Invalid time format. Use HH:MM")

    def round_down_to_quarter_hour(self, hours):
        total_minutes = int(hours * 60)
        rounded_minutes = (total_minutes //15) * 15
        return rounded_minutes / 60

    def add_entry(self):
        date = input("Enter date: ")
        time_in = self.get_time("Enter time in (HH:MM): ")
        time_out = self.get_time("Enter time out (HH:MM): ")

        if time_out <= time_in:
            time_out += timedelta(days=1)

        worked_time = time_out - time_in
        exact_hours = worked_time.total_seconds() / 3600
        total_hours = self.round_down_to_quarter_hour(exact_hours)

        with open(self.file_path, mode = "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([
                date,
                time_in.strftime("%H:%M"),
                time_out.strftime("%H:%M"),
                total_hours
            ])

        self.grand_total_hours += total_hours
        print(f"Timesheet saved! Total hours worked {total_hours}")

    def run(self):
        while True:
            self.add_entry()

            while True:
                choice = input("Add another entry? (y/n): ").lower()
                if choice == "y":
                    break
                elif choice == "n":
                    print(f"Hours to pay this cut-off: {round(self.grand_total_hours, 2)}")
                    return
                else:
                    print("Invalid choice. Please enter y or n.")

if __name__ == "__main__":
    FILE_NAME = r"C:\SAIT 1st Sem\OOP1\timesheet.csv"
    timesheet_app = Timesheet(FILE_NAME)
    timesheet_app.run()