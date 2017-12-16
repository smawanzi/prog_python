def luminosite(MAT):
    S=0
    for i in range(3):
        for j in range(3):
            S= S + MAT [i][j]
    return(S/9)
MAT = [[1,2,3],[4,5,6],[7,8,9]]        
print(luminosite(MAT))
