"""Realiza a Otimizacao da estrutura"""
import numpy as np
from scipy import sparse
from createtruss10 import createtruss10
from math import sin, cos
class optsolpso():
    def __init__(self):
        """Fornece valores para as funcões objetivo e restrição e atualiza todas as variáveis primárias"""
        #
        #ang = props[0][:]
        #comp = props[1][:]
        #els = props[2][:]

        #
        # Faz a solução via o MEF para avaliação das funções.
        #
    def fobfre(self,props, fext, glb, link, tpobj, tpres, x):
        area = self.getval(props[1][:], x, link)
        self.fesol(area, props[0][:], props[1][:], props[2][:], fext, glb)
        en = np.transpose(fext)*self.u
        #
        # guarda na variavel  ' 'par' alguns paramentros adicionais
        #
        #	par = [ndvab]
        #
        # Armazena todas as funções
        #
        if tpobj == 1:
            fob = self.vol
        elif tpobj == 2:
            fob = en
        elif tpobj == 3:
            fob = max(abs(self.sig))
        elif tpobj == 4:
            fob = max(abs(self.u))

        if tpres == 1:
            fre = self.vol
        elif tpres == 2:
            fre = self.sig
        elif tpres == 3:
            fre = [self.sig, self.u]
        elif tpres == 4:
            fre = np.transpose(self.u)
        else:
            fre = en
        fobfre=[fob,fre]
        return fobfre
    def getval(self,comp,xvalu,link):
        #
        #  atualiza as variáveis
        #
        #
        # dimensoes:
        #

        nelem  = len(comp)
        #
        #  inicializa
        #
        self.area = np.zeros(nelem)
        #
        #  atualiza
        #
        for jelem in range(nelem):
            ivp = link[jelem][0]
            scal = link[jelem][1]
            self.area[jelem] = xvalu[ivp] * scal
        return self.area

    def fesol(self,area, ang, comp, els, fext, glb):

        #
        # Realiza Análise via o MEF
        #

        #
        # Matriz de rigidez global:
        #
        self.kg = self.keglb(area, comp, els, ang, glb)
        #
        # Deslocamentos:
        #
        self.u = np.linalg.solve(self.kg, fext)
        #
        # Esforços:
        #
        self.esf = self.tresf(area, comp, els, ang, glb, self.u)
        #
        # Tensões:
        #
        self.sig = self.sigma(area, comp, self.esf)
        #
        # Volume:
        #
        self.vol = self.volume(area, comp)


    def keglb(self,area, comp, els, ang, glb):
        # Monta a matriz de rigidez global

        self.nelm = len(comp)
        nglb = int(glb.max())
        glb=np.array(glb)
        kgb = np.zeros(shape=(nglb, nglb))#mudei de sparse.csr_matrix

        for i in range(self.nelm):
            ke = createtruss10.keltr(self,area[i], comp[i], els[i], ang[i])
            id = np.flatnonzero(glb[:,i])
            gb = glb[id,i]-1
            for a in range(len(gb)):
                for b in range(len(gb)):
                    kgb[gb[a],gb[b]] = kgb[gb[a],gb[b]] + ke[id[a],id[b]]

        return kgb

    def tresf(self,area, comp, els, ang, glb, u):

        esf = np.zeros(self.nelm)
        glb=np.array(glb)
        for i in range(self.nelm):

            ae = [-cos(ang[i]), -sin(ang[i]), cos(ang[i]), sin(ang[i])]
            id = np.flatnonzero((glb[:,i]))
            gb = glb[id[0]:(id[-1]+1),i]-1
            uo = u[gb]
            #produto escalar entre os 2 vetores
            en = np.dot(ae[id[0]:(id[-1]+1)],uo)
            kl = area[i] * els[i] / comp[i]
            esf[i] = kl * en

        return esf

    def sigma(self,area, comp, esf):
        #
        # Calcula as tensões nas barras
        #
        sig = np.zeros(self.nelm)
        for i in range(self.nelm):
            sig[i] = esf[i] / area[i]

        return sig

    def volume(self,area, comp):
        # Calcula o volume total das barras.
        #
        nelem=len(comp)
        vol = 0.0
        for ielem in range(nelem):
            vol = vol + (area[ielem] * comp[ielem])

        return vol

"""optsolpso=optsolpso()
fobfre=optsolpso.optsolpso(props=[[0.0, 0.0, 0.7853981633974483, 2.356194490192345, 1.5707963267748966, 0.7853981633974483, 2.356194490192345, 1.5707963267748966, 0.0, 0.0], [50.0, 50.0, 70.71067811865476, 70.71067811865476, 50.0, 70.71067811865476, 70.71067811865476, 50.0, 50.0, 50.0], [2.07e+11, 2.07e+11, 2.07e+11, 2.07e+11, 2.07e+11, 2.07e+11,
       2.07e+11, 2.07e+11, 2.07e+11, 2.07e+11], [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]],fext=[0, -1000, 0, 0, 0, -1000, 0, 0],glb=[[0, 1, 0, 1, 1, 1, 5, 5, 0, 3,], [0, 2, 0, 2, 2, 2, 6, 6, 0, 4], [1, 5, 3, 0, 3, 7, 3, 7, 3, 7], [2, 6, 4, 0, 4, 8, 4, 8, 4, 8]],link=[[0, 1], [1, 1], [1, 1], [1, 1], [2, 1], [2, 1], [1, 1], [2, 1], [0, 1], [2, 1]],tpobj=1,tpres=2,x=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
fob=fobfre[0]
fre=fobfre[1]
print(fre)"""