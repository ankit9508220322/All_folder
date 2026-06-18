# f = open("ankit.txt","r")
# data = f.read()
# print(data)
# f.close()

f = open("ankit.txt","r")
for line in f:
    print(line)
f.close()
# no need to write f.close because file is alrready closed with method
with open("ankit.txt","r") as f:
    data = f.read()
    print(data)
    