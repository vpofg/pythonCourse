numpad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*", 9, "#"))

for row in numpad:
    for num in row:
        print(num, end=" ")
    print()