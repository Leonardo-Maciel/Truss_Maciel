"""Realiza a Optimizacao da estrutura"""
import numpy as np
from scipy import sparse
from createtruss10 import createtruss10
from math import sin, cos
class optsolpso():
    def __init__(self,props, fext, glb, link, tpobj, tpres, x):
        #
        # Fornece valores para as funcões objetivo e restrição e
        #
        #        atualiza todas as variáveis primárias
        #
        ang = props[1][:]
        comp = props[2][:]
        els = props[3][:]

        area = self.getval(comp, x, link)
        #
        # Faz a solução via o MEF para avaliação das funções.
        #
        self.fesol(area, ang, comp, els, fext, glb)
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
        f=[fob, fre]

        return f

    def getval(self,comp,xvalu,link):
        #
        #  atualiza as variáveis
        #
        #
        # dimensoes:
        #
        m = len(comp)
        nelem = len(comp[0])
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

        self.m = len(comp)
        self.nelm = len(comp[0])
        nglb = max(max(glb))
        kgb = sparse.csr_matrix(nglb, nglb)

        for i in range(self.nelm):
            ke = createtruss10.keltr(self,area[i], comp[i], els[i], ang[i])
            id = np.flatnonzero(glb[:][i])
            gb = glb[id][i]
            kgb[gb][gb] = kgb[gb][gb] + ke[id][id]

        return kgb

    def tresf(self,area, comp, els, ang, glb, u):

        esf = np.zeros(self.nelm)

        for i in range(self.nelm):

            ae = [-cos(ang[i]), -sin(ang[i]), cos(ang[i]), sin(ang[i])]
            id = np.flatnonzero(glb[:][i])
            gb = glb[id][i]
            uo = u[gb]
            en = ae[id] * uo
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
        vol = 0.0
        for ielem in range(self.nelem):
            vol = vol + area[ielem] * comp[ielem]

        return vol