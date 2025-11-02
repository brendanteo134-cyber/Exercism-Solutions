def is_paired(input_string):
    open_brackets = ["[", "{", "("]
    closed_brackets = ["]", "}", ")"]
    stack = []
    for i in input_string:
        if i in open_brackets:
            stack.append(i)
        elif i in closed_brackets:
            pos = closed_brackets.index(i)
            if ((len(stack)>0) and (open_brackets[pos]==stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
