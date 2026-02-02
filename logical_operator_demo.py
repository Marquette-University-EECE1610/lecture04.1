# Truth table for logical operators
print("\nTruth Table for Logical Operators")
print("a\t\tb\t\tnot a\t\tnot b\t\ta and b\t\ta or b\t\ta != b")
boolean_values = [True, False]
for a in boolean_values:
    for b in boolean_values:
        print(f"{a}\t\t{b}\t\t{not a}\t\t{not b}\t\t{a and b}\t\t{a or b}\t\t{a != b}")

# Define some boolean variables
a = True
b = False

# Logical AND (and)
print("\nSome example logical expressions")
print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}, because one operand is false.")

# Logical OR (or)
print(f"a or b:  {a or b}, because at least one operand is true.")

# Logical NOT (not)
print(f"not a:   {not a}, because 'a' is {a}.")
print(f"not b:   {not b}, because 'b' is {b}.")

# Logical XOR (!=)
print(f"a != b:  {a != b}, because operands are different.\n")

# Combining logical operators
result = (a and not b) or (not a and b)
print(f"(a and not b) or (not a and b): {result}")  # True

# Example with numbers
x = 10
y = 5
print(f"\nx = {x}, y = {y}")
print(f"(x > 5) and (y < 10): {(x > 5) and (y < 10)}\n")  # True
