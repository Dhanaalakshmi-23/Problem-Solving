def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


nums_input = input("Enter numbers (space separated): ")
nums_str = nums_input.split()  

nums = []
for x in nums_str:
    nums.append(int(x))

target = int(input("Enter target: "))


result = twoSum(nums, target)

print("Result:", result)