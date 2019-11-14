def multiply(a,b):
    mul = 0
    for i in range(0,b):
        mul = mul + a
    return mul
a,b = map(int,input().split())
print(multiply(a,b))