def memoria(fit,p,cont,mem,tmax,nparticulas):
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

    pmem = int(cont%(0.1*tmax))
    #if pmem == 0:
    #    pmem = int(0.1*tmax)

    for i in range(nparticulas):
        mem[pmem,0,i] = fit[i]
        mem[pmem,1:,i]=p[i][:]
    mempmem=[mem,pmem]
    return mempmem