def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    
    if sq < 0:
        return -1
    
    left = 0
    right = sq
    
    while left <= right:
        mid = (left + right) // 2
        mid_sq = mid * mid
        
        if mid_sq == sq:
            return (mid + 1) * (mid + 1)
        elif mid_sq < sq:
            left = mid + 1
        else:
            right = mid - 1
          
    return -1

