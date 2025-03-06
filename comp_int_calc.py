# Python compound interest calculator
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle Can't be Less than or Equal to Zero")
    else:
        break
    
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate Can't be Less than or Equal to Zero")
    else:
        break
        
while True:
    time = float(input("Enter the Time in years: "))
    if time < 0:
        print("Time Can't be Less than or Equal to Zero")
    else:
        break
        
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")