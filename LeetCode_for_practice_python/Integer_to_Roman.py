def intToRoman(num):
    Ans = ""
    listAns = []
    # test = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    
    while num > 0:
        if(num >= 1000):
            listAns.append("M")
            num -= 1000
        elif(num < 1000 and num >= 900):
            listAns.append("CM")
            num -= 900
        elif(num < 900 and num >= 500):
            listAns.append("D")
            num -= 500
        elif(num < 500 and num >= 400):
            listAns.append("CD")
            num -= 400
        elif(num < 400 and num >= 100):
            listAns.append("C")
            num -= 100
        elif(num < 100 and num >= 90):
            listAns.append("XC")
            num -= 90
        elif(num < 90 and num >= 50):
            listAns.append("L")
            num -= 50
        elif(num < 50 and num >= 40):
            listAns.append("XL")
            num -= 40
        elif(num < 40 and num >= 10):
            listAns.append("X")
            num -= 10
        elif(num < 10 and num >= 9):
            listAns.append("IX")
            num -= 9
        elif(num < 9 and num >= 5):
            listAns.append("V")
            num -= 5
        elif(num < 5 and num >= 4):
            listAns.append("IV")
            num -= 4
        elif(num < 4 and num >= 1):
            listAns.append("I")
            num -= 1

    for i in listAns:
        Ans += str(i)

    print(listAns)
    print(Ans)

    return Ans

# intToRoman(3)
# intToRoman(58)
intToRoman(1994)
# intToRoman(3999)