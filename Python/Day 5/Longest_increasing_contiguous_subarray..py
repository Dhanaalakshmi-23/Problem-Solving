#2. Find the length of the longest increasing contiguous subarray.
# sample input : [1, 3, 5, 4, 7]
# output : 3

def longestIncreasingSubarray(nums):
    count = 1
    max_len = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
            if count > max_len:
                max_len = count
        else:
            count = 1
    
    return max_len

print(longestIncreasingSubarray([1, 3, 5, 4, 7]))