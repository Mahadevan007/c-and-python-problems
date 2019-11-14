newlist = list(map(int,input().split()))
for i in range(0,len(newlist)):
    for j in range(0,len(newlist)-i):
        if(newlist[i]>newlist[j]):
            temp = newlist[i]
            newlist[i] = newlist[j]
            newlist[j] = temp
print(newlist)