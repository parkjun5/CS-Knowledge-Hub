str1 = "3 + 2 * 7"
str2 = "3 * 2 - 7"
str3 = "5 - ( 3 + 2 ) * 7"
result = ""
split_str = str3.split()

stack = []

for each in split_str:
    if each == "(":
        stack.append(each)

    elif each == ")":
        while len(stack) > 0 and stack[-1] != "(":
            result += stack.pop()
        stack.pop()

    elif each in "+-*/":
        if each in "+-":
            while len(stack) > 0 and stack[-1] in "*/":
                result += stack.pop()
            stack.append(each)
        else:
            stack.append(each)
    else :
        result += each


for index in range(len(stack)):
    result += stack.pop()

print(result)