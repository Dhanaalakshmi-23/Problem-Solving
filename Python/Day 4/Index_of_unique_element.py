#5. Find the index of the first unique element in a list.
# sample input : [4,5,1,2,0,4]
# output : 1   (element 5)

def firstUniqueIndex(nums):
    freq = {}
    
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    
    for i in range(len(nums)):
        if freq[nums[i]] == 1:
            return i
    
    return -1

print(firstUniqueIndex([4,5,1,2,0,4]))