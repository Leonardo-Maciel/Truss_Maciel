def keglbrb(comp, els, ang, glb, link):
    # Monta a matriz de rigidez global
    global comp1
    global comp2
    global comp3
    nelm = len(comp[1])
    nglb = max(max(glb))
    #
    #  atencao isto e especifico p/ 3dv apenas!!!
    #  nelm1 =ultimo no. de elemnto coberto pela dv1
    #  nelm2 =ultimo no. de elemnto coberto pela dv2
    #  nelm3 =ultimo no. de elemnto coberto pela dv3= nelm (no. de elementos totais)
    k1 = csr_matrix(nglb, nglb)
    k2 = csr_matrix(nglb, nglb)
    k3 = csr_matrix(nglb, nglb)
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
    aa = np.ones(nelm)
    comp1 = 0.0
    comp2 = 0.0
    comp3 = 0.0

    for i in range(nelm):
        ke = keltr(aa[i], comp[i], els[i], ang[i])
        id = np.flatnonzero(glb[:][i])
        gb = glb[id][i]

        if link[i][0] == 0:
            k1[gb][gb] = k1[gb][gb] + ke[id][id]
            comp1 = comp1 + comp[i]

        if link[i][0] == 1:
            k2[gb][gb] = k2[gb][gb] + ke[id][id]
            comp2 = comp2 + comp[i]

        if link[i][0] == 2:
            k3[gb][gb] = k3[gb][gb] + ke[id][id]
            comp3 = comp3 + comp[i]
    return k1,k2,k3
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
