import numpy as np
from optdat10 import optdat10
from matplotlib import pyplot as plt
from createtruss10 import createtruss10
"""preciso chamar as funcoes para fazer funcionarem"""
class plottruss():

    def __init__(self, x, y, conect,plot='no'):
        self.x = x
        self.y = y
        self.connect = conect
        self.point = []
        self.x1 = []
        self.y1 = []
        #verificar dps se posso fazer melhor esse zip
        if plot == 'yes':
            for xi, yi in zip(self.x, self.y):
                self.point.append([xi, yi])
                plt.scatter(xi, yi, color='grey')
            for i in range(len(self.connect)):
                self.x1.append(self.point[self.connect[i][0]][0])
                self.x1.append(self.point[self.connect[i][1]][0])
                self.y1.append(self.point[self.connect[i][0]][1])
                self.y1.append(self.point[self.connect[i][1]][1])
            plt.plot(self.x1, self.y1)
            plt.show()

class Opt():
    """Otimização via PSO"""

    def __init__(self):
        # Entradas:

        # global lpdva
        # global para
        # global props
        # global con
        # global penal
        # global kns
        # global idan

        self.idan = 1
        # 1 --- FEM(método dos elementos finitos)
        # 2 --- RBM

        self.iflag = 2
        # 1 --- Análise estrutural
        # 2 --- Otimização

        createtruss10()

        #self.trussfe() salvava variáveis do createtruss em um arquivo .mat
        # Execute a opção desejada:
        #		2---OTIMIZAÇÃO
        #penal = 10 ^ 8; JA TEM LA EM CIMA
        self.ndvab = max(max(link))

        dadosoptdat10 = optdat10(area, lpdva, ndvab, nglb)#
        tpobj = dadosoptdat10[0]
        tpres = dadosoptdat10[1]
        vlb =dadosoptdat10[2]
        vub =dadosoptdat10[3]
        x0 =dadosoptdat10[4]
        clb =dadosoptdat10[5]
        cub =dadosoptdat10[6]

        fobfre = optsolpso(props, fext, glb, link, tpobj, tpres, area)
        fob = fobfre[0]
        fre = fobfre[1]
        #*********
        para = [ndvab, tpobj, tpres, f0]
        con = [clb, cub]
        #*********
        np = 20  # número de partículas20
        dim = para[0]  # número de dimensões das partículas
        maxiter = 500  # número de iterações máximas10000


        vmin = -0.5 * (vub - vlb)  # limites para as mudanças locais
        vmax = 0.5 * (vub - vlb)

        wp = 3.0  # parâmetros de c1
        ws = 4 - wp  # confiança c2
        Zb = inf(np, 1)  # forma inicial

        pnextvel = inicia(dim, np, vlb, vub)  # inicialização das partículas
        pnext = pnextvel[0]
        vel = pnextvel[1]

        cvg = 0
        cont = 0
        cond = 0
        wn = 1.4
        xb = np.zeros((np, dim))
        mZb = np.zeros((0.25 * maxiter, dim + 1))
        mp = np.zeros((0.1 * maxiter, dim + 1, np))
        Zbsf = 0
        t = np.zeros((np, 1))
        fit = np.zeros((1, np))

        while cont < maxiter:  # início do loop
            cont = cont + 1
            p = pnext  # atualização das partículas
            for i in range(np):
                ft = funpso(p[i][:], fext, glb, link)
                f=ft[0]
                t0=ft[1]
                fit[i] = f
                t[i] = t0

            Zbxbt = selectZb(Zb, fit, xb, t, p, np)   # teste para ver a melhor forma
            Zb = Zbxbt[0]
            xb = Zbxbt[1]
            t = Zbxbt[2]

            mZbposZb = tZbest(Zb, xb, mZb, cont, maxiter)  # seleção da melhor aptidão no enxame
            mZb = mZbposZb[0]
            posZb = mZbposZb[1]

            mpposp = memoria(fit, p, cont, mp, maxiter, np)  # histórico das iterações
            mp = mpposp[0]
            posp = mpposp[1]

            if cont%3 == 0:     ###############
                w = ajuste(mp(posp, end,:), np, wn)  # atualização da inércia
                wn = w

            if cont > 0.1 * maxiter & & (rem(cont, 50) == 0):
                [cvg, cond] = tconv(Zb, mp, posp, mZb, posZb, cont, cond, maxiter, np)  # teste de
                # convergência

            if cvg ~= 0:
                break

            for i in np:
                del = atualiza(xb(i,:), mZb(posZb, (2:end)), wn, wp, ws, p(i,:), vel(i,:), t(i))  #
                velnext = constrict(vmax, vmin,del);  # atualização da
                vel(i,:) = velnext  # velocidade
                del = p(i,:) + vel(i,:)  #
                pnt = constrict(vub, vlb,del)
                pnext(i,:) = pnt

            #wp = 0.5 + (3 / maxiter) * cont
            #             ws = 4 - wp;
        tempo = toc

        xstr = mZb(posZb, 2:end)  # posição do ótimo
        ang = props(1,:)
        comp = props(2,:)
        els = props(3,:)
        [u, sig, esf, vol] = fesol(xstr(link(:, 1)), ang, comp, els, fext, glb)
        en = fext'*u;

        fstr = mZb(posZb, 1)# valor ótimo
        print(fstr)
