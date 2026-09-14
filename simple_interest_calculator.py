"""
Simple Interest Calculator
---------------------------
Calculates simple interest given a principal amount, annual interest rate,
and time period, using the formula:

    Simple Interest (SI) = (P * R * T) / 100

Where:
    P = Principal amount
    R = Annual interest rate (in percent)
    T = Time period (in years)
"""


def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate simple interest.

    Args:
        principal: The initial amount of money (P).
        rate: The annual interest rate, in percent (R).
        time: The time period, in years (T).

    Returns:
        The simple interest amount.
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative.")

    return (principal * rate * time) / 100


def calculate_total_amount(principal: float, rate: float, time: float) -> float:
    """
    Calculate the total amount (principal + interest).

    Args:
        principal: The initial amount of money (P).
        rate: The annual interest rate, in percent (R).
        time: The time period, in years (T).

    Returns:
        The total amount after interest is applied.
    """
    interest = calculate_simple_interest(principal, rate, time)
    return principal + interest


def main():
    print("=== Simple Interest Calculator ===")
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time period (years): "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    try:
        interest = calculate_simple_interest(principal, rate, time)
        total = calculate_total_amount(principal, rate, time)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"\nPrincipal Amount : {principal:.2f}")
    print(f"Interest Rate    : {rate:.2f}%")
    print(f"Time Period      : {time:.2f} year(s)")
    print(f"Simple Interest  : {interest:.2f}")
    print(f"Total Amount     : {total:.2f}")


if __name__ == "__main__":
    main()
