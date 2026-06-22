'''name = "ankit kumar choubey"
print(name[0])
print(name[-1])
print(name)

name1 = "ankit"
name2 = "kumar"
print(name1 + " " + name2)'''


namea = "ankit kumar chaubey"
print(namea[0:6])
print(namea[-6:])

reverse =" chaubey jii"
print(reverse[::-1])

text = "  i love python programming  "
print(text.strip())
print(text.count("o"))
print(text.title())
print(text.count("p"))

# count the vowel in this string
name = "i am ankit kumar o the"
vowel = ['a','e','i','o','u']
count = 0
# print the vowel then write  the loop char
for i in name:
    if i in vowel:
        count += 1
        print(count)

check = ""
if check == check[::-1]:
    print(f"string is palindrome {check}")
else:
    print(f"not palin drome: {check}")
