n = int(input().strip())
student_marks = {}
for _ in range(n):
    name, *marks = input().split()
    marks = list(map(float, marks))
    student_marks[name] = marks
query_name = input().strip()
marks = student_marks[query_name]
average = sum(marks) / len(marks)
print("{:.2f}".format(average))
