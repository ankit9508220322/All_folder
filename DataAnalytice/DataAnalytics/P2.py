# count tne any character in this word
A = input("enter the chsrcter: ")
term = input("enter the find character: ")
count = 0
for i in A:
    if i == term:
        count += 1
print(count)