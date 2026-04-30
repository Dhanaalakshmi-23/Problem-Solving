#3. Check if two strings are anagrams using dictionary.
# sample input : s = "dhanaa", t = "ahdnac"
# output : False

def isanagram(s, t):
    if len(s) != len(t):
        return False
    
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    
    return True

print(isanagram("dhanaa", "ahdnac"))