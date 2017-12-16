def fusion(T1,T2) :
    if T1==[] :return T2
    if T2==[] :return T1
    if T1[0]< T2[0] :
        return [T1[0]]+fusion(T1[1 :],T2)
    else :
        return [T2[0]]+fusion(T1,T2[1 :])
def tableau(tab):
    for k in range(len(tab)):
        if k%10==9:
            print(tab[k])
        else:
            print(tab[k],"\t",end=" ")
