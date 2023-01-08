def mySqrt(x):
    ####################### First Solution #####################################
    # Ans = 0
    
    # for i in range(46341):          # 46341 come from square root of 2**31 -1 
    #     if (i**2 <= x and (i+1)**2 > x):
    #         Ans = i
    #         return Ans
        
    ####################### Second Solution #####################################
    root = x
    if x == 0 :
        return 0
    else:
        while 0.5*(root+(x/root)) != root:
            root = 0.5*(root+(x/root))
        return int(root//1)         # // = divide and display only integer




# mySqrt(4)
# mySqrt(8)

print(mySqrt(0))
print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(638585692))


# You must not use any built-in exponent function or operator.
    # For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.