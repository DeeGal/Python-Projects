from Classes import Student

student_1 = Student("Lisa", "Economics", 5.3, False)
student_2 = Student("Pam", "Art", 5.9, True)

print(student_1.name)
print(student_1.gpa)
print(student_2.name)
print(student_2.gpa)
print(student_1.is_on_probation)
print(student_2.is_on_probation)

print(student_2.on_honor_roll())
