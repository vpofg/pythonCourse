def function_name(string):
    print(f"Hello {string}!")
    
function_name("Janek")

def substract(x, y):
    sub = x - y
    print(f"{x} - {y} = {sub}") 
substract(1)

# Sending Arguments with key=value syntax
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# *Args and **Kwargs
# many arguments passed
def fun(*args):
    return sum(args)
print(fun(1, 2, 3, 4)) # 10
print(fun(5, 10, 15))  # 30

# keyword arguments passed
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)
fun(a=1, b=2, c=3)
# OUTPUT
# a 1
# b 2
# c 3
