import os

file = input("Enter the file name: ")

if os.path.isfile(file):
    print("the file exists")
else:
    print("the file does not exist")
    