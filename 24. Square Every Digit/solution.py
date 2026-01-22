def square_digits(num):
    # Your code here
    result = ''
    
    for i in str(num):
        result = result + str(int(i) * int(i))
        
    return int(result)
