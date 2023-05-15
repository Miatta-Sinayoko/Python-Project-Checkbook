Python Project
Command Line Checkbook Application
You will create a command line checkbook application that allows users to track their financeswith a command line interface.
Project Requirements
Build a
.py
file that will be run from the command line.
When run, the application should welcome the user, and prompt them for an action totake:
view current balance
add a debit (withdrawal)
add a credit (deposit)
exit
The application should notify the user if the input is invalid and prompt for anotherchoice.
The application should persist between times that it is run.
Example, if you run the application, add some credits, exit the application and run itagain, you should still see the balance that you previously created. In order to do this,your application will need to store its data in a text file. Consider creating a file whereeach line in the file represents a single transaction.
Utilize functions to call the balance, debit, credit, and exit
Example Ouput
Here is an example of what using the program might look like:
$ python checkbook.py ~~~ Welcome to your terminal checkbook! ~~~
5/12/23, 5:07 PM Python Checkbook Project - Codeup Data Science
https://ds.codeup.com/python/project/ 2/3
Bonus Features
What would you like to do? 1) view current balance 2) record a debit (withdraw) 3) record a credit (deposit) 4) exit Your choice? 5 Invalid choice: 5 Your choice? 1 Your current balance is $100.00. What would you like to do? 1) view current balance 2) record a debit (withdraw) 3) record a credit (deposit) 4) exit Your choice? 2 How much is the debit? $50 What would you like to do? 1) view current balance 2) record a debit (withdraw) 3) record a credit (deposit) 4) exit Your choice? 1 Your current balance is $50.00. What would you like to do? 1) view current balance 2) record a debit (withdraw) 3) record a credit (deposit) 4) exit Your choice? 4 Thanks, have a great day!