postfix1 = "532+7*-"
postfix2 = "235*+7-"
stack = []


def calculate_by_enum(val1, val2, enum):
    if enum == "+":
        return val1 + val2
    elif enum == "-":
        return val1 - val2
    elif enum == "*":
        return val1 * val2
    elif enum == "/":
        return val1 / val2

for each in postfix1:
    if each in "+-*/":
        num2 = stack.pop()
        num1 = stack.pop()
        result = calculate_by_enum(num1, num2, each)
        stack.append(result)
    else :
        stack.append(int(each))

print(stack)