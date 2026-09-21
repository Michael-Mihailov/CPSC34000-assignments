def intToHex(num):
    hex_characters = "0123456789ABCDEF"
    def helper(num):
        if num == 0:
            return ""
        return helper(num // 16) + hex_characters[num % 16]

    if num < 0:
        return "-" + helper(-num)
    if num == 0:
        return "0"
    return helper(num)