#4. Find if there exists a pair with given sum in a sorted array.
# sample input : nums = [1,2,3,4,6], target = 6
# output : True

def hasPairWithSum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current = nums[left] + nums[right]
        
        if current == target:
            return True
        elif current < target:
            left += 1
        else:
            right -= 1
    
    return False

print(hasPairWithSum([1,2,3,4,6], 6))