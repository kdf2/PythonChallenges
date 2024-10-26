def mergeAlternately( word1, word2):
    unir=[]
    for l1, l2 in zip(word1, word2):
        unir.append(l1)
        unir.append(l2)
    unir.append(word1[len(word2):] or word2[len(word1):])
    return ''.join(unir)


word1=input("ingrese la palabra 1: ")
word2=input("Ingrese la palabra 2: ")
print(mergeAlternately(word1,word2))

    