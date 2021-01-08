def keltr(area,ls,els,teta):
    ke = np.zeros((4, 4))
    s = sin(teta)
    c = cos(teta)
    kl = area * els / ls
    ke[0][0] = kl * c * c
    ke[0][1] = kl * c * s
    ke[0][2] = -kl * c * c
    ke[0][3] = -kl * c * s

    ke[1][0] = kl * c * s
    ke[1][1] = kl * s * s
    ke[1][2] = -kl * s * c
    ke[1][3] = -kl * s * s

    ke[2][0] = -kl * c * c
    ke[2][1] = -kl * c * s
    ke[2][2] = kl * c * c
    ke[2][3] = kl * c * s

    ke[3][0] = -kl * c * s
    ke[3][1] = -kl * s * s
    ke[3][2] = kl * s * c
    ke[3][3] = kl * s * s