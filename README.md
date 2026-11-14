# Debt Tracker

A beginner Python project that tracks how much a person borrowed,
how much they have paid, and what they still owe.

## What it does
- Stores a person's name and the amount borrowed
- Records payments with two guards: no zero or negative payments,
  and no payment bigger than the remaining balance
- Reports the balance and whether the debt is CLEARED or OWING

## Version 1
The Debt class with its methods (make_payment, is_cleared, balance,
summary), tested with fixed values written in the code.

## Version 2
Rebuilt from my own plan, without looking at v1:
- Asks the user for the name, amount borrowed and payments
- Rejects letters and asks again until the input is a number
- Keeps taking payments until the debt is cleared
- Uses balance() everywhere instead of repeating the sum
- Prints the summary once at the end

## How to run
v1 (runs fixed test values):
```
python debt_tracker_v1.py
```
v2 (asks you for the name, amount and payments):
```
python debt_tracker_v2.py
```
## What I learned
Classes and `__init__`, guard's with early return, try/except, loops with break, and calling my own methods with self.d

## Next
Let the user quit early and show the debt as still OWING.
