student = {
    "name": "John",
    "age": 20,
    "gender": "Male",
    "major": "Computer Science",
    "GPA": 3.8
}

#Print value associated with key 'age'
print("Age:", student["age"])

#Print value associated with key 'GPA'
print("GPA:", student["GPA"])

#Find and print the number of key-value pairs
print("Number of key-value pairs:", len(student))

#Add a new key-value pair
student["year"] = 3

#Update the value of GPA
student["GPA"] = 3.9

#Print updated dictionary
print("Updated student dictionary:", student)
print(student["name"])

print(student.values())

