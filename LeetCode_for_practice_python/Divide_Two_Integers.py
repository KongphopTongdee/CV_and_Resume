import numpy as np
def divide(dividend,divisor):
    ############################### First Solution ###################################
    Ans = 0
    StoreAns = []
    valuebelow0 = 0
    
    if (divisor == 1 and dividend > 0):
        print(dividend)
        return dividend
    elif (divisor == -1 and dividend < 0):
        dividend = str(dividend)
        dividend = dividend[1:]
        dividend = np.uint32(dividend)
        print(dividend)
        return dividend
    
    if (dividend < 0):
        # create the value more than zero
        dividend = str(dividend)
        dividend = dividend[1:]
        dividend = int(dividend)
        valuebelow0 = 1
    if (divisor < 0):
        # create the value more than zero
        divisor = str(divisor)
        divisor = divisor[1:]
        divisor = int(divisor)
        if (valuebelow0 == 1):
            valuebelow0 = 2
        elif (valuebelow0 == 0):
            valuebelow0 = 1
    
    for i in range(divisor):
        StoreAns.append(0)
    
    numcountarray = len(StoreAns)
    
    for i in range(dividend):
        if (numcountarray > 0):
            StoreAns[numcountarray-1] += 1
            numcountarray -= 1
        elif(numcountarray == 0):
            StoreAns[numcountarray-1] += 1
            numcountarray = len(StoreAns)-1
            
    Ans = StoreAns[0]
    
    if (valuebelow0 == 1):
        # insert the - in the first index
        Ans = str("-")+str(Ans)
        Ans = int(Ans)

    print(Ans)
    
    return Ans

    ####################################### Second Solution #####################################
    # a = abs(dividend)
    # b=abs(divisor)
    
    # negative = (dividend<0 and divisor>=0) or (dividend>=0 and divisor<0)
    
    # output = 0
    
    # while a>=b:
    #     counter = 1
    #     decrement = b
        
    #     while a>=decrement:
    #         a-=decrement
            
    #         output+=counter
    #         counter+=counter
    #         decrement+=decrement
            
    # output = output if not negative else -output
    
    # return min(max(-2147483648, output), 2147483647)
        
divide(10,3)
divide(7,-3)
divide(-2147483648,-1)

# Given two integers dividend and divisor, divide two integers 
# without using multiplication, division, and mod operator. Mean that we can use +,-

# easy way to change from negative value to positive value is times -1 to negative value
# example test : -7 change to positive value by times -1 = 7
