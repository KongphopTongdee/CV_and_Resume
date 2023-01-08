def strStr(haystack,needle):
    Ans = -1
    
    for i in range(0,len(haystack)-len(needle)+1,1):
        if (needle == haystack[i:i+len(needle)]):
            Ans = i
            break
        else:
            Ans = -1
    
    print(Ans)
    
    return Ans

# strStr("sadbutsad","sad")
# strStr("leetcode","leeto")
strStr("aaa","aaaa")
