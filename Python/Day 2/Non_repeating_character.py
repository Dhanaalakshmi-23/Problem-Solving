#1. Find the first non-repeating character in a string using dictionary.
# sample input : "dhanaa"
# output : 'd'

def firstUniqueChar(s):
    freq = {}
    
    # count frequency
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    # find first unique
    for ch in s:
        if freq[ch] == 1:
            return ch
    
    return None

print(firstUniqueChar("dhanaa"))