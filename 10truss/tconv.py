import numpy as np
import statistics

def tconv(Zb, mp, pp, Zbsf, ppb, t, cond, tmax, np):
    """Avaliação dos critérios para encerramento do procedimento de otimizaçao"""
    #  via aglomeraçao de particulas (Particle Swarm Optimization - PSO)
    #
    #    [conv,cond] = tconv(Zb,mp,pp,Zbsf,ppb,t,cond,tmax,np)
    #
    #    conv: parâmetro que indica a convergência do enxame
    #    cond: parâmetro que indica se há a necessidade de avaliação na melhor
    #          aptidão do enxame
    #    Zb: apitidão da partícula
    #    mp: memória da partícula
    #    pp: posição atual da partícula na memória
    #    Zbsf: memória das melhores aptidões
    #    ppb: posição atual da melhor partícula na memória das melhores partículas
    #    t: contador de iterações
    #    tmax: número máximo de iterações
    #    np: número de partículas

    ver1 = 0
    ver2 = 0
    ver3 = 0
    dc = np.zeros(100, 10)
    # first termination condition
    gworst = max(Zb)
    gbest = min(Zb)
    den = gworst - gbest
    if (ppb - 99) <= 0:
        cgbest = [Zbsf[(0.25 * tmax) - (99 - ppb):][0], Zbsf[1:ppb+1][0]]
        dif = Zbsf[(0.25 * tmax) - (99 - ppb)][0] - Zbsf[ppb][0]
    else:
        cgbest = Zbsf[ppb - 99:ppb+1][0]
        dif = Zbsf[ppb - 99][0] - Zbsf[ppb][0]

    for i in range(np):
        if (pp - 99) <= 0:
            cg = [mp[(0.1 * tmax) - (99 - pp):][0][i], mp[0:pp+1][0][i]]
        else:
            cg = mp[pp - 99:pp+1][0][i]

        dc[:][i] = cg - cgbest
    dcm=[]
    for i in range(len(dc)):
        dcm.append(statistics.mean(dc[i][:]))
    if den == 0:
        den = 10 ** -15

    rel1 = sum(dcm) / (100 * den)
    rel2 = dif / (100 * den)
    if rel1 < 10 ** -12:
        ver1 = 1

    if rel2 < 10 ** -15:
        ver2 = 1

    # rel1 ---> rel_c_me: avalia a razão entre a diferença da aptidão de cada partícula
    #                     em relação a melhor aptidão encontrada pelo enxame nas últimas
    #                     100 iterações, e a diferença entre a pior e a melhor aptidão
    #                     encontradas na iteração
    # rel2 ---> rel_c_cgbest: avalia a razão entre a diferença da atual melhor aptidão encontrada
    #                         em relação a melhor aptidão encontrada a 100 iterações anteriores,
    #                         e a diferença entre a pior e a melhor aptidão encontradas na iteração

    if (ver1 + ver2) < 2:
        cond = cond + 1

    # second termination condition
    #   Avalia num determinado período de iterações a variação na melhor aptidão
    #   encontrada pelo enxame

    if cond%10 == 0 and t > 0.25 * tmax:
        if (ppb - 0.25 * tmax) < 0:
            relcb = Zbsf[ppb + 1][0] - Zbsf[ppb][0]
        else:
            relcb = Zbsf[0][0] - Zbsf[ppb][0]

        if relcb == 0:
            ver3 = 1

    if ver3 == 1 or (ver1 + ver2) == 2:
        conv = 1
    else:
        conv = 0

    convcond=[conv, cond]
    return convcond

