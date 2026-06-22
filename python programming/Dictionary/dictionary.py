# student = {
#     "name": "anit",
#     "age": 21,
#     "college": "abc college",
# }
# print(student["name"], student["age"])

# # method number 2 dict
# person = dict(
#     name = "ankit",
#     age = 22,
#     collage = "maharishi")
# print(person)
# person["email"] = "ankit@example.com"
# print(person)
# del person["collage"]
# print(person)
# print(person.keys())
# print(person.values())
# print(person.items())
# print(person.get("name"))
# print(person.pop("age"))

# looping method
# person1 = dict(
#     name = "ankit",
#     age = 22,
#     collage = "maharishi")
# for key in person1:
#     print(f"{key}: {person1[key]}")
    
# nested dictionary
student = {
    "final":{
    'name': 'ankit kumar',
    'age': 88,
    'school': 'maharishi',
    },
    'marks': {
        'math': 95,
        'science': 88,
        'english': 92
    }
}
for i in student:
    print(f"{i}: {student[i]}")
    print(student.keys())

for keys,value in student.items():
    print(keys,value)
