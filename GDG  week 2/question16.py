grades = {"John": "A", "Sara": "B", "Musa": "A"}
rev = {}
for name, grade in grades.items():
    if grade not in rev:
        rev[grade] = []
    rev[grade].append(name)
print(rev)
