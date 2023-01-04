
def kWeakestRows(mat,k):
    Ans = []
    storenum = []
    dict_ans = {}
    store_ans = []
    
    def sortnum(num):
        return num[1]
    
    for i in mat:
        storenum.append(sum(i))
        
    for j in range(len(mat)):
        dict_ans[j] = storenum[j]
        
    sort_dict_ans = sorted(dict_ans.items(), key=lambda x:x[1])
    converted_dict = dict(sort_dict_ans)
    
    for key,value in converted_dict.items():
        store_ans.append(key)
        
    for l in range(k):
        Ans.append(store_ans[l])
        
    return Ans
    
print(kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))
print(kWeakestRows([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]],2))

# input
# mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],k = 3
# mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]],k = 2
