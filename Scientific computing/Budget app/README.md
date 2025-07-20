# Budget App

A python based budget application that allows users to track spending across various categories and visualize their expenses with a text-based chart.

## Description
This budget app is a Python-based personal finance tool that allows users to manage their money across customizable spending categories such as Food, Clothing, Auto, or anything else they choose. Each category functions like a digital envelope, where users can deposit funds, make withdrawals, and transfer money between envelopes as needed. Transactions are stored in a detailed ledger for each category, which can be printed in a clean, formatted summary. The app also includes a text-based spend chart that visually represents how much money has been spent per category as a percentage of total expenses, helping users understand their spending habits at a glance. Designed with simplicity and clarity in mind, this project demonstrates core object-oriented programming principles, modularity, and unit testing with unittest, making it a great example of clean Python design while also being practically useful.

## Features
- Create budget categories (e.g., Food, Entertainment, Business).
- Deposit funds with optional descriptions.
- Withdraw funds if sufficient balance exists.
- Transfer funds between categories.
- Print a clean ledger of all transactions.
- Generate a spending chart that shows where your money goes.


## Dependancies
Runs on Python's standard library (Python 3.6 or later)

## Deployment
  - clone the repository or download the files
  - run main.py script
  -  ```bash
   python main.py
  - run the unit tests
  -   python test_module.py
 
## Sample Output
text
Copy
Edit
*************Food*************
initial deposit        1000.00
restaurant and more f   -15.89
Transfer to Clothing    -50.00
Total: 934.11

Percentage spent by category
100|          
 90|          
 80|          
 70|    o     
 60|    o     
 ...
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g    



## Author
Zaynab Khan
email: zaynabkhan982@gmail.com

## License
The project is licensed under the MIT License
