#5. Count occurrences of a target element in a list.
# sample input : nums = [1, 2, 2, 3, 2], target = 2
# output : 3

def countOccurrences(nums, target):
    count = 0
    
    for n in nums:
        if n == target:
            count += 1
            
    return count

print(countOccurrences([1, 2, 2, 3, 2], 2))