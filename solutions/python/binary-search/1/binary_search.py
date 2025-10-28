def find(search_list, value):
    if value in search_list: return search_list.index(value)
    else: raise ValueError("value not in array")
        
