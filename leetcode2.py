nums = [0,0,0,0,0]
length = len(nums)
i = 0
while i <= length:
    for j in range(0, length-1):
        if j == length-1 or j >= length :
            break
        else:
            if nums[j] == nums[j + 1]:
                nums.remove(nums[j])
                length = len(nums)
    i += 1
print(nums)