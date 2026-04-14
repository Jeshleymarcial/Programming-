#Part 1
#Tuple of 5 favorite fruits
fruits = ("apple", "banana", "mango", "grapes", "orange")
#List of 5 daily tasks
tasks = ["wake up", "eat breakfast", "exercise", "play", "sleep"]
#Set of unique numbers
numbers = set([1, 2, 2, 3, 4, 4, 5])
#Dictionary
student = {
    "name": "Jeshley",
    "age": 18,
    "course": "BSIT"
}

#List 
#Add a new task
tasks.append("play badminton")
#Remove one task
tasks.remove("exercise")
#Sort the list
tasks.sort()
print(tasks)

#Tuple 
#Try to change one value
fruits[0] = "apple"
Tuples are immutable cannot be changed after creation.

#Set
#Add a number
numbers.add(6)
#Remove a number
numbers.remove(2)
print(numbers)
#Show how duplicates are removed
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
print(unique_nums)

#Dictionary
#Add new key
student["grade"] = "12"
#Update age
student["age"] = 18
#Print all keys and values
print(student.keys())
print(student.values())
