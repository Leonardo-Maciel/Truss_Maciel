import random
def atualiza(pbest,sbest,w,c1,c2,p,vel,t):
    """Atualiza a velocidade das partículas penalizando-as se necessário"""
    #
    #    del = atualiza(pbest,sbest,w,c1,c2,p,vel,t)
    #
    #    del: vetor velocidade atualizado
    #    pbest: melhor posição da partícula encontrada até o momento
    #    Sbest: melhor posição no enxame no momento
    #    w: inércia do enxame
    #    c1: parâmetro de confiança da partícula em si
    #    c2: parâmetro de confiança no enxame
    #    P: posição atual da partícula no enxame
    #    vel: velocidade atual da partícula
    #    t: parâmetro para atualização da velocidade

    if t==1:
        dell = c1*random.random()*(pbest-p) + c2*random.random()*(sbest-p)
    else:
        dell = w*vel + c1*random.random()*(pbest-p) + c2*random.random()*(sbest-p)

    return dell