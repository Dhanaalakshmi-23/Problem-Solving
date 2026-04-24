nums = [10, 20, 4, 45, 99]

first = second = nums[0]

for n in nums:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

print(second)