def is_valid_age(age):
    """Return True if 0 <= age <= 120, else False."""
    # TODO: implement
    pass


def run_age_driver():
    age = int(input("Enter age: "))
    if is_valid_age(age):
        print("Valid")
    else:
        print("Invalid")


def classify_temperature(temperature):
    """
    Return:
      - "Freezing" if temperature < 32
      - "Cold" if 32 <= temperature <= 59
      - "Comfortable" if 60 <= temperature <= 79
      - "Hot" if temperature >= 80
    """
    pass


def run_temp_driver():
    temp = float(input("Enter temperature (F): "))
    print(classify_temperature(temp))


def validate_password(password):
    """
    Return:
      - "Too short" if len(password) < 8
      - "No digit" if password contains no digits
      - "Valid" otherwise

    Constraint for now: no loops required.
    Hint: use membership checks like ("0" in password).
    """
    # TODO: implement using guard clauses (early returns)


def shipping_cost(weight, is_member):
    """
    Rules:
      - If weight <= 0: return "Invalid weight"
      - Base cost = 10
      - If weight > 10: add 5
      - If is_member: subtract 3
      - Cost cannot go below 0
    """
    # TODO: implement
    pass


def quick_tests():
    assert is_valid_age(-1) is False, "is_valid_age(-1) should be False"
    assert is_valid_age(0) is True, "is_valid_age(0) should be True"
    assert is_valid_age(120) is True, "is_valid_age(120) should be True"
    assert is_valid_age(121) is False, "is_valid_age(121) should be False"

    assert classify_temperature(31) == "Freezing", "classify_temperature(31) should be 'Freezing'"
    assert classify_temperature(32) == "Cold", "classify_temperature(32) should be 'Cold'"
    assert classify_temperature(80) == "Hot", "classify_temperature(80) should be 'Hot'"

    assert validate_password("abc") == "Too short", "validate_password('abc') should be 'Too short'"
    assert validate_password("abcdefgh") == "No digit", "validate_password('abcdefgh') should be 'No digit'"
    assert validate_password("abcd3fgh") == "Valid", "validate_password('abcd3fgh') should be 'Valid'"

    assert shipping_cost(-1, False) == "Invalid weight", "shipping_cost(-1, False) should be 'Invalid weight'"
    assert shipping_cost(1, False) == 10, "shipping_cost(1, False) should be 10"
    assert shipping_cost(11, False) == 15, "shipping_cost(11, False) should be 15"
    assert shipping_cost(1, True) == 7, "shipping_cost(1, True) should be 7"


if __name__ == "__main__":
    # Uncomment one at a time during class:
    # run_age_driver()
    # run_temp_driver()
    quick_tests()
