#5. Group numbers based on even and odd using dictionary.
# sample input : [1,2,3,4,5,6]
# output : {
#  'even': [2,4,6],
#  'odd': [1,3,5]
# }

def groupEvenOdd(nums):
    result = {"even": [], "odd": []}
    
    for n in nums:
        if n % 2 == 0:
            result["even"].append(n)
        else:
            result["odd"].append(n)
    
    return result

print(groupEvenOdd([1,2,3,4,5,6]))