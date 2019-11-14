a = 0
b = 0
c = 1
resarr = []
resarr.append(a)
resarr.append(b)
resarr.append(c)
limit = int(input("Enter the limit"))
n = 3
if(limit==3):
    print(resarr)
else:
    while(n<=limit):
        d = a + b + c
        a = b
        b = c
        c = d
        resarr.append(d)
        n = n + 1
print(*resarr)