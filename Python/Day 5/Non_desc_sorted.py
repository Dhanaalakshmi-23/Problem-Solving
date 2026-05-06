#1. Check if an array is sorted in non-decreasing order.
# sample input : [1, 2, 2, 3, 4]
# output : True

def isSorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

print(isSorted([1, 2, 2, 3, 4]))