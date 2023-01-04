def fizzBuzz(a):
    Ans = []
    
    for i in range(1,a+1):
        if(i % 3 == 0 and i % 5 == 0):
            Ans.append("FizzBuzz")
        elif(i % 3 == 0):
            Ans.append("Fizz")
        elif(i % 5 == 0):
            Ans.append("Buzz")
        else:
            Ans.append(str(i))
    
    print(Ans)
    return Ans
            
fizzBuzz(3)
# fizzBuzz(5)
# fizzBuzz(15)