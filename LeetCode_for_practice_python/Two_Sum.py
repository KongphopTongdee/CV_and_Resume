def twoSum(nums,target):
    Ans = []
    dict_ans = {}
    dict_sort = []
    
    for i in range(len(nums)):
        dict_ans[i] = nums[i]
    
    dict_sort = sorted(dict_ans.items(), key=lambda x:x[1])
                              
    for j in range(len(dict_sort)):
        for k in range(j+1,len(dict_sort)):
            if (target == (dict_sort[j][1] + dict_sort[k][1])):
                Ans.append(dict_sort[j][0])   
                Ans.append(dict_sort[k][0])  
    
    print(Ans)
    return Ans

twoSum([2,7,11,15],9)
twoSum([3,2,4],6)
twoSum([3,3],6)