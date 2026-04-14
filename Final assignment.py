#LList
my_list = ["apple", "grapes", "mango"]
my_list.append("orange")
my_list.remove("mango")
my_list.sort()

print("List:", my_list)


#Tuple
my_tuple = (1, 2, 3)

# Try to modify one element
my_tuple[0] = 10
Tuples are designed to be unchangeable immutable.

#Set
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(3)

print("Set:", my_set)


#Dictionary
student = {
    "name": "Jeshley",
    "age": 17
}
# Add a new key "grade"
student["grade"] = "12"
# Update your "age"
student["age"] = 18
# Print all keys
print(student.keys())
