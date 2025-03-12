nums = [-1,1,0,-3,3]
answer = []
copy = []
copy.extend(nums)
for i in range(0, len(nums)):
    product_full = 1
    stack = nums[i]
    nums.pop(i)
    for j in range(0, len(nums)):
        product_full *= nums[j]
    answer.append(int(product_full))
    nums.insert(i, stack)
    nums = copy
    
print(answer) 
