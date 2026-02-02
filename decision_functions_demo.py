"""
decision_functions_demo.py

Live demo code for branching/booleans/conditionals using functions.
Designed for early CS1: readable, testable, and focused on decision logic.
"""

def is_even(n: int) -> bool:
    """Return True if n is even; otherwise False."""
    return n % 2 == 0


def is_valid_age(age: int) -> bool:
    """Valid ages are between 0 and 120 inclusive."""
    return age >= 0 and age <= 120


def letter_grade(score: int) -> str:
    """Return a letter grade based on a 0–100 score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def classify_temperature(temp_f: float) -> str:
    """Classify a temperature in Fahrenheit into a human-friendly category."""
    if temp_f < 32:
        return "Freezing"
    elif temp_f <= 59:
        return "Cold"
    elif temp_f <= 79:
        return "Comfortable"
    else:
        return "Hot"


def validate_password(pw: str) -> str:
    """
    Return:
      - "Too short" if len(pw) < 8
      - "No digit" if pw contains no digits
      - "Valid" otherwise

    Note: Implemented without loops to match early-course constraints.
    """
    if len(pw) < 8:
        return "Too short"

    has_digit = (
        ("0" in pw) or ("1" in pw) or ("2" in pw) or ("3" in pw) or ("4" in pw) or
        ("5" in pw) or ("6" in pw) or ("7" in pw) or ("8" in pw) or ("9" in pw)
    )
    if not has_digit:
        return "No digit"

    return "Valid"


def shipping_cost(weight: float, is_member: bool):
    """
    Return either:
      - "Invalid weight" (string) if weight <= 0
      - A non-negative numeric cost otherwise

    Rules:
      - Base cost = 10
      - If weight > 10, add 5
      - Members subtract 3
      - Cost cannot go below 0
    """
    if weight <= 0:
        return "Invalid weight"

    cost = 10.0
    if weight > 10:
        cost += 5.0
    if is_member:
        cost -= 3.0
    if cost < 0:
        cost = 0.0

    return cost


def _demo():
    print("=== Predicate demos ===")
    print("is_even(4):", is_even(4))
    print("is_even(7):", is_even(7))
    print("is_valid_age(-1):", is_valid_age(-1))
    print("is_valid_age(120):", is_valid_age(120))

    print("\n=== Classification demos ===")
    for s in [59, 60, 79, 80, 100]:
        print(f"letter_grade({s}):", letter_grade(s))

    for t in [31, 32, 59, 60, 79, 80]:
        print(f"classify_temperature({t}):", classify_temperature(t))

    print("\n=== Validation demos ===")
    for pw in ["abc", "abcdefgh", "abcd3fgh"]:
        print(f"validate_password({pw!r}):", validate_password(pw))

    print("\n=== Shipping demos ===")
    tests = [(-1, False), (1, False), (11, False), (1, True)]
    for w, m in tests:
        print(f"shipping_cost(weight={w}, is_member={m}):", shipping_cost(w, m))


if __name__ == "__main__":
    _demo()
