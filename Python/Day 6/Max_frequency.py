#2. Find the character with maximum frequency in a string.
# sample input : "dhanaa"
# output : 'a'

def maxFrequencyChar(s):
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    max_char = ""
    max_count = 0
    
    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            max_char = key
    
    return max_char

print(maxFrequencyChar("dhanaa"))