# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:43:16 2020

@author: erwann bora clement elliot
"""

def decalagetable (texte, n):
    """// ---------------- DEBUT EN TETE --------------------------------------//
// NOM :                    codage transposition                        //
//                                                                      //
// AUTEURS : E.chassagne B.balos C.da cruz E.bertrand                   //
//                                                                      //
// VERSION :    1.1                                  septembre 2020     //
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :                                                            //
//    cap      texte en clair à coder                                    //                                                                      //                                                 //
// SORTIES :                                                            //
//    texte    le texte codé par transposition                          //                                                                      //                                                                      //
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
    texte = texte.lower()
    alphabetcod=['o','r','n','i','t','h','y','q','u','e','a','b','c','d','f','g',' ','k','l','m','p','s','v','w','x','z','j']
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    if n == 1:
        alphabetcod[0] = input("entrez la lettre ou espace qui remplacera a")
        alphabetcod[1] = input("entrez la lettre ou espace qui remplacera b")
        alphabetcod[2] = input("entrez la lettre ou espace qui remplacera c")
        alphabetcod[3] = input("entrez la lettre ou espace qui remplacera d")
        alphabetcod[4] = input("entrez la lettre ou espace qui remplacera e")
        alphabetcod[5] = input("entrez la lettre ou espace qui remplacera f")
        alphabetcod[6] = input("entrez la lettre ou espace qui remplacera g")
        alphabetcod[7] = input("entrez la lettre ou espace qui remplacera h")
        alphabetcod[8] = input("entrez la lettre ou espace qui remplacera i")
        alphabetcod[9] = input("entrez la lettre ou espace qui remplacera j")
        alphabetcod[10] = input("entrez la lettre ou espace qui remplacera k")
        alphabetcod[11] = input("entrez la lettre ou espace qui remplacera l")
        alphabetcod[12] = input("entrez la lettre ou espace qui remplacera m")
        alphabetcod[13] = input("entrez la lettre ou espace qui remplacera n")
        alphabetcod[14] = input("entrez la lettre ou espace qui remplacera o")
        alphabetcod[15] = input("entrez la lettre ou espace qui remplacera p")
        alphabetcod[16] = input("entrez la lettre ou espace qui remplacera q")
        alphabetcod[17] = input("entrez la lettre ou espace qui remplacera r")
        alphabetcod[18] = input("entrez la lettre ou espace qui remplacera s")
        alphabetcod[19] = input("entrez la lettre ou espace qui remplacera t")
        alphabetcod[20] = input("entrez la lettre ou espace qui remplacera u")
        alphabetcod[21] = input("entrez la lettre ou espace qui remplacera v")
        alphabetcod[22] = input("entrez la lettre ou espace qui remplacera w")
        alphabetcod[23] = input("entrez la lettre ou espace qui remplacera x")
        alphabetcod[24] = input("entrez la lettre ou espace qui remplacera y")
        alphabetcod[25] = input("entrez la lettre ou espace qui remplacera z")
        alphabetcod[26] = input("entrez la lettre ou espace qui remplacera espace")
    texteclaire = list(texte)
    for i in range(0,len(texte)):
        lettre = int(alphabet.index(texteclaire[i]))
        texteclaire[i] = alphabetcod[lettre]
        texte ="".join(texteclaire)
        texte = texte.upper()
    return texte


