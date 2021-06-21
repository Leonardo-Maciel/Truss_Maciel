import numpy as np
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
    collumns=len(xb[0])+1
    Z_p=np.zeros(shape=(len(Zb),collumns))
    Z_p[:,0]=Zb
    for i in range(len(xb)):
        for j in range(len(xb[0])):
            Z_p[i,j+1] = xb[i,j]
    Z=Z_p
    Zb_pb= np.ones(shape=(len(Z_p),len(Z_p[0])))*np.max(Z_p)
    for i in range(len(Z)):
        for j in range(len(Z)):
            if Z[j][0]<Zb_pb[i][0]:
                Zb_pb[i]=Z[j]
        for k in range(len(Z)):
            if Zb_pb[i][0]==Z[k][0]:
                Z[k][0]=np.max(Z_p)+1
        #tirei sortrows daqui

    pmem = int((cont-1)%(0.25*tmax))
    #if pmem == 0:
    #   pmem = int(0.25*tmax)

    mem[pmem,:] = Zb_pb[0,:]
    mempmem=[mem,pmem]
    return mempmem
