def invert(lst):
    if not lst:
        return []
    
    inverted_elements = []
    
    for i in lst:
        inverted_elements.append(-i)
        
    return inverted_elements
