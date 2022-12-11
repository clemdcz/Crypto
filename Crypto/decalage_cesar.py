# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:29:57 2020

@author: erwann bora clement elliot
"""

def decalagecesar (texte, dec):
    """// ---------------- DEBUT EN TETE --------------------------------------//
// NOM :                    codage cesar                                //
//                                                                      //
// AUTEURS : E.chassagne B.balos C.da cruz E.bertrand                   //
//                                                                      //
// VERSION :    1.1                                  septembre 2020     //
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :                                                            //
//    cap  :   texte en clair à coder                                    //                                                                      //                                                 //
// SORTIES :                                                            //
//    texte    le texte codé avec la méthode de césar                   //                                                                      //                                                                      //
// MODIFIEES :                                                          //
//                                                                      //
// LOCALES :                                                            //
//             alphabet et la valeur du decalage (3)                    //
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
        letre = int(alphabet.index(texteclaire[i]))
        if letre+dec <= 26:
            texteclaire[i] = alphabet[letre+ dec]
        else:
            texteclaire[i] = alphabet[letre+dec-26]
        texte ="".join(texteclaire)
        texte = texte.upper()
    return texte


