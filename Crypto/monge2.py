def monge2(mot):
    """// ---------------- DEBUT EN TETE --------------------------------------//
// NOM :                    codage monge2                        //
//                                                                      //
// AUTEURS : E.chassagne B.balos C.da cruz E.bertrand                   //
//                                                                      //
// VERSION :    1.3                                  novembre 2020     // 
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :                                                            //
//    cap      texte en clair à coder                                    //                                                                      //                                                 //
// SORTIES :                                                            //
//    texte    le texte codé par monge2                          //                                                                      //                                                                      //
// MODIFIEES :                                                          //
//                                                                      //
// LOCALES :                                                            //
//             alphabet et remplacement                                 //
//                                                                      //
// FONCTIONS APPELEES :                                                 //
//                                                                      //
// ALGO - REFERENCES :                                                  //
//                                                                      //
// ---------------- FIN EN TETE ----------------------------------------//

    """
    motclaire = list(mot) 
    longeur = len(motclaire)
    ordre= []
    motcode = []
    moitier = int(longeur/2)
    chifre = longeur
    if longeur%2 == 1:
        chifre = chifre -1
        for i in range (0, moitier):
            ordre.append(chifre)
            chifre = chifre -2
        for g in range (1, longeur+1, 2):
                ordre.append(g)
        ordre.reverse
    else: 
        for i in range (0, moitier):
            ordre.append(chifre)
            chifre = chifre -2
        for g in range (1, longeur+1, 2):
                ordre.append(g)
        ordre.reverse
    for k in range (0, longeur):
        numero = ordre[k] -1
        motcode.append(motclaire[numero])
    textecode = "".join(reversed(motcode))
    return textecode


