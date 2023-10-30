import os
import json
import sys

dict = {}

# Entering the student details
n = int(input("Enter the number of students : "))
for i in range(n):
    keys = input(f"\nEnter the name of the {i+1} student : ")
    values = input("Enter the his/her marks : ")
    dict[keys] = values

#  Storing the data into the json file 
file_name  = input("\nEnter the json file name  : ")
if os.path.isfile(file_name):
    choice = input("file already exists. Do you want to replace it ? [y/n]")
    if choice.lower() == 'y':
        store_json = input("Do you want to store the details into json file  [y/n] : ")
        if store_json.lower() == 'y':
            with open(file_name,"w") as Insert_details:
                json.dump(dict,Insert_details)
            if os.path.getsize(file_name) != 0:
                print("Successfully created json file and data has been stored ")
            else:
                print("Error in file creation")
    else:
        sys.exit(0)

else:
    store_json = input("Do you want to store the details into json file  [y/n] : ")
    if store_json.lower() == 'y':
            with open(file_name,"w") as Insert_details:
                json.dump(dict,Insert_details)
            if os.path.getsize(file_name) != 0:
                print("Successfully created json file and data has been stored ")
            else:
                print("Error in file creation")
print()
#  Reading the data from the json file
read_json = input("Do you want to read the json file [y/n] :  ")
if read_json.lower() == 'y':
    with open(file_name,'r') as read:
        if os.path.getsize(file_name) == 0:
            print("There is nothing in the json file ")
        else:
            print(json.load(read))

print()
# Searching the student grade
search  = input("Do you want to search the student data ? [y/n] ")
if search.lower() == 'y':
    if os.path.isfile(file_name):
        if os.path.getsize(file_name) == 0:
            print("file is empty")
        else:
            student_name = input("Enter the student name to be search  : ")
            with open(file_name,"r") as file:
                data = json.load(file)
                print(f"Grades of the {student_name} is : ",data[student_name])

print()
if os.path.isfile(file_name):
    find = input("Do you want to find name of the student who got highest grade ? [y/n] ")
    if find.lower() == 'y':
        with open(file_name,"r") as file:
            data = json.load(file)
            max , name = 0,""
            for line,values in data.items():
                if max <  int(values) :
                    max = int(values)
                    name = line
            print(f"{name} got highest marks ")