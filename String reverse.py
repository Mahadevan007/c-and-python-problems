def rev_string(string):
    string = list(string)
    i = 0
    j = len(string) - 1
    while(i<j):
        temp = string[i]
        string[i] = string[j]
        string[j] = temp
        i = i + 1
        j = j - 1
    return "".join(string)

string = input()
print(rev_string(string))