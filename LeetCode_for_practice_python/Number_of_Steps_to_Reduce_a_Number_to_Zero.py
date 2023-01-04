def numberOfSteps(num):
    Ans = 0
    stepnum = 0
    
    for i in range(num,0,-1):
        if(num %2 == 0):
            num /= 2
            # print("even")
            # print(num)
        else:
            num -= 1
            # print("odd")
            # print(num)
        stepnum += 1
        if (num == 0):
            break
        
    Ans = stepnum
    return Ans

print(numberOfSteps(14))
print(numberOfSteps(8))
print(numberOfSteps(123))