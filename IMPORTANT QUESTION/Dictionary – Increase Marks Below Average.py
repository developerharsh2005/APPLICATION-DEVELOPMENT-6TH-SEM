marks = {'Amit': 70, 'Rina': 45, 'Suman': 60, 'Neha': 80}

avg = sum(marks.values()) / len(marks)

for k in marks:
    if marks[k] < avg:
        marks[k] = round(marks[k] * 1.05, 2)

print(marks)
