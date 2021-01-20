import numpy as np
"""Função que inicializa os dados de cada partícula (velocidade e posição)"""
def inicia(dim,np,lb,ub):

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

    minp = np.ones(np,1)*lb              #
    maxp = np.ones(np,1)*ub              # valores máximos e mínimos para cada
    minv = np.ones(np,1)*delmin          # coordenada da posição e da velociade
    maxv = np.ones(np,1)*delmax          #

    rp=np.random.rand([np,dim])
    rv=np.random.rand([np,dim])

    pnext = (minp + rp*(maxp - minp))  # posições iniciais
    vel = (minv + rv*(maxv - minv))    # velocidades iniciais
    pnextvel=[pnext, vel]
    return pnextvel