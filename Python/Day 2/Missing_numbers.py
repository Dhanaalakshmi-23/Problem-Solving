#1. Find the missing number in an array containing numbers from 0 to n.
# sample input : [3, 0, 1]
# output : 2

def missingNumber(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    sum_nums = 0
    
    for num in nums:
        sum_nums += num
        
    return total - sum_nums

print(missingNumber([3, 0, 1]))