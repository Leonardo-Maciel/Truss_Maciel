"""Fornece para o otimizador as funcões objetivo e restrição"""
from optsolpso import optsolpso
import numpy as np
def funpso(para,props,con,penal,x,fext,glb,link):

    #
    #	Pega  nas variaveis  "para"  , "props"  e "con" alguns
    #  paramentros adicionais
    tpobj = para[1]
    tpres = para[2]
    f0 = para[3]
    #
    clb = con[0][:]
    cub = con[1][:]
    #
    # Compara os vetores das variáveis de projeto
    #
    #--------------------------------------------------------------------------
    optsolPSO = optsolpso()
    fobfre = optsolPSO.fobfre(props,fext,glb,link,tpobj,tpres,x)
    fob= fobfre[0]
    fre= fobfre[1]
    #--------------------------------------------------------------------------
    #   Pega os valores das funcões objetivo e restrição
    #  as restrições são normalisadas e são do tipo <=0!!
    #
    #     funcões objetivo:
    #
    f = fob
    #
    #     compute das restrições  normalisadas:
    #
    nsize = len(fre)
    rnor = np.zeros(2*nsize)
    for isize in range(nsize):
        #icon = isize
        rnor[isize] = (fre[isize] -  cub[isize])/cub[isize]
        rnor[isize + nsize] = (clb[isize] - fre[isize])/abs(clb[isize])

    #
    #    finalmente as funcões restrição

    soma = 0
    g = rnor

    #--------------------------------------------
    # Função fitnnes para PSO
    #--------------------------------------------
    for ir in range(2*nsize):
       if g[ir] > 1e-6:
           soma = soma + g[ir]**2

    f = f/f0 + penal*soma
    t=0
    if soma!=0:
        t=1
    ft=[f,t]
    return ft
