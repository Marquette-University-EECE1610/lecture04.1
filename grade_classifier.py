score = float(input("Enter the student's score (0-100): "))

if score > 100:
    grade = "U"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 0:
    grade = "F"
else:
    grade = "U"

print(f"The student's grade is: {grade}")
