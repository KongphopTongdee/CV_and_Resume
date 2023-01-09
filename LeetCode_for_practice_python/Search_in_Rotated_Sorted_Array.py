def search(nums, target):
    ############################# First Solution ########################################
    Ans = 0
    
    if (target in nums):
        Ans = nums.index(target)
    else:
        Ans = -1
        
    print(Ans)
    
    return Ans
    ############################# Second Solution ########################################
    # Ans = 0
    # stringnums = ""
    
    # for i in nums:
    #     stringnums += str(i)
    # target = str(target)
    
    # x = stringnums.find(target)
    # Ans = x
    
    # print(x)
    
    # return Ans
    
    
    

search([4,5,6,7,0,1,2],0)
search([4,5,6,7,0,1,2],3)
search([1],0)
