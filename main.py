
import pandas as pd


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


students = pd.read_csv("students.csv")

print("ORIGINAL DATA")
print(students)

print("\nMISSING VALUES")
print(students.isnull().sum())

subjects = ["python", "maths", "database"]

# Convert subject columns to numeric values.
for subject in subjects:
    students[subject] = pd.to_numeric(
        students[subject],
        errors="coerce"
    )

# Identify marks outside the allowed range.
invalid_marks = (
    (students[subjects] < 0) |
    (students[subjects] > 100)
)

print("\nOUT-OF-RANGE MARK COUNTS")
print(invalid_marks.sum())

# Keep only records with complete, valid marks.
valid_rows = (
    students[subjects].notna().all(axis=1)
    & students[subjects].ge(0).all(axis=1)
    & students[subjects].le(100).all(axis=1)
)

valid_students = students[valid_rows].copy()
rejected_students = students[~valid_rows].copy()

print("\nVALID STUDENTS")
print(valid_students)

print("\nRECORDS REQUIRING CORRECTION")
print(rejected_students)

# Calculate averages and grades ONLY for valid students.
valid_students["average"] = valid_students[subjects].mean(axis=1)

valid_students["grade"] = valid_students["average"].apply(
    calculate_grade
)

# Rank valid students from highest to lowest average.
sorted_students = valid_students.sort_values(
    by="average",
    ascending=False
).copy()

sorted_students.insert(
    0,
    "rank",
    range(1, len(sorted_students) + 1)
)

print("\nSTUDENT RANKINGS")
print(sorted_students[["rank", "name", "average", "grade"]])
