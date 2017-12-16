def contraste(MAT):
    m=5
    for i in range(3):
        for j in range(3):
            if MAT[i][j] < m:
                MAT[i][j] = MAT[i][j]/2
            else:
                MAT[i][j]=2*MAT[i][j]
                if MAT [i][j]>100:
                    MAT[i][j] = 100
    return (MAT)
MAT = [[1,2,3],[4,5,6],[7,8,9]]        
print(contraste(MAT))
