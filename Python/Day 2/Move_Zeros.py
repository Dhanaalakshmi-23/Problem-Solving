#3. Move all zeros to the end of the array.
# sample input : [0, 1, 0, 3, 12]
# output : [1, 3, 12, 0, 0]

def moveZeroes(nums):
    pos = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1
    
    for i in range(pos, len(nums)):
        nums[i] = 0
        
    return nums

print(moveZeroes([0, 1, 0, 3, 12]))