import numpy as np

# Taking input
n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    m = int(input(f"Enter marks for student {i+1}: "))
    marks.append(m)

# Convert to NumPy array
marks_array = np.array(marks)

# Calculations
average = np.mean(marks_array)
highest = np.max(marks_array)
lowest = np.min(marks_array)
passed = np.sum(marks_array >= 40)
failed = np.sum(marks_array < 40)

# Grade system
grades = []

for m in marks_array:
    if m >= 90:
        grades.append("A")
    elif m >= 75:
        grades.append("B")
    elif m >= 50:
        grades.append("C")
    elif m >= 40:
        grades.append("D")
    else:
        grades.append("F")

# Output
print("\n--- Result Analysis ---")
print("Marks:", marks_array)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", passed)
print("Failed:", failed)
print("Grades:", grades)
