N = int(input().strip())
students = []
for _ in range(N):
    name = input().strip()
    grade = float(input().strip())
    students.append([name, grade])

students.sort(key=lambda x: x[1])
second_lowest_grade = None
for i in range(1, N):
    if students[i][1] != students[0][1]:
        second_lowest_grade = students[i][1]
        break
students_with_second_lowest_grade = [student[0] for student in students if student[1] == second_lowest_grade]
for name in sorted(students_with_second_lowest_grade):
    print(name)
