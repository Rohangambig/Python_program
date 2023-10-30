import os
import sys

str = input("Enter the string to be store into the file  : ")
file_name = input("Enter the file name : ")

# write the content into to the file
if os.path.isfile(file_name):
    choice = input("File already exists . Do you want to replace it  ? [y/n] ")
    
    if choice.lower == 'y':
        with open(file_name,"w") as file:
            file.write(str)
    
    if os.path.getsize(file_name) == 0:
        print("Error in file creation")
    else:
        print("Successfully created file")
else:
    with open(file_name,"w") as file:
            file.write(str)
    
    if os.path.getsize(file_name) == 0:
        print("Error in file creation")
    else:
        print("Successfully created file")
        
#  Reading the file
file_name = input("Enter the file name to read it : ")
if os.path.exists(file_name):
    read_file = input("Do you want to read the file ? [y/n]")
    if read_file.lower() == 'y':
        with open(file_name,"r") as file:
            print(file.read())
else:
    with open(file_name,"r") as file:
        print(file.read())
        
# Search the word from the file
file = input("Enter the file name : ")
file_name = open(file,"r")
flag = 0 
word = input("Enter the word from the file : ")
for line in file_name:
    if word in line:
        flag = 1
        break
print(word," found") if flag == 1 else print(word," not foung")