def paranthesis_match(string):
    string = list(string)
    resarr = []
    for i in range(0,len(string)):
        if(string[i]=="{" or string[i]=="(" or string[i]=="["):
            resarr.append(string[i])
        if(string[i]=="}"):
            if resarr[len(resarr)-1]=="(" or resarr[len(resarr)-1]="[":
                resarr.pop()
            else:
                resarr.append(string[i])
        if(string[i]==")"):
            if resarr[len(resarr)-1]=="[" or resarr[len(resarr)-1]="{":
                resarr.pop()
            else:
                resarr.append(string[i])
        if(string[i]=="]"):
            if resarr[len(resarr)-1]=="(" or resarr[len(resarr)-1]="{":
                resarr.pop()
            else:
                resarr.append(string[i])
    return "".join(resarr)

string = input()
paranthesis_match(string)