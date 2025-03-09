nums = [1,2,3,4,5,6,7]
k = 3
i = 0
length = len(nums)
nums_c = []
for i in range(0, abs(length - k)):
    nums_c.append(nums[i])
    i += 1
print(nums_c)
