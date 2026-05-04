#2. Find the first repeating element in a list.
# sample input : [1, 2, 3, 2, 4, 5]
# output : 2

def firstRepeating(nums):
    seen = set()
    
    for n in nums:
        if n in seen:
            return n
        seen.add(n)
    
    return None

print(firstRepeating([1, 2, 3, 2, 4, 5]))