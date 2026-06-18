# find the email in user name before the @ part
name = input("enter the email: ")
count = name.index('@')
print(name[0:count])