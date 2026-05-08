#3. Group words based on last character.
# sample input : ["apple", "table", "cat", "bat", "ball"]
# output : {
#  'e': ['apple', 'table'],
#  't': ['cat', 'bat'],
#  'l': ['ball']
# }

def groupByLastChar(words):
    result = {}
    
    for word in words:
        key = word[-1]
        result.setdefault(key, []).append(word)
    
    return result

print(groupByLastChar(["apple", "table", "cat", "bat", "ball"]))