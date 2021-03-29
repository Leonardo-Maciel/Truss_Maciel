def compang(x, y, conect):
    x = x
    y = y
    nelm = 13
    connect = conect
    """ Calculando o comprimento e os angulos das barras"""
    comp = []  # comprimentro entre os nós
    ang = []  # angulos entre as barras da treliça
    L = []
    teta = []
    A = []
    B = []

    for i in range(nelm):
        noj = connect[i][0]
        nok = connect[i][1]
        L.append(sqrt((x[noj] - x[nok]) ** 2 + (y[noj] - y[nok]) ** 2))
        comp.append(L[i])

    for i in range(nelm):
        # nessa parte q ele relaciona as coordenadas com os nós
        A.append(abs(x[connect[i][1]] - x[connect[i][0]]))
        if A[i] == 0:
            A[i] = 10 ** (-9)  # ???????

        B.append(abs(y[connect[i][1]] - y[connect[i][0]]))
        if x[connect[i][1]] < x[connect[i][0]]:
            teta.append(atan(A[i] / B[i]))
        else:
            teta.append(atan(B[i] / A[i]))
        ang.append(teta[i])
    print(ang)
    print(comp)
    ang_comp=[ang,comp]
    return ang_comp
