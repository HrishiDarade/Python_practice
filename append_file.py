myFile = "movies.txt"

try:
    file = open(myFile, "a") #a is the append mode which appends the content in the file and move cursor to the end
except FileNotFoundError as e:
    print("The file was not found")
    print(e)
    exit(1)

movies = ["The Matrix", "The Lord of the Rings", "The Avengers"]

for m in movies:
    file.write(m + "\n")
file.close()