def canConstruct(ransomNote,magazine):
    # Ans = False
    # listinputcheck = []
    # listoutputcheck = []
    # liststore = []
    # stringstore = ""

    # listinputcheck.append(ransomNote)

    # for i in magazine:
    #     liststore.append(i)

    # for j in range(len(magazine)-(len(ransomNote)-1)):
    #     stringstore += str(magazine[j:j+len(ransomNote)])
    #     listoutputcheck.append(stringstore)
    #     stringstore = ""

    # print(listinputcheck)
    # print(listoutputcheck)

    # # For checking ans 
    # for m in range(len(listinputcheck)):
    #     for n in range(len(listoutputcheck)):
    #         if(listinputcheck[m] == listoutputcheck[n]):
    #             Ans = True
    #             break

    #Another Ans
    Ans = False
    listransomNote = []
    listmagazine = []

    for i in ransomNote:
        listransomNote.append(i)

    for j in magazine:
        listmagazine.append(j)

    for i in ransomNote:
        if (i in magazine):
            Ans = True

    # if (listransomNote in listmagazine):
    #     Ans = True
    # else:
    #     Ans = False

    #Test1
    # a = ["ab","ga","ho"]
    # b = ["ba","no","fu"]
    # string = ""

    # for m in range(len(a)):
    #     string += str(a[m])

    # print(string)

    #Test2
    # a = ["abb","acc"]
    # b = ["buu","Fuck","you","though"]

    # for k in range(len(a)):
    #     for l in range(len(b)):
    #         if(a[k] == b[l]):
    #             Ans = True
    #             break

    #Test3
    # a = "abb"
    # b = "baallmksihbwjxojk"
    # listb = []
    # testlist = []
    # teststring = ""

    # for k in b:
    #     listb.append(k)

    # for i in range(len(b)-(len(a)-1)):
    #     teststring += str(b[i:i+len(a)])
    #     testlist.append(teststring)
    #     teststring = ""
        

    # print(len(a))
    # print(len(b))
    # print(listb)
    # print(teststring)
    # print(testlist)

    print(Ans)

    return Ans
canConstruct("a","b")
# canConstruct("aa","ab")
# canConstruct("aa","aab")
# canConstruct("aab","baa")
# canConstruct("aab","baallmksihbwjxojk")