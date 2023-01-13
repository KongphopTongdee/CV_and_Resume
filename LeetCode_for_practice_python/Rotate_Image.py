def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """    
    ################################## First Solution ###############################################
    Ans = []
    
    for i in range(len(matrix)):
        Ans.append([])
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            Ans[i].append(matrix[j][i])
            
    for i in range(len(Ans)):
        Ans[i] = Ans[i][::-1]
            
    print(Ans)
    
    return Ans
    ################################## Second Solution ###############################################
def rotate(matrix):
    matrix[:] = zip(*matrix[::-1])
    return matrix

rotate([[1,2,3],[4,5,6],[7,8,9]])
# rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])