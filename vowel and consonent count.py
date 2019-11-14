vowels = ["a","e","i","o","u"]
consonents = 0
vowelcount = 0
string = input()
string = list(string)
for i in range(0,len(string)):
    if string[i] in vowels:
        vowelcount = vowelcount + 1
    else:
        consonents = consonents + 1
print("Vowels: "+str(vowelcount))
print("Consonents: "+str(consonents))