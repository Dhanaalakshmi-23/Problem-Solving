#4. Find the most frequent element in an array.
# sample input : [1,3,2,1,4,1]
# output : 1

def mostFrequent(nums):
    freq = {}
    max_count = 0
    result = None
    
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
        
        if freq[n] > max_count:
            max_count = freq[n]
            result = n
    
    return result

print(mostFrequent([1,3,2,1,4,1]))