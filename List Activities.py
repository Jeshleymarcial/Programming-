# Activity 1: Create a List
fruits = ["apple", "banana", "mango"]

#Activity 2: Access Items
fruits = ["apple", "banana", "cherry"]
print(fruits [0])
print(fruits [2])

# Activity 3: List Length
colors = ["red", "blue", "green", "yellow"]
print(len(colors))

#Activity 4: Change Item
fruits = ["apple", "banana", "cherry"]
fruits[1]="orange"
print(fruits)

#Activity 5: Add Items
fruits = ["apple", "banana"]
fruits.append("mango")
fruits.insert(1, "grapes")
print(fruits)

#Activity 6: Remove Items
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
fruits.pop()
print(fruits)

# Activity 7: For Loop
animals = ["dog", "cat", "bird"]
for x in animals:
 print(x)

 # Activity 8: With Index
numbers = [10, 20, 30]
for x, y in enumerate(numbers):
    print(x, ":", y)

# Activity 9: Check if Item Exists
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
   print("yes, banana exist")

# Activity 10: Sorting
numbers = [5, 2, 9, 1]
# Ascending
numbers.sort()
print(numbers)
# Descending
numbers.sort(reverse = True)
print(numbers)
# Activity 11: Copy List
list1 = ["a", "b", "c"]
list2 = list1.copy()
print(list2)