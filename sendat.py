def sendat(self):
  "Fornece dados para a análise de sensibilidades"

#	> Entra com no. de variáveis de projeto --- ndvab
#	> relacao entre as variáveis primárias e secundárias:
#							---	link(iel,1)= no. da variável primária a qual iel está associada
#							---	link(iel,2)=  fator de escala entre elas.
#   > nome do elemento o qual as variáveis primárias estão associadas ---lpdva
#   > valor da perturbação a ser aplicada --- perturb
#
#

    self.ndvab = 3#nmudei
    #        1   2   3   4   5   6   7   8   9   10
    self.link = [[0, 0][1, 0][1, 0][1, 0][2, 0][2, 0][1, 0][2, 0][0, 0][2, 0]] #mudei
    self.lpdva = [1, 3, 2]
    self.perturb = 10**-6