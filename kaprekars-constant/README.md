# Kaprekar's Constant Calculator

A Python program that demonstrates Kaprekar's Constant (6174).

## Overview

Kaprekar's Constant is a mathematical process involving four-digit numbers.

Starting with any four-digit number containing at least two different digits:

1. Arrange the digits in descending order.
2. Arrange the digits in ascending order.
3. Subtract the smaller number from the larger number.
4. Repeat the process.

The result will eventually reach 6174, known as Kaprekar's Constant.

Example:
3524

5432 - 2354 = 3078
8730 - 0378 = 8352
8532 - 2358 = 6174


## Features

- Validates user input.
- Ensures the input is a valid four-digit number.
- Rejects numbers containing four identical digits.
- Calculates each iteration until 6174 is reached.
- Displays the calculation steps and number of iterations.

## Example Output
Please enter a 4 digit number: 3524

5432 - 2354 = 3078
8730 - 0378 = 8352
8532 - 2358 = 6174

Total steps = 3


## Concepts Demonstrated

- User input validation
- Functions
- String manipulation
- Lists and sorting
- Type conversion
- Loop control
- Returning values from functions

## Running the Program

Requirements:

- Python 3.x

Run:
python kaprekar.py

## Future Improvements

Possible enhancements:

- Calculate the maximum number of steps across all possible starting numbers.
- Add a graphical representation of the process.
- Store results for analysis.