# Budget App

Apython based budget application that allows users to track spending across various categories and visualize their expenses with a text-based chart.

## Features
- Create budget categories (e.g., Food, Entertainment, Business).
- Deposit funds with optional descriptions.
- Withdraw funds if sufficient balance exists.
- Transfer funds between categories.
- Print a clean ledger of all transactions.
- Generate a spending chart that shows where your money goes.

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


## License
The project is licensed under the MIT License
