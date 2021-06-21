import random
import statistics
def ajuste(mem,nparticulas,wo):

    """Atualiza a inércia do enxame OBS: MUDEI OS CALCULOS"""
    #
    #    wn = ajuste(mem,np,wo)
    #
    #    wn: inércia (atualizada)
    #    mem: memória das partículas
    #    np: número de partículas
    #    wo: inércia (a ser atualizada)

    #wn=random.random*wo
    memsel = mem[:round(0.2 * nparticulas)]
    covar=statistics.mean(memsel)/statistics.stdev(memsel)
    if covar < 1:
        wn = wo * 0.975
    else:
        wn = wo
    if wn < 0.35:
        wn = 0.35
    return wn