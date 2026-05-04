#4. Replace each element with its frequency in the list.
# sample input : [1,2,2,3,1]
# output : [2,2,2,1,2]

def replaceWithFrequency(nums):
    freq = {}
    
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    
    result = []
    for n in nums:
        result.append(freq[n])
    
    return result

print(replaceWithFrequency([1,2,2,3,1]))