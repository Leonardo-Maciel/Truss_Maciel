import numpy as np
def createtruss10(self):
    # Entrada de Dados relacionado com a Geometria dos elementos
    # forneça as coordenadas dos nos

    self.X = [0, 0, 50, 50, 100, 100]
    self.Y = [0, 50, 0, 50, 0, 50]

    # Forneça a conectividade de cada elemento
    self.conect = [[0, 2], [2, 4], [0, 3], [2, 1], [2, 3], [2, 5], [4, 3], [4, 5], [1, 3], [3, 5]] #mudei

    self.sendat()
    #   Calculando o comprimento e os angulos das barras
    self.compang(X, Y, conect)

    #   Forneça o modulo de elasticidade de cada barra

    self.E = 2.07 * (10 ** 11)
    self.els = E * np.ones([1, len(conect)])

    self.ro = np.ones([1, len(conect)])

    self.props = [self.ang, self.comp, self.els, self.ro]

    #   forneça a area da seçao tansversal de cada elemento

    self.mu = [5, 5, 5]
    self.area = []
    for i in range(len(link)):
        self.area.append(mu[link[i][0]])

    #   Dados relacionado com Graus de liberdade globais da
    #   estrutura construindo a matriz ID
    #			0 => Grau de liberdade livre (desconhecido)
    #			1 => grau de liberdade restrito (conhecido)

    self.ID = np.zeros([len(X), 2])
    ID[0][0] = 1
    ID[0][1] = 1
    ID[1][0] = 1
    ID[1][1] = 1

    self.nglb = (2 * len(X) - np.count_nonzero(ID))

    #   Construindo a matriz dos graus de liberdade

    self.glb = constroi(ID, conect)

    #   Entrada de Dados relacionado com as Cargas externas

    self.fext = np.zeros(self.nglb, 1)
    self.fext[1] = -1000
    self.fext[5] = -1000

    self.nelem = length(conect)
    # la=find(link(:,1)==1)
    # lb=find(link(:,1)==2)
    # lc=find(link(:,1)==3)
    # limit = [length(la) length(lb) length(lc)]

    self.K = keglbrb(comp, els, ang, glb, link)
    # save trussfe.mat X Y conect props area ID nglb glb fext nelem link lpdva
    # save trussrb.mat X Y conect props mu ID nglb glb fext nelem link K1 K2 K3
