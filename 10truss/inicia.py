import numpy as np
"""Função que inicializa os dados de cada partícula (velocidade e posição)"""
def inicia(dim,nparticulas,lb,ub):

    #    [pnext,vel,minp,maxp,minv,maxv] = inicia(dim,np,lb,ub)
    #
    #    pnext: posição da partícula no enxame
    #    vel: velocidade da partícula
    #    dim: dimenção da partícula
    #    np: número de partículas
    #    lb: cota mínima
    #    ub: cota máxima

    delmin = -0.5*(ub-lb)              # limites para as mudanças locais
    delmax = 0.5*(ub-lb)               #
    minp=np.zeros(shape=(nparticulas,dim))
    maxp=np.zeros(shape=(nparticulas,dim))
    minv=np.zeros(shape=(nparticulas,dim))
    maxv=np.zeros(shape=(nparticulas,dim))

    pnext=np.zeros(shape=(nparticulas,dim))
    vel=np.zeros(shape=(nparticulas,dim))

    rp = np.random.rand(nparticulas, dim)
    rv = np.random.rand(nparticulas, dim)

    for i in range(nparticulas):
        for j in range(dim):
            minp[i,j] = minp[i,j]+lb[j]              #
            maxp[i,j] = maxp[i,j]+ub[j]              # valores máximos e mínimos para cada
            minv[i,j] = minv[i,j]+delmin[j]         # coordenada da posição e da velociade
            maxv[i,j] = maxv[i,j]+ delmax[j]         #


            pnext[i,j] = (minp[i,j] + rp[i,j]*(maxp[i,j] - minp[i,j]))  # posições iniciais
            vel[i,j] = (minv[i,j] + rv[i,j]*(maxv[i,j] - minv[i,j]))    # velocidades iniciais
    pnextvel=[pnext, vel]
    return pnextvel