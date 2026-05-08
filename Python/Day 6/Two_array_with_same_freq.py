#4. Check if two arrays contain the same frequency of elements.
# sample input : arr1 = [1,2,2,3], arr2 = [2,1,3,2]
# output : True

def sameFrequency(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    freq1 = {}
    freq2 = {}
    
    for n in arr1:
        freq1[n] = freq1.get(n, 0) + 1
    
    for n in arr2:
        freq2[n] = freq2.get(n, 0) + 1
    
    return freq1 == freq2

print(sameFrequency([1,2,2,3], [2,1,3,2]))