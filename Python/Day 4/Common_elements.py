#3. Find common elements between two lists (including duplicates).
# sample input : nums1 = [1,2,2,1], nums2 = [2,2]
# output : [2,2]

def intersect(nums1, nums2):
    freq = {}
    result = []
    
    for n in nums1:
        freq[n] = freq.get(n, 0) + 1
    
    for n in nums2:
        if n in freq and freq[n] > 0:
            result.append(n)
            freq[n] -= 1
    
    return result

print(intersect([1,2,2,1], [2,2]))