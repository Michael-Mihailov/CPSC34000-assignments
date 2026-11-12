def hash1(s):
    ans = 0
    for i in range(len(s)):
        code = ord(s[i])
        ans += code
    return ans % 20


def hash2(num):
    return ((num * 21) % 37)


def hash3(num):
    square = num * num
    squareStr = str(square)
    if len(squareStr) <= 3:
        return square
    else:
        startIndex = (len(squareStr) - 3) // 2
        midDigits = squareStr[startIndex : (startIndex + 3)]
        return int(midDigits)


def hash4(s):
    ans = 0
    multiplier = 1
    for i in range(len(s)):
        code = ord(s[i])
        ans += code * multiplier
        multiplier *= 7
    return ans


def hash5(num):
    MAGIC_NUMBER = 0.6180339887
    num = (num * MAGIC_NUMBER)
    num = num - int(num)
    num *= 31
    num = int(num)
    return num
