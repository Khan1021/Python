# Arithmetic Formatter

This Python project takes a list of arithmetic problems and returns them formatted vertically and side-by-side, with optional solutions. This project covers string manipulation, input validation, and conditional logic.

## Description

This supports:
- addition and subtraction
- up to 5 problems at once
- input validation

### Features


### Example usage

#### example 1 (no solution):

```python
from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
```
output (with no solution):

```python
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

#### example 2 (with solution):

```python
pythonprint(arithmetic_arranger(["32 + 698", "1 - 3801"], solve=True))
```

output (with solution):

```python
   32         1
+ 698    - 3801
-----    ------
  730     -3800

```

### Files

- ```arithmetic_arranger.py``` - core logic to format arithmetic problems
- ```test_arithmetic_arranger.py``` Unit tests using pytest
- ```README.md```  

## Getting Started

### Dependencies

- Python version 3.6 or above
- standard Python library
- to install 'pytest' if needed (for testing):
  ``` bash
  pip install pytest
  ```
  
### Deployment

1. Clone the repository  ```git clone https://github.com/Khan1021/Python.git```
2. Change to this folder in cmd  ```cd "Python/Scientific computing/Arithmetic Formatter"```
3. Install dependecy on cmd or bash (pytest (above))
4. Testing the code is available by opening a Python file or interpreter and inputting
   
   ```python
   from arithmetic_arranger import arithmetic_arranger
   print(arithmetic_arranger(["3 + 855", "988 + 40"], solve=True))
   ```
   
6. To check the everything works properly
   ```
   pytest -vv
   ```
   
## Authors

Zaynab Khan  
zaynabkhan982@gmail.com

## License

This project is under the license of the MIT License
