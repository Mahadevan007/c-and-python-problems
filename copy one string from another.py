string = input()
string = list(string)
newstring = string[0:len(string)]
print("Original String ", end="")
print("".join(string))
print("Copied String ", end="")
print("".join(newstring))