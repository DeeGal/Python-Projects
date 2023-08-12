#Reading Files

#employee_file = open("employees.txt", "r")

#for employees in employee_file.readlines():
    #print(employees)

#employee_file.close()

#writing to files
#employee_file = open("employees.txt", "a")


#employee_file.write("\nToby - Human Resources")

#employee_file.close()

#Append to a file means that u have already written on the text file, u are just modifing the text file. 
#Write to a file means that u have not written any material, u are starting a new page or text file, if u already have text inn the file it gets erased with the new text. 


employee_file = open("employees.txt", "r+")

for employees in employee_file.readlines():

    print(employees)

employee_file.close()


#employee_file = open("employee.txt", 'w')

##employee_file.write("John - Manager")

#employee_file.close()

# modules and pipes






 




