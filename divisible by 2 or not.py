def power_of_2(n):
    if n%2==0:
        return "divisible by 2"
    else:
        return "not divisible"

n = int(input())
print(power_of_2(n))