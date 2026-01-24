def filter_list(l):
    'return a new list with the strings filtered out'
    numeric_list = []
    
    for i in l:
        if not isinstance(i, str):
            numeric_list.append(i)
            
    return numeric_list
