def chech_divisibility(a,b):
    if a%b==0:
        return True
    else:
        return False
a,b = map(int,input().split())
if(chech_divisibility(a,b)):
    print("Divisible")
else:
    print("Not Divisible")