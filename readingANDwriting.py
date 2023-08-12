employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()



#employee_file = open("employees.txt", "w")
#employee_file.write("\nKelly Naidoo - Programmer")