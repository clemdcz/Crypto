# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:17:35 2020

@author: erwann bora clement elliot
"""






def decalage (texte, dec):
    """// ---------------- DEBUT EN TETE --------------------------------------//
// NOM :                    codage decalage                             //
//                                                                      //
// AUTEURS : E.chassagne B.balos C.da cruz E.bertrand                   //
//                                                                      //
// VERSION :    1.1                                  septembre 2020     //
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :                                                            //
//    cap      texte en clair à coder                                    //                                                                      //                                                 //
// SORTIES :                                                            //
//    texte    le texte codé avec la décalage                           //                                                                      //                                                                      //
// MODIFIEES :                                                          //
//                                                                      //
// LOCALES :                                                            //
//             alphabet et la valeur du décalage                        //
//                                                                      //
// FONCTIONS APPELEES :                                                 //
//                                                                      //
// ALGO - REFERENCES :                                                  //
//                                                                      //
// ---------------- FIN EN TETE ----------------------------------------//

    """
    texte = texte.lower()
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    texteclaire = list(texte)
    for i in range(0,len(texte)):
        lettre = int(alphabet.index(texteclaire[i]))
        if lettre+dec <= 26:
            texteclaire[i] = alphabet[lettre+ dec]
        else:
            texteclaire[i] = alphabet[lettre+dec-26]
        texte ="".join(texteclaire)
        texte = texte.upper()
    return texte



