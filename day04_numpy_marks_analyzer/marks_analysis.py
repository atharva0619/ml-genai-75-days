import numpy as np

# Student data
names = np.array(["A", "B", "C", "D", "E"])
marks = np.array([70, 85, 90, 60, 75])

# Basic stats
average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)

# Grade assignment
def assign_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "D"

grades = np.array([assign_grade(m) for m in marks])

# Pass/Fail
result = np.where(marks >= 60, "Pass", "Fail")

# Percentage
total_marks = 100
percentage = (marks / total_marks) * 100

# Topper
topper_index = np.argmax(marks)
topper_name = names[topper_index]
topper_marks = marks[topper_index]

# Display Report
print("\n===== Student Report =====\n")
print("Name | Marks | %     | Grade | Result")
print("--------------------------------------")

for i in range(len(names)):
    print(f"{names[i]}    | {marks[i]}    | {percentage[i]:.2f}% | {grades[i]}     | {result[i]}")

print("\n===== Summary =====")
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

print(f"\nTopper: {topper_name} with {topper_marks} marks")
