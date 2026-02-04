students = [
    {"name": "Alice", "grades": [85, 92, 88]},
    {"name": "Bob", "grades": [78, 81, 85]},
    {"name": "Charlie", "grades": [95, 100, 91]}
]
print("Student Averages:")
for student in students:
    total = sum(student["grades"])
    count = len(student["grades"])
    average = total / count
    print(f"{student['name']}: {average:.2f}")