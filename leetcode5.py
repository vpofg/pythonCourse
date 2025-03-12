nums = [-1,-100,3,99]
k = 2
i = 0
length = len(nums)
nums.reverse()
for i in range(0, abs(k)):
    nums.append(nums[0])
    nums.pop(0)
    i += 1
nums.reverse()
print(nums)


# 3,1,2