def createtruss10():

    # Entrada de Dados relacionado com a Geometria dos elementos
    #
    # forneça as coordenadas dos nos

    X = [0,0,50,50,100,100]
    Y = [0,50,0,50,0,50]

    # Forneça a conectividade de cada elemento
    conect = [[1, 3],[3, 5],[1, 4],[3, 2],[3, 4],[3, 6], [5, 4],[5, 6],[2, 4],[4, 6]]

    [ndvab,link,lpdva] = sendat
    #   Calculando o comprimento e os angulos das barras
    [ang,comp] = compang(X,Y,conect)

    #   Forneça o modulo de elasticidade de cada barra

    E = 2.07*(10**11)
    els = E*ones([1,length(conect)])

    ro = ones([1,length(conect)])

    props = [ang,comp,els,ro]

    #   forneça a area da seçao tansversal de cada elemento

    mu = [5, 5, 5]
    area = mu(link(:,1))
    #   Dados relacionado com Graus de liberdade globais da
    #   estrutura construindo a matriz ID
    #			0 => Grau de liberdade livre (desconhecido)
    #			1 => grau de liberdade restrito (conhecido)

    ID = zeros([length(X),2])
    ID(1,1)=1
    ID(1,2)=1
    ID(2,1)=1
    ID(2,2)=1
    #ID(3,1)=1
    #ID(3,2)=1
    #ID(4,1)=1
    #ID(4,2)=1

    nglb=(2*length(X)-nnz(ID))

    #   Construindo a matriz dos graus de liberdade

    glb=constroi(ID,conect)

    #
    #   Entrada de Dados relacionado com as Cargas externas
    #
    fext=zeros(nglb,1)
    fext(2) = -1000
    fext(6) = -1000

    nelem = length(conect)
    # la=find(link(:,1)==1)
    # lb=find(link(:,1)==2)
    # lc=find(link(:,1)==3)
    # limit = [length(la) length(lb) length(lc)]

    [K1, K2, K3] = keglbrb(comp,els,ang,glb,link)
    #save trussfe.mat X Y conect props area ID nglb glb fext nelem link lpdva
    #save trussrb.mat X Y conect props mu ID nglb glb fext nelem link K1 K2 K3