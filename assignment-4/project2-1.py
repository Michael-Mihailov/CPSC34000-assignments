def balanced_parentheses(s: str):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True


# NOTE: The below test cases are from the textbook. The above code passes all test cases.
print(balanced_parentheses("(a(b+c)(d+(fg)h)d)")) # True
print(balanced_parentheses("(((ab)))"))           # True
print(balanced_parentheses("(a)(b)()()((()()))")) # True

print(balanced_parentheses("(ab(c)(d)(())"))      # False
print(balanced_parentheses("()())"))              # False
print(balanced_parentheses("(()()"))              # False
