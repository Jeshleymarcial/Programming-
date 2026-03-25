#1
text = input("Name: ")
length = len(text)
print("Length of the string is:", length)

#2
text = input("Name: ")
count = 0

for char in text:
    count += 1

print("Number of characters:", count)

#3
text = input("Name:")
first_char = text[1]

new_string = first_char + text[1:].replace(first_char, '$')

print("Result:", new_string)


#4
str1 = input("First name:")
str2 = input("Last name: ")

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

result = new_str1 + " " + new_str2

print("Result:", result)

#5
a = "aquino"
b = "bautista"
c = "esto"
d = "ferido"
result = a + " " + b + " " + c + " " + d 
print(result)

#6
str1 = input("first name: ")
str2 = input("second name: ")

result = str1 + " " + str2
print("result:", result)

#7
name = input("Name: ")
age = input("Age: ")

paragraph = "My name is " + name + " and I am " + age + " years old."
print(paragraph)
