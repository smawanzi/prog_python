def lumi(mat):
   s=0
   for i in range(3):
       for j in range(3):
           s=s + mat [i][j]
   return (s/9)
mat=[[1,2,3],[4,5,6],[7,8,9]]

print(lumi(mat))
