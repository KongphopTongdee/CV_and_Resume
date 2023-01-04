def longestCommonPrefix(strs):
    Ans = ""
    store_list = []
    spare_list = []
    k = 0
    
    def myFunc(e):
        return len(e)
    strs.sort(reverse=True, key=myFunc)

    # print(strs)

    for i in range(3):
        for j in strs[i]:
            spare_list.append(j)
        store_list.append(spare_list)
        spare_list = []

    if (len(store_list[0]) >= len(store_list[1]) and len(store_list[0]) >= len(store_list[2])):
        check_num = len(store_list[0]) 
    elif (len(store_list[1]) >= len(store_list[0]) and len(store_list[1]) >= len(store_list[2])):
        check_num = len(store_list[1])
    elif(len(store_list[2]) >= len(store_list[0]) and len(store_list[2]) >= len(store_list[1])):
        check_num = len(store_list[2])

    for k in store_list[0]:
        if (k in store_list[1] and k in store_list[2]):
            Ans += str(k)

    
    # print(check_num)
    # print(store_list)
    print(Ans)

    return Ans
    
longestCommonPrefix(["flower","flow","flight"])
longestCommonPrefix(["dog","racecar","car"])