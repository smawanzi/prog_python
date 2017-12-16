def insert(element, sequence):
    if sequence==[]:
        return [element]
    elif element<=sequence[0]:
        return [element] + sequence
    else:
        return [sequence[0]] + insert(element, sequence[1:len(sequence)])

 

# La fonction merge prend 2 séquences triées comme arguments.

# Elle retourne une fusion des 2 séquences telles que la séquence résultante est triée.

 

def merge(subSequence1,subSequence2):
    if subSequence1==[]:
        return subSequence2
    elif subSequence2==[]:
        return subSequence1
    else:
        return merge(subSequence1[1:len(subSequence1)],insert(subSequence1[0], subSequence2))

 

# La fonction mergeSort prend la séquence à trier comme argument. La séquence d'entrée est supposée être une liste.

# Cette fonction retourne une permutation de la séquence d'entrée, triée par ordre croissant.

 

def mergeSort(sequence):
    if len(sequence)==0 or len(sequence)==1:
        return sequence
    else:
        return merge(mergeSort(sequence[0:n/2]),mergeSort(sequence[n/2+1:n]))

