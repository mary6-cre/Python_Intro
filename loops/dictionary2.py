# dict with more values
students= [
    {"name": "Mary", "place": "Nakuru", "age": 21},
    {"name": "John", "place": "Nakuru", "age": 15},
    {"name": "Dennis", "place": "Rongai", "age": 21}
]
# dict allows you to use to use words as indices
for student in students:
    print(student["name"], student["place"], student["age"], sep=", ")