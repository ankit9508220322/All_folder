# Without Walrus
with open("my_file.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

# With Walrus
with open("my_file.txt", "r") as f:
    while (line := f.readline()):
        print(line.strip())