#!/usr/bin/python3

my_file = input("Enter the file name to open: ")
try:
    file = open(my_file, "r") # open function is used to open the file and  r is read only option 
except FileNotFoundError as e:
    print(e)
    exit(1)
for line in file:
    print(line)