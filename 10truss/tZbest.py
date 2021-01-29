def tZbest(Zb,xb,mem,cont,tmax):
    #  Verifica qual a melhor aptidão de todo o enxame
    #
    #    [mem,pmem]= tZbest(Zb,xb,mem,cont,tmax)
    #
    #    mem: histórico com as melhores posições
    #    pmem: posição da atualização na memória das partículas
    #    Zb: aptidão da partícula
    #    xb: posição para aptidão Zb
    #    cont: contador de iterações
    #    np : número de partículas

    Z_p = [Zb, xb]
    Zb_pb = [Z_p][0]#tirei sortrows daqui

    pmem = cont%(0.25*tmax)
    if pmem == 0:
        pmem = 0.25*tmax

    mem[pmem][:] = Zb_pb[0][:]
    mempmem=[mem,pmem]
    return mempmem
