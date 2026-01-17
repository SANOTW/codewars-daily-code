def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        string_ = string_.replace(i, '')
        string_ = string_.replace(i.upper(), '')
    return string_
