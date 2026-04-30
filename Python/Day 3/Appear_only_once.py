#2. Find the element that appears only once (others appear twice).
# sample input : [4,1,2,1,2]
# output : 4

def singleNumber(nums):
    freq = {}
    
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    
    for key in freq:
        if freq[key] == 1:
            return key

print(singleNumber([4,1,2,1,2]))