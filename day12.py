# Valid Parentheses with Multiple Types


s="[[{}]]"


def valid_parenthesis(s):

    parenthesis = {")": "(",
                   "}": "{",
                   "]": "["}
    stack = []

    for i in s:
        if i in parenthesis.values():
            stack.append(i)
        elif i in parenthesis.keys():
            if stack and parenthesis.get(i)==stack[-1]:
                stack.pop()
            else:
                return False
        else:
            return False
            
    return True

print(valid_parenthesis(s))
