#6. Count frequency of each character in a string.
# sample input : "character"
# output : {'c': 2, 'h': 1, 'a': 2, 'r': 2, 't': 1, 'e': 1}

def charFrequency(s):
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    return freq

print(charFrequency("character"))