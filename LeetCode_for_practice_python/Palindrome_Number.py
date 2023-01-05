def isPalindrome(x):
    Ans = False
    strcheck = ""
    strcheckpalindrome = ""

    strcheck = str(x)
    strcheckpalindrome = str(x)[::-1]

    if(strcheck == strcheckpalindrome):
        Ans = True

    return Ans

isPalindrome(121)
isPalindrome(-121)
isPalindrome(10)