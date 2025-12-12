def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        return  "Student not found in the system"
grade = {"dagim": 97, "biruk": 90}
print(get_grade(grade, "mark"))