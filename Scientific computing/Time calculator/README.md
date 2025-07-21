# Time Calculator
This Python program calculates the future time after adding a duration to a starting time.
It can also track the day of the week if provided and tell you how many days have passed.

This project is written using manual string parsing and math, not Python’s datetime module as this project is to get practise for manipulating strings,math and control flow manually.


## Description
This supports:
- 12-hour time format with AM/PM
- Minute and hour overflow
- Optional weekday tracking (e.g., starting from “Monday”)
- Day rollover calculation (e.g., next day, 2 days later)

### Features
- adds hours and minutes to any start time
- automatic AM -> PM flipping (vice versa)
- tracks days passed

### Example usage 
```
from time_calculator import add_time

print(add_time("11:06 PM", "2:02"))
# Output: 1:08 AM (next day)

print(add_time("3:30 PM", "2:12", "Monday"))
# Output: 5:42 PM, Monday

```

### Files 
- time_calculator.py – Core logic that handles time calculation

- test_module.py – Unit tests using Python’s unittest framework

- main.py or the entry script – Calls the function and runs tests

## Getting started

### Dependencies
- Python version 3.6 or above
- Python standard library
  
## Deployment
1. git clone this repository
2. in the cmd, navigate to this directory
3. run the rests
   ```
    python -m unittest test_module.py

   ```

## Author
Zaynab Khan  
zaynabkhan982@gmail.com

## License
This is registered under the MIT license
