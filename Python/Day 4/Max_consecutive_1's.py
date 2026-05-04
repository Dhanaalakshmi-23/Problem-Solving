#6. Find the maximum consecutive 1's in a binary array.
# sample input : [1,1,0,1,1,1]
# output : 3

def maxConsecutiveOnes(nums):
    count = 0
    max_count = 0
    
    for n in nums:
        if n == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    
    return max_count

print(maxConsecutiveOnes([1,1,0,1,1,1]))