def count_positives_sum_negatives(arr):
    if not arr:
        return []

    result = [0, 0]
    
    for integer in arr:
        if integer < 0:
            result[1] += integer
        elif integer > 0:
            result[0] += 1
            
    return result
