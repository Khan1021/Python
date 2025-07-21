# Probability Calculator
This project uses object oriented Python and random simulations to mimic probability experiments. 

## Description
This project simulates drawing coloured balls from a har and uses that to estimate the probability of drawing a specific combination of balls.

### Features
- create a hat with any number of coloured balls
- randomly draw balls out of the hat
- run simulations of drawing the balls to estimate the probability of drawing specific colours
- includes automated tests

### Example Usage
  
  `hat = Hat(red=3, blue=2)
probability = experiment(
    hat=hat,
    expected_balls={"red": 2},
    num_balls_drawn=3,
    num_experiments=1000
)
print("Probability:", probability)`

### Files
- `prob_calculator.py`: core logic
- `test_module.py`: Unit tests
- `main.py`: example execution and test runner

## Getting Started
### Dependencies
- Python verstion 3.6 or above
- Python standard library

## Deployment
1. git clone this repository on your local device
2. in the cmd, navigate to this folder directory
3. still in cmd and directory, `python -m unittest test_module.py`

This will execute the unit tests

## Authors
Zaynab Khan
zaynabkhan982@gmail.com 

## License
This project is licensed the MIT license.
