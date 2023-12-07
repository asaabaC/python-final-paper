# part i
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")



#part ii
def grade_student(marks):
    if marks >= 90:
        return 'A'
    elif 80 <= marks <= 89:
        return 'B'
    elif 70 <= marks <= 79:
        return 'C'
    elif 60 <= marks <= 69:
        return 'D'
    else:
        return 'F'
student_marks = int(input("Enter the student's marks: "))
result_grade = grade_student(student_marks)
print(f"The student's grade is: {result_grade}")


#part iii
student_marks = 85
result_grade = grade_student(student_marks)
print(f"For a mark of {student_marks}, the student's grade is: {result_grade}")


#part iv
def grade_student(marks):
    if not isinstance(marks, (int, float)):
        return 'Invalid input'
valid_student_marks = 85
result_valid_grade = grade_student(valid_student_marks)
print(f"For a mark of {valid_student_marks}, the student's grade is: {result_valid_grade}")

invalid_student_marks = {}
result_invalid_grade = grade_student(invalid_student_marks)
print(f"For an input of {invalid_student_marks}, the result is: {result_invalid_grade}")


#part v
def grade_student(marks):

    if not isinstance(marks):
        return 'Invalid input', None

    if marks >= 90:
        return 'A', 'Excellent'
    elif 80 <= marks <= 89:
        return 'B', 'Excellent'
    elif 70 <= marks <= 79:
        return 'C', 'Good'
    elif 60 <= marks <= 69:
        return 'D', 'Satisfactory'
    else:
        return 'F', 'Needs improvement'

valid_student_marks = 85
result_grade, result_message = grade_student(valid_student_marks)
print(f"For a mark of {valid_student_marks}, the student's grade is: {result_grade} ({result_message})")

invalid_student_marks = {}
result_grade, result_message = grade_student(invalid_student_marks)
print(f"For an input of {invalid_student_marks}, the result is: {result_grade} ({result_message})")


#part vi

def grade_student(marks):
    if marks >= 90:
        return 'A', 'Excellent'
    elif 80 <= marks <= 89:
        return 'B', 'Excellent'
    elif 70 <= marks <= 79:
        return 'C', 'Good'
    elif 60 <= marks <= 69:
        return 'D', 'Satisfactory'
    else:
        return 'F', 'Needs improvement'

student_marks = 78
result_grade, result_message = grade_student(student_marks)
print(f"For a mark of {student_marks}, the student's grade is: {result_grade} ({result_message})")
