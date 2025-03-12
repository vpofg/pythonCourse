nums = [2,3,1,2,4,3]
target = 7
n = len(nums)
res = float('inf')
for i in range(n):
    curr = 0
    for j in range(i, n):
        curr += nums[j]
        if curr > target:
            res = min(res, j - i + 1)
            break
if res == float('inf'):
    print("0")

print(res)
