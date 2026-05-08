#5. Find the longest word in a list. If multiple words have same length, return the first one.
# sample input : ["apple", "banana", "cat", "elephant"]
# output : "elephant"

def longestWord(words):
    longest = words[0]
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

print(longestWord(["apple", "banana", "cat", "elephant"]))