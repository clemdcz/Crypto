def monge1(mot):
    """// ---------------- DEBUT EN TETE --------------------------------------//
// NOM :                    codage monge1                        //
//                                                                      //
// AUTEURS : E.chassagne B.balos C.da cruz E.bertrand                   //
//                                                                      //
// VERSION :    2.1                                  novembre 2020     // 
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :                                                            //
//    cap      texte en clair a codé                                    //                                                                      //                                                 //
// SORTIES :                                                            //
//    texte    le texte codé par monge1                         //                                                                      //                                                                      //
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
    else: 
        for i in range (0, moitier):
            ordre.append(chifre)
            chifre = chifre -2
        for g in range (1, longeur+1, 2):
                ordre.append(g)            
    for k in range (0, longeur):
        numero = ordre[k] -1
        motcode.append(motclaire[numero])
    textecode = "".join(motcode)
    return textecode

