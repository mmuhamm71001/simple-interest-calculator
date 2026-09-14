# Simple Interest Calculator

A simple Python command-line program that calculates **simple interest** based on a given principal amount, annual interest rate, and time period.

## What is Simple Interest?

Simple interest is a quick method of calculating the interest charge on a loan or the interest earned on an investment. It is calculated only on the original principal amount, unlike compound interest, which is calculated on the principal plus any accumulated interest.

## Formula

```
Simple Interest (SI) = (P x R x T) / 100
```

Where:
- **P** = Principal amount (the initial sum of money)
- **R** = Annual interest rate (in percent)
- **T** = Time period (in years)

The total amount after interest is applied is calculated as:

```
Total Amount = P + SI
```

## Features

- Calculates simple interest given principal, rate, and time
- Calculates the total amount (principal + interest)
- Validates input to ensure non-negative values
- Simple, interactive command-line interface

## Files

| File | Description |
|---|---|
| `simple_interest_calculator.py` | Main script containing the calculator logic and CLI |

## How to Use

1. Clone this repository:
   ```
   git clone <repository-url>
   ```
2. Navigate into the project directory:
   ```
   cd <repository-folder>
   ```
3. Run the script using Python 3:
   ```
   python3 simple_interest_calculator.py
   ```
4. Enter the requested values when prompted:
   - Principal amount
   - Annual interest rate (%)
   - Time period (years)

## Example

```
=== Simple Interest Calculator ===
Enter principal amount: 1000
Enter annual interest rate (%): 5
Enter time period (years): 2

Principal Amount : 1000.00
Interest Rate    : 5.00%
Time Period      : 2.00 year(s)
Simple Interest  : 100.00
Total Amount     : 1100.00
```

## Requirements

- Python 3.x (no external libraries required)

## License

This project is open source and available for personal or educational use.
