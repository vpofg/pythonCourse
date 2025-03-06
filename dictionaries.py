capitals = {"USA": "Washington DC", 
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA")) # return value for provided key

if capitals.get("Japan"):
    print("That capital exists!")
else:
    print("That capital doesn't exists")
    
    
# capitals.update({"Germany": "Berlin"}) # adds a new key-value pair
# print(capitals) 
# capitals.update({"USA": "Detroit"}) # updates value of an existing key-value pair
# print(capitals)
# capitals.pop("China") # Delete from disctionary
# capitals.popitem() # Delete the last key value pair
# capitals.clear() # clear the whole dict

keys = capitals.keys() # displays only keys
for key in keys:
    print(key)
    
values = capitals.values() # displays only values 
for value in values:
    print(value)
    
items = capitals.items() # displays the pairs
for item in items:
    print(item)
    
for key, value in items:
    print(f"{key} : {value}")
