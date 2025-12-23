def answer(question):
    substitutions=[("plus", "+"), ("minus", "-"), ("times", "*"), ("multiplied by", "*"),("divided by", "/")]
    if question[:7] == "What is":
        question = question[7:]
    if question[-1] == "?":
        question = question[:-1]
    question = question.strip()
    if not question:
        raise ValueError("syntax error")
    for s in substitutions:
        question = question.replace(*s)
    sequence = question.split(" ")
    register = op_register = None
    for item in sequence:
        if item.isnumeric() or (item[0] == "-" and item[1:].isnumeric()):
            if register == None:
                register = eval(item)
            elif op_register:
                register = eval("{}{}{}".format(register, op_register, item))
                op_register = None
            else:
                raise ValueError("syntax error")
        elif item in ["+", "-", "*", "/"]:
            if op_register or register == None:
                raise ValueError("syntax error")
            op_register = item
        else:
            raise ValueError("unknown operation", item)
    if op_register or register == None:
        raise ValueError("syntax error")
    return register