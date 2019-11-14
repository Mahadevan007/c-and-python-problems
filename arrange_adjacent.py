def arrange_adjacent(arr):
    mid  = len(arr)/2
    firstarr = []
    secondarr = []
    resultarr = []
    for i in range(0,mid):
        firstarr.append(arr[i])
    for i in range(mid,len(arr)):
        secondarr.append(arr[i])
    for i range(0,mid+1):
        resultarr.append(firstarr[i])
        resultarr.append(secondarr[i])
    return resultarr

arr = list(map(int,input().split()))
print(arrange_adjacent(arr))