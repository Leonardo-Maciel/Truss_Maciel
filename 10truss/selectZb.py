def selectZb (Zb,fit,xb,t,p,nparticulas):
    #  Seleciona a melhor forma encontrada pela partícula até o memento
    #
    #    [Zb,xb,t] = selectZb (Zb,fit,xb,t,p,np)
    #
    #    Zb: melhor forma da partícula
    #    xb: melhor posição da partícula encontrada até o momento
    #    t: parâmetro para atualização da velocidade
    #    fit: forma da partícula no momento
    #    p: posição atual da partícula no enxame
    #    np: número de partículas
    #    obj: psoição do objetivo analizado (otimização multiobjetivo)

    for i in range(nparticulas):
        if fit[i] < Zb[i]:
            Zb[i] = fit[i]
            xb[i][:] = p[i][:]
            t[i]=0
        else:
            t[i]=1
    Zbxbt=[Zb,xb,t]
    return Zbxbt