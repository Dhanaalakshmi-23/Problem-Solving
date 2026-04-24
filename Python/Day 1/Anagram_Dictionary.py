lis = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = {}

for w in lis:
    key = "".join(sorted(w))
    result.setdefault(key, []).append(w)

print(result)