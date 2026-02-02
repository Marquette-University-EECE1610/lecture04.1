def is_even(n: int) -> bool:
    """Return True if n is even; otherwise False."""
    return n % 2 == 0


def is_valid_age(age: int) -> bool:
    """Valid ages are between 0 and 120 inclusive."""
    return age >= 0 and age <= 120


def main():
    print(f"is_even(4):        {is_even(4)}")
    print(f"is_even(7):        {is_even(7)}")
    print(f"is_valid_age(-1):  {is_valid_age(-1)}")
    print(f"is_valid_age(120): {is_valid_age(120)}\n")


if __name__ == "__main__":
    main()
