#1. Check if all characters in a string are unique.
# sample input : "abcde"
# output : True

def isUnique(s):
    seen = set()
    
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    
    return True

print(isUnique("abcde"))