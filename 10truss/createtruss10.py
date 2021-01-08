import numpy as np
from scipy.sparse import csr_matrix
from math import sqrt, atan, sin, cos
"se precisar de algum K1K2K3 TEM Q RESOLVER KEGLBRB!! maxmax tbm é lá"

class createtruss10():

    """
    Entrada de Dados relacionado com a Geometria dos elementos
    """
    def __init__(self,X,Y,conect):

        # forneça as coordenadas dos nos

        self.X = X
        self.Y = Y

        # Forneça a conectividade de cada elemento
        self.conect = conect

        self.sendat()
        #   Calculando o comprimento e os angulos das barras
        self.compang()

        #   Forneça o modulo de elasticidade de cada barra

        self.E = 2.07 * (10 ** 11)
        self.els = self.E * np.ones([1,len(self.conect)])

        self.ro = np.ones([1, len(self.conect)])

        self.props = [self.ang, self.comp, self.els, self.ro]

        #   forneça a area da seçao tansversal de cada elemento

        self.mu = [5, 5, 5]
        self.area = []
        for i in range(len(self.link)):
            self.area.append(self.mu[self.link[i][0]])

        #   Dados relacionado com Graus de liberdade globais da
        #   estrutura construindo a matriz ID
        #			0 => Grau de liberdade livre (desconhecido)
        #			1 => grau de liberdade restrito (conhecido)

        self.ID = np.zeros([len(self.X), 2])
        self.ID[0][0] = 1
        self.ID[0][1] = 1
        self.ID[1][0] = 1
        self.ID[1][1] = 1

        self.nglb = (2 * len(self.X) - np.count_nonzero(self.ID))

        #   Construindo a matriz dos graus de liberdade

        self.glb = self.constroi()

        #   Entrada de Dados relacionado com as Cargas externas

        self.fext = np.zeros(self.nglb)
        self.fext[1] = -1000
        self.fext[5] = -1000

        self.nelem = len(self.conect)
        # la=find(link(:,1)==1)
        # lb=find(link(:,1)==2)
        # lc=find(link(:,1)==3)
        # limit = [length(la) length(lb) length(lc)]

        #self.K = self.keglbrb() ISSO TA DANDO MT ERRO
        # save trussfe.mat X Y conect props area ID nglb glb fext nelem link lpdva
        # save trussrb.mat X Y conect props mu ID nglb glb fext nelem link K1 K2 K3
    
    def sendat(self):
        "Fornece dados para a análise de sensibilidades"

    #   > Entra com no. de variáveis de projeto --- ndvab
    #	> relacao entre as variáveis primárias e secundárias:
    #							---	link(iel,0)= no. da variável primária a qual iel está associada
    #							---	link(iel,1)=  fator de escala entre elas.
    #   > nome do elemento o qual as variáveis primárias estão associadas ---lpdva
    #   > valor da perturbação a ser aplicada --- perturb
    #
    #

        self.ndvab = 3
        #        1   2   3   4   5   6   7   8   9   10
        self.link = [[0, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [1, 0], [2, 0], [0, 0], [2, 0]] #mudei
        self.lpdva = [1, 3, 2]
        self.perturb = 10**-6
    
    def compang(self):

        self.nelm = len(self.conect)
        """ Calculando o comprimento e os angulos das barras"""
        self.comp = []  # comprimentro entre os nós
        self.ang = []  # angulos entre as barras da treliça
        L = []
        teta = []
        A = []
        B = []

        for i in range(self.nelm):
            noj = self.conect[i][0]
            nok = self.conect[i][1]
            L.append(sqrt((self.X[noj] - self.X[nok]) ** 2 + (self.Y[noj] - self.Y[nok]) ** 2))
            self.comp.append(L[i])

        for i in range(self.nelm):
            # nessa parte q ele relaciona as coordenadas com os nós
            A.append(abs(self.X[self.conect[i][1]] - self.X[self.conect[i][0]]))
            if A[i] == 0:
                A[i] = 10 ** (-9)  # ???????

            B.append(abs(self.Y[self.conect[i][1]] - self.Y[self.conect[i][0]]))
            if self.X[self.conect[i][1]] < self.X[self.conect[i][0]]:
                teta.append(atan(A[i] / B[i]))
            else:
                teta.append(atan(B[i] / A[i]))
            self.ang.append(teta[i])
        print(self.ang)
        print(self.comp)
    
    def constroi(self):
        # sub-rotina para construir a matriz LD

        #---------------------------------------------------------
        # nnos = numero de nos
        # ngl = numero de graus de liberdade
        # ID entra como matriz de zeros e uns e sai com uma matriz
        # contendo os indices dos graus de liberdade e
        # zeros nas restriçoes
        # con = contem a conectividade de cada elemento
        # --------------------------------------------------------
        nnos = len(self.ID)
        ngl = 0.0

        for i in range(nnos):
            for j in range(2):
                n = self.ID[i][j]
                if n >= 1:
                    self.ID[i][j]=0.0
                else:
                    ngl = ngl + 1
                    self.ID[i][j] = ngl

        self.LD = np.zeros((self.nelm,4))
        for i in range(self.nelm):
            for j in range(2):
                self.LD[i][j] = self.ID[self.conect[i][0]][j]
                self.LD[i][j+2] = self.ID[self.conect[i][1]][j]
        return self.LD
    def keglbrb(self):
        # Monta a matriz de rigidez global
        global comp1
        global comp2
        global comp3
        #self.nglb = max(max(self.glb))????tirei
        #
        #  atencao isto e especifico p/ 3dv apenas!!!
        #  nelm1 =ultimo no. de elemnto coberto pela dv1
        #  nelm2 =ultimo no. de elemnto coberto pela dv2
        #  nelm3 =ultimo no. de elemnto coberto pela dv3= nelm (no. de elementos totais)
        self.k1 = csr_matrix((self.nglb, self.nglb))
        self.k2 = csr_matrix((self.nglb, self.nglb))
        self.k3 = csr_matrix((self.nglb, self.nglb))
        #    k1 = zeros(nglb,nglb)
        #    k2 = zeros(nglb,nglb)
        #    k3 = zeros(nglb,nglb)

        #    nelm1 = limit(1)
        #    nelp1 = nelm1 + 1
        #    nelm2 = limit(1) + limit(2)
        #    nelp2 = nelm2 + 1

        #
        #  make a equal unity so the old routine keltr can be used
        #
        #
        #  also computes the sum of comp per region for later usage in sensitivity
        #  analysis
        #
        aa = np.ones(self.nelm)
        comp1 = 0.0
        comp2 = 0.0
        comp3 = 0.0

        for i in range(self.nelm):
            self.keltr(aa[i], self.comp[i], self.els[i], self.ang[i])
            id = np.flatnonzero(self.glb[:][i])
            gb = self.glb[id][i]

            if self.link[i][0] == 0:
                self.k1[gb][gb] = self.k1[gb][gb] + self.ke[id][id]
                self.comp1 = self.comp1 + self.comp[i]

            if self.link[i][0] == 1:
                self.k2[gb][gb] = self.k2[gb][gb] + self.ke[id][id]
                self.comp2 = self.comp2 + self.comp[i]

            if self.link[i][0] == 2:
                self.k3[gb][gb] = k3[gb][gb] + ke[id][id]
                self.comp3 = self.comp3 + self.comp[i]

        #
        # for i = nelp1:nelm2
        #         ke = keltr(aa(i),comp(i),els(i),ang(i))
        #         id = find(glb(:,i))
        #         gb = glb(id,i)
        #         k2(gb,gb) = k2(gb,gb) + ke(id,id)
        #         comp2 = comp2  + comp(i)
        # end
        # for i = nelp2:nelm
        #         ke = keltr(aa(i),comp(i),els(i),ang(i))
        #         id = find(glb(:,i))
        #         gb = glb(id,i)
        #         k3(gb,gb) = k3(gb,gb) + ke(id,id)
        #         comp3 = comp3  + comp(i)
        # end
        # c1 = comp1
        # c2 = comp2
        # c3 = comp3
    
    def keltr(self,area,ls,els,teta):
        self.ke = np.zeros((4, 4))
        s = sin(teta)
        c = cos(teta)
        kl = area * els / ls
        self.ke[0][0] = kl * c * c
        self.ke[0][1] = kl * c * s
        self.ke[0][2] = -kl * c * c
        self.ke[0][3] = -kl * c * s

        self.ke[1][0] = kl * c * s
        self.ke[1][1] = kl * s * s
        self.ke[1][2] = -kl * s * c
        self.ke[1][3] = -kl * s * s

        self.ke[2][0] = -kl * c * c
        self.ke[2][1] = -kl * c * s
        self.ke[2][2] = kl * c * c
        self.ke[2][3] = kl * c * s

        self.ke[3][0] = -kl * c * s
        self.ke[3][1] = -kl * s * s
        self.ke[3][2] = kl * s * c
        self.ke[3][3] = kl * s * s

createtruss10(X = [0, 0, 50, 50, 100, 100],Y = [0, 50, 0, 50, 0, 50],
              conect = [[0, 2], [2, 4], [0, 3], [2, 1], [2, 3], [2, 5], [4, 3], [4, 5], [1, 3], [3, 5]])