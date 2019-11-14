def print_pascal(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(values(i,j)," ",end="")
        print()

def values(i,j):
    res = 1
    if(j > i-j):
        j = i - j
    for k in range(0,j):
        res = res * (i-k)
        res = res // (k+1)
    return res

n = int(input())
print_pascal(n)
        