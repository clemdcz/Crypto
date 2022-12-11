def lapileecitableXn(mot,n):
    motcliare = list(mot)
    motint =motcliare
    longeur = len(motcliare)
    moitier = int(longeur/2)
    ordre = []
    motcodeint=[]
    motcode = []
    for j in range(0, n):
        for i in range(longeur-1, 0, -2):
            ordre.append(i)
        for o in range(longeur, 0, -2):
            ordre.append(o)
        if longeur%2 ==0:
            for k in range (0, moitier):
                numero = ordre[k] -1
                motcodeint.append(motint[numero])
        else: 
            for k in range (0, moitier):
                numero = ordre[k] -1
                motcodeint.append(motint[numero])
        motcodeint.reverse()
        motcode = motcode + motcodeint
        motcodeint=[]
        motcliare = motint
        motint = []
        if longeur%2 == 0:
            for k in range (moitier, longeur):
                numero = ordre[k] -1
                motint.append(motcliare[numero])
        else:
            for k in range (moitier, longeur):
                numero = ordre[k] -1
                motint.append(motcliare[numero])
        if j+1 == n: 
            motcode.reverse()
            motcode = motint + motcode 
            motcode.reverse()
        longeur = len(motint)
        ordre = []
        moitier = int(longeur/2)
    motcode.reverse()
    textecode = "".join(motcode)
    return textecode

