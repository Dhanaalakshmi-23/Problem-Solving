#1. Find intersection of two arrays (unique elements) using dictionary.
# sample input : nums1 = [1,2,2,1], nums2 = [2,2]
# output : [2]

def intersection(nums1, nums2):
    freq = {}
    result = []
    
    for n in nums1:
        freq[n] = 1
    
    for n in nums2:
        if n in freq:
            result.append(n)
            del freq[n]
    
    return result

print(intersection([1,2,2,1], [2,2]))