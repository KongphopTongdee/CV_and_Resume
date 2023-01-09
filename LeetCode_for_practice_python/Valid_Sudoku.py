def isValidSudoku(board):
    Ans = True
    listcheck = []
    liststore = [[],[],[],[],[],[],[],[],[]]
    
    # 1) Check row
    for i in range(9):
        if board[i].count("1") >= 2:
            Ans = False
        elif board[i].count("2") >= 2:
            Ans = False
        elif board[i].count("3") >= 2:
            Ans = False
        elif board[i].count("4") >= 2:
            Ans = False
        elif board[i].count("5") >= 2:
            Ans = False
        elif board[i].count("6") >= 2:
            Ans = False
        elif board[i].count("7") >= 2:
            Ans = False
        elif board[i].count("8") >= 2:
            Ans = False
        elif board[i].count("9") >= 2:
            Ans = False
            
    
    # 2) Check column
    for i in range(9):
        for j in range(9):
            listcheck.append(board[i][j])
    
    for k in range(len(listcheck)):
        if (k % 9 == 0):
            liststore[0].append(listcheck[k])
        elif (k % 9 == 1):
            liststore[1].append(listcheck[k])
        elif (k % 9 == 2):
            liststore[2].append(listcheck[k])
        elif (k % 9 == 3):
            liststore[3].append(listcheck[k])
        elif (k % 9 == 4):
            liststore[4].append(listcheck[k])
        elif (k % 9 == 5):
            liststore[5].append(listcheck[k])
        elif (k % 9 == 6):
            liststore[6].append(listcheck[k])
        elif (k % 9 == 7):
            liststore[7].append(listcheck[k])
        elif (k % 9 == 8):
            liststore[8].append(listcheck[k])
        
    for i in range(9):
        if liststore[i].count("1") >= 2:
            Ans = False
        elif liststore[i].count("2") >= 2:
            Ans = False
        elif liststore[i].count("3") >= 2:
            Ans = False
        elif liststore[i].count("4") >= 2:
            Ans = False
        elif liststore[i].count("5") >= 2:
            Ans = False
        elif liststore[i].count("6") >= 2:
            Ans = False
        elif liststore[i].count("7") >= 2:
            Ans = False
        elif liststore[i].count("8") >= 2:
            Ans = False
        elif liststore[i].count("9") >= 2:
            Ans = False    
    
    liststore = [[],[],[],[],[],[],[],[],[]]
    
    # 3) Check box
    
    for i in range(81):
        if (i >= 0 and i <= 2):
            liststore[0].append(listcheck[i])
        elif (i >= 9 and i <= 11):
            liststore[0].append(listcheck[i])
        elif (i >= 18 and i <= 20):
            liststore[0].append(listcheck[i])
            
        elif (i >= 3 and i <= 5):
            liststore[1].append(listcheck[i])
        elif (i >= 12 and i <= 14):
            liststore[1].append(listcheck[i])
        elif (i >= 21 and i <= 23):
            liststore[1].append(listcheck[i])
            
        elif (i >= 6 and i <= 8):
            liststore[2].append(listcheck[i])
        elif (i >= 15 and i <= 17):
            liststore[2].append(listcheck[i])
        elif (i >= 24 and i <= 26):
            liststore[2].append(listcheck[i])
            
        elif (i >= 27 and i <= 29):
            liststore[3].append(listcheck[i])
        elif (i >= 36 and i <= 38):
            liststore[3].append(listcheck[i])
        elif (i >= 45 and i <= 47):
            liststore[3].append(listcheck[i])
            
        elif (i >= 30 and i <= 32):
            liststore[4].append(listcheck[i])
        elif (i >= 39 and i <= 41):
            liststore[4].append(listcheck[i])
        elif (i >= 48 and i <= 50):
            liststore[4].append(listcheck[i])
    
        elif (i >= 33 and i <= 35):
            liststore[5].append(listcheck[i])
        elif (i >= 42 and i <= 44):
            liststore[5].append(listcheck[i])
        elif (i >= 51 and i <= 53):
            liststore[5].append(listcheck[i])
            
        elif (i >= 54 and i <= 56):
            liststore[6].append(listcheck[i])
        elif (i >= 63 and i <= 65):
            liststore[6].append(listcheck[i])
        elif (i >= 72 and i <= 74):
            liststore[6].append(listcheck[i])
            
        elif (i >= 57 and i <= 59):
            liststore[7].append(listcheck[i])
        elif (i >= 66 and i <= 68):
            liststore[7].append(listcheck[i])
        elif (i >= 75 and i <= 77):
            liststore[7].append(listcheck[i])
    
        elif (i >= 60 and i <= 62):
            liststore[8].append(listcheck[i])
        elif (i >= 69 and i <= 71):
            liststore[8].append(listcheck[i])
        elif (i >= 78 and i <= 80):
            liststore[8].append(listcheck[i])
    
    for i in range(9):
        if liststore[i].count("1") >= 2:
            Ans = False
        elif liststore[i].count("2") >= 2:
            Ans = False
        elif liststore[i].count("3") >= 2:
            Ans = False
        elif liststore[i].count("4") >= 2:
            Ans = False
        elif liststore[i].count("5") >= 2:
            Ans = False
        elif liststore[i].count("6") >= 2:
            Ans = False
        elif liststore[i].count("7") >= 2:
            Ans = False
        elif liststore[i].count("8") >= 2:
            Ans = False
        elif liststore[i].count("9") >= 2:
            Ans = False   
    
    listcheck = []
    liststore = []
    
    print(Ans)
    
    return Ans

isValidSudoku([["5","3",".",".","7",".",".",".","."]
               ,["6",".",".","1","9","5",".",".","."]
               ,[".","9","8",".",".",".",".","6","."]
               ,["8",".",".",".","6",".",".",".","3"]
               ,["4",".",".","8",".","3",".",".","1"]
               ,["7",".",".",".","2",".",".",".","6"]
               ,[".","6",".",".",".",".","2","8","."]
               ,[".",".",".","4","1","9",".",".","5"]
               ,[".",".",".",".","8",".",".","7","9"]])

isValidSudoku([["8","3",".",".","7",".",".",".","."]
               ,["6",".",".","1","9","5",".",".","."]
               ,[".","9","8",".",".",".",".","6","."]
               ,["8",".",".",".","6",".",".",".","3"]
               ,["4",".",".","8",".","3",".",".","1"]
               ,["7",".",".",".","2",".",".",".","6"]
               ,[".","6",".",".",".",".","2","8","."]
               ,[".",".",".","4","1","9",".",".","5"]
               ,[".",".",".",".","8",".",".","7","9"]])



