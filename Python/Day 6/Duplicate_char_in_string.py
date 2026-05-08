#1. Find all duplicate characters in a string with their count.
# sample input : "programming"
# output : {
#  'r': 2,
#  'g': 2,
#  'm': 2
# }

def duplicateChars(s):
    freq = {}
    result = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    for key in freq:
        if freq[key] > 1:
            result[key] = freq[key]
    
    return result

print(duplicateChars("programming"))