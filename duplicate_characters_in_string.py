string = input()
string = list(string)
string_obj = {}
for i in range(0,len(string)):
    if string[i] not in string_obj:
        string_obj[string[i]] = 1
    else:
        string_obj[string[i]] = string_obj[string[i]] + 1
for i in string_obj:
    if string_obj[i]>1:
        print(i)