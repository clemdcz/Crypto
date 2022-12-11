def faro1 (texteor, nombre):
    """// ---------------- DEBUT EN TETE --------------------------------------//
// NOM :                    codage faro1                                //
//                                                                      //
// AUTEURS : E.chassagne B.balos C.da cruz E.bertrand                   //
//                                                                      //
// VERSION :    1.6                                  septembre 2020     // 
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :                                                            //
//    cap  :   texte en clair à coder                                    //                                                                      //                                                 //
// SORTIES :                                                            //
//    texte    le texte codé avec la méthode de faro1                  //                                                                      //                                                                      //
// MODIFIEES :                                                          //
//                                                                      //
// LOCALES :                                                            //
//             alphabet                     //
//                                                                      //
// FONCTIONS APPELEES :                                                 //
//                                                                      //
// ALGO - REFERENCES :                                                  //
//                                                                      //
// ---------------- FIN EN TETE ----------------------------------------//

    """
    texte = texteor
    texte = texte.lower()
    moite = int(len(texte)/2)
    texteclaire = list(texte)
    groupe1 = texteclaire[0:moite:1]
    groupe2 = texteclaire[moite:len(texte)+1:1] 
    textecode =""
    textefin = ""
    k = 0
    r=0
    if (len(texte) % 2) == 0:
        for n in range(0,nombre):
            for i in range(0,moite):
                texte = groupe1[i] + groupe2[i]
                textecode ="".join(textecode)
                textecode = textecode +texte
                textecode = textecode.upper()
            textecode = textecode.lower()
            texteclaire = list(textecode)
            groupe1 = texteclaire[0:moite:1]
            groupe2 = texteclaire[moite:len(textecode)+1:1]
            if n == nombre-1:
                textefin = textecode
            textecode=""
    else:
        groupe1.append("$")
        moite = int(len(texte)/2) + 1
        for n in range(0,nombre):
            for i in range(0,moite):
                texte = groupe1[i] + groupe2[i]
                textecode ="".join(textecode)
                textecode = textecode +texte
                textecode = textecode.upper()
            textecode = list(textecode)
            textecode.remove("$")
            textecode ="".join(textecode)
            textecode = textecode.lower()
            texteclaire = list(textecode)
            groupe1 = texteclaire[0:moite:1]
            groupe2 = texteclaire[moite:len(textecode)+1:1]
            if n == nombre-1:
                textefin = textecode
            textecode=""
            groupe2.append("$")
    return textefin 


            

            
