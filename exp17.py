import random

nums = []

for i in range(8):
    nums.append(random.randint(1, 100))

big = nums[0]
small = nums[0]

for n in nums:
    if n > big:
        big = n
    if n < small:
        small = n

print(nums)
print(big)
print(small)
