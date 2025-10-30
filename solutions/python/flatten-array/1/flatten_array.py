def flatten(iterable):
    res = []
    for i in iterable:
        if isinstance(i, list):
            for j in i:
                res.append(j)
        elif i != None: res.append(i)
    if res == iterable: 
        return res
    else: 
        return flatten(res)
