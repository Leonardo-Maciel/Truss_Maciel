import numpy as np

def optdat10(area,lpdva,ndvab,nglb):
    """Fornece dados para a otimizacao"""
    #	                           	 Tipo de funcao objetivo: tpobj==1 ---Peso
    #                                tpobj==2 ---Energia
    #                                tpobj==3 ---Máxima tensão
    #                                tpobj==4 ---Máximo deslocamento
    #
    tpobj = 1
    #
    #	 	Tipo de funcao restrição: tpres==1 ---Peso
    #                                 tpres==2 ---Tensão
    #				                  tpres==3 ---Tensão e deslocamento
    #                                 tpres==4 ---Deslocamento
    #                                 tpres==5 ---Energia
    tpres = 2
    #
    #       Entrar com os valores limites das variáveis de projeto
    #               vlb---limite inferiores
    #               vub---limite superiores
    #               x0 --- valor inicial
    #


    xpdva = np.zeros(ndvab)
    for idvab in range(ndvab):
        iel = lpdva[idvab]
        xpdva[idvab] = area[iel]

    x0 = xpdva
    vlb = 0.1 * np.ones(ndvab)
    vlb = 0.1 * np.ones(ndvab)
    vub = 10 * np.ones(ndvab)

    #
    #         	Entrar com os valores limites das restrições
    #               clb---limites inferiores
    #               cub---limites superiores

    cones = np.ones(len(area))  # relacionado ao nº de elementos
    cones2 = np.ones(nglb)  # relacionado ao nº de graus de liberdade

    clb1 = -250 * cones
    cub1 = 250 * cones
    #         clb1 = -20*cones
    #         cub1 = 20*cones

    #         dlb1 = -0.4*cones2
    #         dub1 = 0.4*cones2

    clbv = 1.5e+06 - 2.2204e-16  # 0
    cubv = 1.5e+06

    clbd = -1 * (10 ** -3) * cones2
    cubd = 1 * (10 ** -3) * cones2

    elbv = 2e-2
    eubv = 2e-2

    if tpres == 1:
    # VOLUME
        cub = cubv
        clb = clbv
    elif tpres == 2:
    # TENSOES
        clb = clb1
        cub = cub1
    elif tpres == 3:
    # TENSOES e DESLOCAMENTOS
        clb = [clb1, clbd]
        cub = [cub1, cubd]
    elif tpres == 4:
    # DESLOCAMENTOS
        clb = clbd
        cub = cubd
    else:
    # ENERGIA
        clb = elbv
        cub = eubv

    dadosoptdat10= [tpobj,tpres,vlb,vub,x0,clb,cub]

    return dadosoptdat10
