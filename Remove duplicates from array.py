newlist = list(map(int,input().split()))
obj = {}
for i in range(0,len(newlist)):
    if newlist[i] not in obj:
        obj[newlist[i]] = 1
    else:
        obj[newlist[i]] = obj[newlist[i]] + 1
result = []
for i in obj:
    if obj[i]==1:
        result.append(i)
print(result)