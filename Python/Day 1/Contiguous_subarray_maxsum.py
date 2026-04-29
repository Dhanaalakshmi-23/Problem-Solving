#2. Find the maximum sum of a contiguous subarray.
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# output : 6

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = nums[0]
maximum_sum = nums[0]

for i in range(len(nums)):
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)