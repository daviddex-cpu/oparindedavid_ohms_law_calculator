# Smart Ohm's Law & Power Calculator

## What it does
This program is a smart Ohm’s Law calculator that lets you find Voltage (V), Current (I), Resistance (R) or Power (P).  
It guides you step by step, handles wrong input cleanly, and after every calculation it gives you a practical engineering tip based on the power level (whether you need a heat sink, if it’s safe for small electronics, etc.).

It also keeps a live history of all calculations you make in the current session so you can review them anytime.

## How to run it
Install Python 3, then run:
```
python ohms_law_calculator.py
```
You can also run it on Android using Pydroid 3.

## Sample output
```
==================================================
   SMART OHM'S LAW & POWER CALCULATOR
==================================================
Calculate Voltage, Current, Resistance or Power
with engineering tips and calculation history.

Main Menu:
1. New Calculation
2. View History
3. Exit
Choose option (1-3): 1

What do you want to calculate?
1. Voltage (V)
2. Current (I)
3. Resistance (R)
4. Power (P)
Enter choice (1-4): 1
Enter Current (A): 0.5
Enter Resistance (Ω): 220

=============================================
RESULT
=============================================
Voltage = 110.0000 V
Details: I = 0.5 A, R = 220 Ω
Power   : 55.0000 W
---------------------------------------------
Engineering Tip:
Very high power → Requires serious thermal management & safety.
=============================================
```

## My own twist
- After every calculation the program gives a real engineering tip based on the power value (from “safe for sensors” to “needs serious heat management”).
- It keeps a full calculation history for the current session so you can review previous results without writing them down.

## What I learned
- How to structure a multi-option menu cleanly with functions.
- How to give the user useful feedback beyond just the raw number (engineering tips).
- How to store and display session history using a list of dictionaries.

## Author(Oparinde David)  
ND1 Mechatronics Engineering, YabaTech
