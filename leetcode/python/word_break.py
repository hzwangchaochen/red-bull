def word_break(s,dict):
    if s=="" and len(dict)==0:
        return True
    res=[False for i in range(0,len(s)+1)]
    res[0]=True

    for i in range(0,len(s)):
        for j in range(0,i+1):
            if res[j] and s[j:i+1] in dict:
                res[i+1]=True
    return res[len(s)]

