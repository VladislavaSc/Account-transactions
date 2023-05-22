# Code for the 'Account Transactions' widget

The IT department of bank is making a new feature for the client's personal account. This's a widget that shows the client's last few successful banking transactions.


TASK

Implement a function that displays a list of the last 5 operations performed by the client in the format:

<transfer date><transfer description><from> -> <to><transfer amount><currency>
  
 # Sample output for one operation:
 
 14.10.2018 Organization transfer Visa Platinum 7000 79** **** 6361 -> Account **9638 82771.72 rub.
  
 # REQUIREMENTS
  
  The last 5 executed (EXECUTED) operations are displayed.
  Operations are separeted by an empty line.
  The transfer date is presented in the format DD.MM.YYYY
  At the top of the list are the most recent transactions (by date).
  The card number is masked and not displayed in its entirety in the XXXX XX** **** XXXX format.
  The account number is masked and not displayed in its entirety in the **XXXX format.
  
  # DATA
