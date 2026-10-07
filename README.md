# Ghana T-Bill Calculator

A Python command-line tool that compares investing in a Ghana Treasury Bill against a fixed deposit, so you can see which one gives more money at maturity.

## Features
- Calculates T-Bill price and interest rate equivalent from the discount rate
- Calculates maturity value for a T-Bill and a fixed deposit
- Compares the two and shows the winner
- Input validation, so bad entries don't crash the program

## How to run
1. Install Python 3
2. Clone this repo
3. Run `py tbill.py` (Windows) or `python3 tbill.py` (Mac/Linux)

## Example
Investing GH₵10,000 for 91 days, with a 25% T-Bill discount rate and a 22% fixed deposit rate:

    T-Bill value:        GH₵10,666.67
    Fixed deposit value: GH₵10,548.49
    Winner: T-Bill by GH₵118.18

## How it works
- T-Bill price = 100 × (1 − discount rate × days / 364)
- Fixed deposit value = amount × (1 + rate × days / 365)

## Roadmap
- Charts showing growth over time
- Support for different T-Bill tenors side by side

## Author
Claudia Lartey