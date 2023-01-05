def reverse(x):
    rev = 0
    sign = 1 if x >= 0 else -1
    x = abs(x)
    while x > 0:
        rev = rev * 10 + x % 10
        if rev > 2**31 - 1:
            return 0
        x //= 10
    return rev*sign

reverse(123)
reverse(-123)
reverse(120)
