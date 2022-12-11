# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:18:55 2020

@author: erwann bora clement elliot
"""
def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)



def affine (texte,A,B):
    """// ---------------- DEBUT EN TETE --------------------------------------//
// NOM :                    codage affine                               //
//                                                                      //
// AUTEURS : E.chassagne B.balos C.da cruz E.bertrand                   //
//                                                                      //
// VERSION :    1.1                                  septembre 2020     //
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :                                                            //
//    cap      texte en clair à coder                                    //                                                                      //                                                 //
// SORTIES :                                                            //
//    texte    le texte codé avec la methode affine                     //                                                                      //                                                                      //
// MODIFIEES :                                                          //
//                                                                      //
// LOCALES :                                                            //
//             alphabet, valeur de A et de B                            //
//                                                                      //
// FONCTIONS APPELEES :                                                 //
//                                                                      //
// ALGO - REFERENCES :                                                  //
//                                                                      //
// ---------------- FIN EN TETE ----------------------------------------//

    """
    texte = texte.lower()
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    texteclaire = list(texte)
    k2 = []
    for j in range(0,len(texteclaire)):
        if ' ' ==  texteclaire[j]:
            k2.append(j)
            texteclaire[j] = "a"
    for i in range(0,len(texteclaire)):
        lettre = int(alphabet.index(texteclaire[i]))
        dec = (A*lettre + B)%26
        texteclaire[i] = alphabet[dec]
    for b in range(0, len(k2)):
        texteclaire[k2[b]] =" "
    texte ="".join(texteclaire)
    texte = texte.upper()
    return texte

