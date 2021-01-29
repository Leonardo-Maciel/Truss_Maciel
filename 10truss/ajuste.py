import random
def ajuste(mem,np,wo):

    """Atualiza a inércia do enxame OBS: MUDEI OS CALCULOS"""
    #
    #    wn = ajuste(mem,np,wo)
    #
    #    wn: inércia (atualizada)
    #    mem: memória das partículas
    #    np: número de partículas
    #    wo: inércia (a ser atualizada)

    wn=random.random*wo
    if wn > 1.4:
        wn = wo * 0.975

    elif wn < 0.8:
        wn = 0.8

    return wn