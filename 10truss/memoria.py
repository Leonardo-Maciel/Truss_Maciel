def memoria(fit,p,cont,mem,tmax,np):
    #  Cria o histórico com as posições e aptidões de cada partícula (apenas das
    #  iterações suficientes para o teste de convergência)
    #
    #    [mem,pmem] = memoria(fit,p,cont,mem,tmax,np)
    #
    #    mem: memória da partícula
    #    pmem: posição da atualização na memória
    #    fit: aptidão da partícula
    #    p: posição da partícula
    #    cont: contador de iterações
    #    tmax: número máximo de iterações
    #    np: número de partículas

    pmem = cont%(0.1*tmax)
    if pmem == 0:
        pmem = 0.1*tmax

    for i in range(np):
        mem[pmem][:][i] = [fit[i], p[i][:]]
    mempmem=[mem,pmem]
    return mempmem