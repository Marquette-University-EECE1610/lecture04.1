"""
ai_pairs_exercises.py

Starter skeletons for in-class paired exercises.
Each exercise has an AI-OFF part (students implement) and an AI-ON part (students verify/refactor).

Instructor tip:
- Have students run boundary tests immediately after writing each function.
- During AI-ON, require students to identify at least one edge case and one simplification.
"""

# ========= Pair 1: is_valid_age =========

def is_valid_age(age: int) -> bool:
    """Return True if 0 <= age <= 120, else False."""
    # TODO: implement
    pass


def run_age_driver():
    age = int(input("Enter age: "))
    if is_valid_age(age):
        print("Valid")
    else:
        print("Invalid")


# ========= Pair 2: classify_temperature =========

def classify_temperature(temp_f: float) -> str:
    """
    Return:
      - "Freezing" if temp_f < 32
      - "Cold" if 32 <= temp_f <= 59
      - "Comfortable" if 60 <= temp_f <= 79
      - "Hot" if temp_f >= 80
    """
    # TODO: implement
    pass


def run_temp_driver():
    temp = float(input("Enter temperature (F): "))
    print(classify_temperature(temp))


# ========= Pair 3: validate_password (no loops required) =========

def validate_password(pw: str) -> str:
    """
    Return:
      - "Too short" if len(pw) < 8
      - "No digit" if pw contains no digits
      - "Valid" otherwise

    Constraint for now: no loops required.
    Hint: use membership checks like ("0" in pw).
    """
    # TODO: implement using guard clauses (early returns)
    pass


# ========= Pair 4: shipping_cost =========

def shipping_cost(weight: float, is_member: bool):
    """
    Rules:
      - If weight <= 0: return "Invalid weight"
      - Base cost = 10
      - If weight > 10: add 5
      - If is_member: subtract 3
      - Cost cannot go below 0
    """
    # TODO: implement using guard clauses
    pass


def quick_tests():
    """Quick boundary tests (students can extend)."""
    print("age:", is_valid_age(-1), is_valid_age(0), is_valid_age(120), is_valid_age(121))
    print("temp:", classify_temperature(31), classify_temperature(32), classify_temperature(80))
    print("pw:", validate_password("abc"), validate_password("abcdefgh"), validate_password("abcd3fgh"))
    print("ship:", shipping_cost(-1, False), shipping_cost(1, False), shipping_cost(11, False), shipping_cost(1, True))


if __name__ == "__main__":
    # Uncomment one at a time during class:
    # run_age_driver()
    # run_temp_driver()
    quick_tests()
