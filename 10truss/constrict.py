def constrict(maxc,minc,dell):
    #  Garante que as coordenadas de dell estão dentro dos limites
    #
    #    next = constrict(maxc,minc,dell)
    #
    #    next: vetor avaliado (com coordenadas dentro dos limites)
    #    maxc: valor máximo das coordenadas
    #    minc: valor mímimo das coordenadas
    #    dell: vetor a ser avaliado
    for i in range(len(maxc)):
        if dell[i]>maxc[i]:
            dell[i]=maxc[i]
        if dell[i]<minc[i]:
            dell[i]=minc[i]

    next = dell
    return next