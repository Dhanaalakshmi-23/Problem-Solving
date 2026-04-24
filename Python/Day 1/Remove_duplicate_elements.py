nums = [1,3,1,3,5,2,7,3]

seen = set()
res = []

for n in nums:
    if n not in seen:
        seen.add(n)
        res.append(n)
print(res)