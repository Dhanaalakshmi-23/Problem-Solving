#3. Count how many numbers have even number of digits.
# nums_input = [1, 22, 3456, 666]
# output : 2

def findNumbers(nums):
    count = 0

    for i in range(len(nums)):
        digit = 0
        n = nums[i]

        while n != 0:
            n = n // 10
            digit += 1

        if digit % 2 == 0:
            count += 1

    return count


nums_input = [1, 22, 3456, 666]

result = findNumbers(nums_input)

print(result)