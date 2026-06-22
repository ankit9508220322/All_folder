mohan = "helo every one my name is {}  {}  and i from {} and i am pursuing {}$"
a = "ankit"
b = "kumar"
c = "bihar"
d = "bca"
converted = mohan.format(a,b,c,d)
print(converted)

print(f" {a} hii how are you {b} and where are from {c} and i am pursuing {d}")

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

text = "choubey jii"
print(f"{text:>16}")  # Right align
print(f"{text:<6}")  # Left align
print(f"{text:^16}")  # Center align

pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")