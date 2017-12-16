def bin(n):
    q = -1 
    res = '' 
    while q != 0: 
        q = n // 2 
        r = n % 16 
        res = r + res 
        n = q 
    return res 
