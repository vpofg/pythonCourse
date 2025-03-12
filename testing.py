citations = [100]
n = len(citations)
citations.sort()
for i,v in enumerate(citations):
    if n - i <= v:
        print(n - i)
print("0")

# i is the iteration while v is the current value. Thanks to that 
# we can iterate trough the whole array and using the if statement
# compare length - iteration (so the maximum values as the array is sorted) with
# v so each value. If the 
    
