#1. Group words that are anagrams.
# lis = ["eat", "tea", "tan", "ate", "nat", "bat"]
# output : {
#  'aet': ['eat', 'tea', 'ate'],
#  'ant': ['tan', 'nat'],
#  'abt': ['bat']
# }

lis = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = {}

for w in lis:
    key = "".join(sorted(w))
    result.setdefault(key, []).append(w)

print(result)