# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

# making the code interactive
start = input("Enter the start time (e.g., 3:30pm):)")
duration = input("Enter the duration (e.g. 2:12)")
day = input("Enter the day (optional): ")


# Handle optional day input cleanly
if day.strip() == "":
    result = add_time(start, duration)
else:
    result = add_time(start, duration, day)


print("Resulting time:")
print(result)

# Run unit tests automatically
main(module='test_module', exit=False)
