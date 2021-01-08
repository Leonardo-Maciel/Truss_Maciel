# sub-rotina para construir a matriz LD

#---------------------------------------------------------
# nnos = numero de nos
# ngl = numero de graus de liberdade
# ID entra como matriz de zeros e uns e sai com uma matriz
# contendo os indices dos graus de liberdade e
# zeros nas restriçoes
# con = contem a conectividade de cada elemento
# --------------------------------------------------------
def constroi(self,ID,conect):

    nnos = len(ID)
    ngl = 0.0

    for i in range(nnos):
        for j in range(2):
            n = ID[i][j]
            if n >= 1:
                ID[i][j]=0.0
            else:
                ngl = ngl + 1
                ID[i][j] = ngl

    nelm = len(conect)
    LD = np.zeros((nelm,4))
    for i in range(nelm):
        for j in range(2):
            LD[i][j] = ID[conect[i][0]][j]
            LD[i][j+1] = ID[conect[i][1]][j]#mudei mas fiquei na duvida nesse j+2
    return LD