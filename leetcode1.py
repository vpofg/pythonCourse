nums = [3, 2,2,3]
val = 3
k = len(nums) - nums.count(val)
while len(nums) > k:
    index = nums.index(val)
    nums.remove(val)
    k = len(nums) - nums.count(val)
print(nums)