def plusOne(digits):
    Ans = []
    strdigits = ""
    numdigits = 0
    
    for i in digits:
        strdigits += str(i)
    numdigits = int(strdigits)
    numdigits += 1
    strdigits = str(numdigits)
    for j in strdigits:
        Ans.append(int(j))
    
    print(Ans)
    
    
    return Ans


plusOne([1,2,3])
plusOne([4,3,2,1])
plusOne([9])