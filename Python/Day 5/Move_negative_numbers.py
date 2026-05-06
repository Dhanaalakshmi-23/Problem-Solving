#5. Move all negative numbers to the beginning of the array.
# sample input : [1, -2, 3, -4, 5]
# output : [-2, -4, 3, 1, 5]

def moveNegatives(nums):
    left = 0
    
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
    
    return nums

print(moveNegatives([1, -2, 3, -4, 5]))