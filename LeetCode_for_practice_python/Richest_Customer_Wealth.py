def maximumWealth(accounts):
    Ans = 0
    check1 = 0
    check2 = 0
    
    for i in accounts:
        for j in i :
            check2 += j
        if (check1 < check2):
            check1 = check2
        check2 = 0
    Ans = check1
    
    return Ans

print(maximumWealth([[1,2,3],[3,2,1]]))
print(maximumWealth([[1,5],[7,3],[3,5]]))
print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))
