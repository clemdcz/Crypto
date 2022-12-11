def lapileequitable(mot):
    """// ---------------- DEBUT EN TETE --------------------------------------//
// NOM :                    codage pile equitable                       //
//                                                                      //
// AUTEURS : E.chassagne B.balos C.da cruz E.bertrand                   //
//                                                                      //
// VERSION :    1.4                                  novembre 2020      // 
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :                                                            //
//    cap      texte en clair à coder                                    //                                                                      //                                                 //
// SORTIES :                                                            //
//    texte    le texte codé avec la methode pile equitable             //                                                                      //                                                                      //
// MODIFIEES :                                                          //
//                                                                      //
// LOCALES :                                                            //
//             alphabet,                                                //
//                                                                      //
// FONCTIONS APPELEES :                                                 //
//                                                                      //
// ALGO - REFERENCES :                                                  //
//                                                                      //
// ---------------- FIN EN TETE ----------------------------------------//

    """
    motclaire = list(mot)
    longeur = len(motclaire)
    ordre = []
    motcode = []
    for i in range(longeur-1, 0, -2):
        ordre.append(i)
    for n in range(longeur, 0, -2):
        ordre.append(n)
    for k in range (0, longeur):
        numero = ordre[k] -1
        motcode.append(motclaire[numero])
    textecode = "".join(motcode)
    return textecode

