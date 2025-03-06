# Variables
string = "Python"
integer = 1
float = 1.0
boolean = True

# Typecasting
print(type(string))
print(type(integer))
print(type(float))
print(type(boolean))

integer = str(integer)
boolean = str(boolean)

# String Methods

# name = input("Enter your name: ")
# length = len(name)
# print(length)
# name.find("a") # Returns the index of the first occurence of the character
# name.count("a") # Returns the number of occurences of the character 
# name.replace("a", "b") # Replaces all occurences of the character
# name.upper() # Converts the string to uppercase
# name.lower() # Converts the string to lowercase
# name.capitalize() # Capitalizes the first character of the string
# name.title() # Capitalizes the first character of each word in the string
# name.strip() # Removes leading and trailing whitespaces
# name.lstrip() # Removes leading whitespaces
# name.rstrip() # Removes trailing whitespaces
# name.split() # Splits the string into a list of words
# name.join(name) # Joins the elements of the list into a string

# String Indexing
# [start : end : step]
credit_number = "1234-5678-9012-3456"
print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-3])
print(credit_number[::2])

# Format Specifiers

price1 = 221213.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.1f}") # print with 1 floating point
print(f"Price 2 is {price2:10}") # 10 spaces to display the number
print(f"Price 3 is {price3:010}") # 0 padded
print(f"Price 3 is {price3:<10}") # left justify
print(f"Price 3 is {price3:>10}") # right justify
print(f"Price 3 is {price3:^10}") # center
print(f"Price 3 is {price3: }") # space before each outisde of signed
print(f"Price 3 is {price3:,}") # thousand separator as comma
print(f"Price 3 is {price1:+,.2f}") # mixed

# While Loops

name = input("Enter your name: ")
while name == "":
    print("Name not entered")
    name = input("Enter your name")
else:
    print(f"Hello {name}")
    
age = int(input("Enter Your Age: "))

while age < 0:
    print("Age can't be negative!")
    age = int(input("Enter Your Age"))
else:
    print(f"You are {age} years old")
    
food = input("Enter your favourite food (q to quit): ")

while not food == "q":
    print(f"Your favourite food is: {food}")
    food = input("Enter your favourite food (q to quit): ")
else:
    print("buhbuy")