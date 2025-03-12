nums = [0, 1]
if len(nums) > 2:
    nums.reverse()
next = nums[0]
if len(nums) == 0:
    print(True) 
elif next == 0: 
    print(False)
else:
    for i in range(1, len(nums)-1):
        if nums[i] >= i:
            next = nums[i+1]
    if nums[len(nums) - 1] >= next:
        print(True)
    else:
        print(False)
        
    #not done yet