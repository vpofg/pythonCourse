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

# name = input("Enter your name: ")
# while name == "":
#     print("Name not entered")
#     name = input("Enter your name")
# else:
#     print(f"Hello {name}")
    
# age = int(input("Enter Your Age: "))

# while age < 0:
#     print("Age can't be negative!")
#     age = int(input("Enter Your Age"))
# else:
#     print(f"You are {age} years old")
    
# food = input("Enter your favourite food (q to quit): ")

# while not food == "q":
#     print(f"Your favourite food is: {food}")
#     food = input("Enter your favourite food (q to quit): ")
# else:
#     print("buhbuy")
    
    
# For Loops

for x in range(1,11, 2):
    print(x)
    
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)
    
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
        
        
        
# Collections:
# List -> []  ordered and changeable. Duplicates OK
# Set -> {}   unordered and immutable, but Add/Remove OK, Duplicates NO
# Tuple -> () ordered and unchangeable. Duplicates OK. FASTER
# Dictionary - discussed later

## List
fruits = ["apple", "banana", "orange", "coconut"]
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[2]) # orange
print(fruits[3]) # coconut
print(fruits[::-1]) # prints backwards

for fruit in fruits:
    print(fruit)
    
print(len(fruits))

print("apple" in fruits) # returns bool statement wheater the string is in the list

fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.remove("pineapple")
print(fruits.index("pineapple"))
print(fruits.count("apple"))

for fruit in fruits:
    print(fruit)
    

## Set

# elements are random, good for conmstants
colors = {"red", "green", "blue"}
colors.add("pink")
print(colors)
colors.remove("red")
print(colors)
colors.pop()
print(colors)
colors.clear()
print(colors)
colors.add("banana")
print(colors)
colors.add("banana")
print(colors)

## Tuples

veggies = ("carrot", "celery", "potato")
print("beetroot" in veggies)
print(fruits.count("carrot"))

for veg in veggies:
    print(veg)
    
    
# 2D lists

fruitties =  ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruitties, vegetables, meats]
print(groceries[0]) # this outputs the fruitties list
print(groceries[0][0]) # apple

for collection in groceries:
    print(collection)
    
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
