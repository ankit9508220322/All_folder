try:
    file = open("myfile.txt","r")
    data = file.read()
    print(data)
    file.close()
except FileExistsError:
    print("File not found.")

try:
    file = open("my_file.txt", "r")
    for line in file: # Efficient for large files
        print(line.strip()) # Remove newline characters
    file.close()
except FileNotFoundError:
    print("File not found.")
#  ///////////////////////////////////////////////

file = open("my_file.txt", "a")  # Open in append mode
file.write("This is appended text.\n")
file.close()

# ////////////////////////////////////////////////

try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

with open("output.txt", "w") as file:
    file.write("Data written using 'with'.\n")
    
# ////////////////////////////////////////////////

try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

with open("output.txt", "w") as file:
    file.write("Data written using 'with'.\n")