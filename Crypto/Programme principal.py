from tkinter import *
from tkinter import ttk
from random import *
from os import chdir
chdir(r"C:\Users\Clement\Desktop\Jeu de cartes") ## A modifier en remplaçant par l'addresse du dossier où vos images sont enregistrées

color="\x1B["

from decalage_coder import *
from decalage_cesar import *
from codage_affine import *
from codage_par_transposition import *
from monge1 import *
from monge2 import *
from lapileequitable import *
from pileequitableXn import *
from faro1 import *
from faro2 import *

fen=0
Saisie=0
Bouton=0
L=0
Phrase=0
Nombres=[1,3,5,7,9,11,15,17,19,21,23,25]


def Acquis():
    global L, Saisie, Bouton, Phrase,fen,mode
    L=str(Saisie.get())


    K=len(L)

    for k in range(K):
        if not(L[k].lower() in text):
            print("Erreur : merci de ne pas utiliser de ponctuation ni de caractères spéciaux (" +color+"31m"+str(L[k])+color+"0m"+").")
            texte=Label(text=L)
            texte.pack()
            Quitter=Button(text="Quitter",command=fen.destroy)
            Quitter.pack()
            return
    MotsEnCartes()

def Transfo():
    global L, Saisie, Bouton, Phrase,fen,mode
    K=len(L)
    if K>10:
        Lg=10
    else:
        Lg=K
    can = Canvas(fen, width = Lg*71 , height = (((K)//10)+1)*97, bg='black')
    can.grid(row=0,column=0)
    Lr=-71
    Ht=0
    Images_Affiches=[]
    for k in range(K):
        Lr+=71
        if k%10==0 and k>5:
            Lr=0
        if k%10==0 and k>5:
            Ht+=97
        Image_Affichee = can.create_image(Lr,Ht, image = images[text.index(L[k].lower())], anchor='nw')
        Images_Affiches.append(Image_Affichee)

def Dec():
    global Choix,Saisie,Valider,L,fen
    Delete()
    Choix=Label(text="Choisir le décalage :")
    Choix.grid(row=0,column=0)
    Saisie=Entry()
    Saisie.grid(row=1,column=0)
    Valider=Button(text="Valider",command=GetDec)
    Valider.grid(row=2,column=0)

def GetDec():
    global Choix,Saisie,Valider,L,fen
    d=int(Saisie.get())
    Choix.destroy()
    Saisie.destroy()
    Valider.destroy()
    L=decalage(L,d)
    Transfo()

def Ces():
    global L,fen
    Delete()
    L=decalagecesar(L,3)
    Transfo()

def Aff():
    global Choix,Saisie,Valider,L,fen
    Delete()
    Choix=Label(text="Choisir le nombre A impaire différent de 13 : (choix alétoire si nombre incorrect)")
    Choix.grid(row=0,column=0)
    Saisie=Entry()
    Saisie.grid(row=1,column=0)
    Valider=Button(text="Valider",command=Aff2)
    Valider.grid(row=2,column=0)

def Aff2():
    global Choix,Saisie,Valider,L,NbA,fen
    NbA=int(Saisie.get())
    if not(NbA in Nombres):
        NbA=Nombres[randint(0,11)]
    Choix.destroy()
    Saisie.destroy()
    Valider.destroy()

    Choix=Label(text="Choisir le nombre B :")
    Choix.grid(row=0,column=0)
    Saisie=Entry()
    Saisie.grid(row=1,column=0)
    Valider=Button(text="Valider",command=GetAff)
    Valider.grid(row=2,column=0)

def GetAff():
    global Choix,Saisie,Valider,L,NbA,fen
    NbB=int(Saisie.get())
    Choix.destroy()
    Saisie.destroy()
    Valider.destroy()
    L=affine(L,NbA ,NbB)
    Transfo()

def Trans():
    global Choix,Saisie,Valider,L,fen
    Delete()
    Choix=Label(text="Voulez-vous faire vous même la table de codage? taper 1 pour oui. taper 2 pour non.")
    Choix.grid(row=0,column=0)
    Saisie=Entry()
    Saisie.grid(row=1,column=0)
    Valider=Button(text="Valider",command=GetTrans)
    Valider.grid(row=2,column=0)

def GetTrans():
    global Choix,Saisie,Valider,L,fen
    n=int(Saisie.get())
    Choix.destroy()
    Saisie.destroy()
    Valider.destroy()
    L=decalagetable(L,n)
    Transfo()

def NoNe():
    global Choix,Saisie,Valider,L,fen
    Delete()
    Transfo()

def Mon1():
    global L,fen
    Delete()
    L=monge1(L)
    Transfo()

def Mon2():
    global L,fen
    Delete()
    L=monge2(L)
    Transfo()

def Pequi():
    global L,fen
    Delete()
    L=lapileequitable(L)
    Transfo()

def PequiXn():
    global Choix,Saisie,Valider,L,fen
    Delete()
    Choix=Label(text="Choisir le numéro :")
    Choix.grid(row=0,column=0)
    Saisie=Entry()
    Saisie.grid(row=1,column=0)
    Valider=Button(text="Valider",command=GetPequiXn)
    Valider.grid(row=2,column=0)

def GetPequiXn():
    global Choix,Saisie,Valider,L,fen
    n=int(Saisie.get())
    Choix.destroy()
    Saisie.destroy()
    Valider.destroy()
    L=lapileecitableXn(L,n)
    Transfo()

def Faro1():
    global Choix,Saisie,Valider,L,fen
    Delete()
    Choix=Label(text="Choisir le nombre de fois ou vous voulez faire le mélange :")
    Choix.grid(row=0,column=0)
    Saisie=Entry()
    Saisie.grid(row=1,column=0)
    Valider=Button(text="Valider",command=GetFaro1)
    Valider.grid(row=2,column=0)

def GetFaro1():
    global Choix,Saisie,Valider,L,fen
    n=int(Saisie.get())
    Choix.destroy()
    Saisie.destroy()
    Valider.destroy()
    L=faro1(L,n)
    Transfo()

def Faro2():
    global Choix,Saisie,Valider,L,fen
    Delete()
    Choix=Label(text="Choisir le nombre de fois ou vous voulez faire le mélange :")
    Choix.grid(row=0,column=0)
    Saisie=Entry()
    Saisie.grid(row=1,column=0)
    Valider=Button(text="Valider",command=GetFaro2)
    Valider.grid(row=2,column=0)

def GetFaro2():
    global Choix,Saisie,Valider,L,fen
    n=int(Saisie.get())
    Choix.destroy()
    Saisie.destroy()
    Valider.destroy()
    L=faro2(L,n)
    Transfo()


def MotsEnCartes():
    global L,Saisie,Bouton,Phrase,fen,Choix,ChoixDec,ChoixCes,ChoixAff,ChoixTrans,ChoixAucun,ChoixMon1,ChoixMon2,ChoixPequi,ChoixPequiXn,ChoixFaro1,ChoixFaro2

    Saisie.destroy()
    Bouton.destroy()
    Phrase.destroy()


    Choix=Label(text="Choissisez la méthode de cryptage")
    Choix.grid(row=0,column=0,columnspan=2)
    ChoixDec=Button(text="Décalage",command=Dec)
    ChoixDec.grid(row=1,column=0)
    ChoixCes=Button(text="César",command=Ces)
    ChoixCes.grid(row=1,column=1)
    ChoixAff=Button(text="Affine",command=Aff)
    ChoixAff.grid(row=2,column=0)
    ChoixTrans=Button(text="Transposition",command=Trans)
    ChoixTrans.grid(row=2,column=1)
    ChoixAucun=Button(text="Aucun cryptage",command=NoNe)
    ChoixAucun.grid(row=6,column=0,columnspan=2)
    ChoixMon1=Button(text="Monge1",command=Mon1)
    ChoixMon1.grid(row=3,column=0)
    ChoixMon2=Button(text="Monge2",command=Mon2)
    ChoixMon2.grid(row=3,column=1)
    ChoixPequi=Button(text='Pile equitable',command=Pequi)
    ChoixPequi.grid(row=4,column=0)
    ChoixPequiXn=Button(text="Pile equitable Xn",command=PequiXn)
    ChoixPequiXn.grid(row=4,column=1)
    ChoixFaro1=Button(text="Faro1",command=Faro1)
    ChoixFaro1.grid(row=5,column=0)
    ChoixFaro2=Button(text="Faro2",command=Faro2)
    ChoixFaro2.grid(row=5,column=1)


def MotsEnCartes2():
    global L,Saisie,Bouton,Phrase,fen,mode,Choix,ChoixDec,ChoixCes,ChoixAff,ChoixTrans,ChoixMon1,ChoixMon2,ChoixPequi,ChoixPequiXn,ChoixFaro1,ChoixFaro2

    defin()

    Phrase=Label(fen,text="Entrez la phrase :")
    Phrase.grid(row=0,column=0)
    Saisie=Entry(fen)
    Saisie.grid(row=1,column=0)
    Bouton=Button(fen,text="Entrée",command=Acquis)
    Bouton.grid(row=2,column=0)
    #ouverture fenetre
    fen.mainloop()

def Delete():
    global L,Saisie,Bouton,Phrase,fen,mode,Choix,ChoixDec,ChoixCes,ChoixAff,ChoixTrans,ChoixAucun,ChoixMon1,ChoixMon2,ChoixPequi,ChoixPequiXn,ChoixFaro1,ChoixFaro2
    Choix.destroy()
    ChoixDec.destroy()
    ChoixCes.destroy()
    ChoixAff.destroy()
    ChoixTrans.destroy()
    ChoixAucun.destroy()
    ChoixMon1.destroy()
    ChoixMon2.destroy()
    ChoixPequi.destroy()
    ChoixPequiXn.destroy()
    ChoixFaro1.destroy()
    ChoixFaro2.destroy()

def defin():
    global images,text,fen
    #Page principale
    fen = Tk()
    fen.title('Jeu de 52 cartes')

    fen.option_add('*tearOff', FALSE)

    Objet_Image0 = PhotoImage(file='c1.gif',master=fen)
    Objet_Image1 = PhotoImage(file='c2.gif',master=fen)
    Objet_Image2 = PhotoImage(file='c3.gif',master=fen)
    Objet_Image3 = PhotoImage(file='c4.gif',master=fen)
    Objet_Image4 = PhotoImage(file='c5.gif',master=fen)
    Objet_Image5 = PhotoImage(file='c6.gif',master=fen)
    Objet_Image6 = PhotoImage(file='c7.gif',master=fen)
    Objet_Image7 = PhotoImage(file='c8.gif',master=fen)
    Objet_Image8 = PhotoImage(file='c9.gif',master=fen)
    Objet_Image9 = PhotoImage(file='c10.gif',master=fen)
    Objet_Image10 = PhotoImage(file='cj.gif',master=fen)
    Objet_Image11 = PhotoImage(file='cq.gif',master=fen)
    Objet_Image12 = PhotoImage(file='ck.gif',master=fen)

    Objet_Image13 = PhotoImage(file='d1.gif',master=fen)
    Objet_Image14 = PhotoImage(file='d2.gif',master=fen)
    Objet_Image15 = PhotoImage(file='d3.gif',master=fen)
    Objet_Image16 = PhotoImage(file='d4.gif',master=fen)
    Objet_Image17 = PhotoImage(file='d5.gif',master=fen)
    Objet_Image18 = PhotoImage(file='d6.gif',master=fen)
    Objet_Image19 = PhotoImage(file='d7.gif',master=fen)
    Objet_Image20 = PhotoImage(file='d8.gif',master=fen)
    Objet_Image21 = PhotoImage(file='d9.gif',master=fen)
    Objet_Image22 = PhotoImage(file='d10.gif',master=fen)
    Objet_Image23 = PhotoImage(file='dj.gif',master=fen)
    Objet_Image24 = PhotoImage(file='dq.gif',master=fen)
    Objet_Image25 = PhotoImage(file='dk.gif',master=fen)

    Objet_Image26 = PhotoImage(file='s1.gif',master=fen)
    Objet_Image27 = PhotoImage(file='s2.gif',master=fen)
    Objet_Image28 = PhotoImage(file='s3.gif',master=fen)
    Objet_Image29 = PhotoImage(file='s4.gif',master=fen)
    Objet_Image30 = PhotoImage(file='s5.gif',master=fen)
    Objet_Image31 = PhotoImage(file='s6.gif',master=fen)
    Objet_Image32 = PhotoImage(file='s7.gif',master=fen)
    Objet_Image33 = PhotoImage(file='s8.gif',master=fen)
    Objet_Image34 = PhotoImage(file='s9.gif',master=fen)
    Objet_Image35 = PhotoImage(file='s10.gif',master=fen)
    Objet_Image36 = PhotoImage(file='sj.gif',master=fen)
    Objet_Image37 = PhotoImage(file='sq.gif',master=fen)
    Objet_Image38 = PhotoImage(file='sk.gif',master=fen)

    Objet_Image39 = PhotoImage(file='h1.gif',master=fen)
    Objet_Image40 = PhotoImage(file='h2.gif',master=fen)
    Objet_Image41 = PhotoImage(file='h3.gif',master=fen)
    Objet_Image42 = PhotoImage(file='h4.gif',master=fen)
    Objet_Image43 = PhotoImage(file='h5.gif',master=fen)
    Objet_Image44 = PhotoImage(file='h6.gif',master=fen)
    Objet_Image45 = PhotoImage(file='h7.gif',master=fen)
    Objet_Image46 = PhotoImage(file='h8.gif',master=fen)
    Objet_Image47 = PhotoImage(file='h9.gif',master=fen)
    Objet_Image48 = PhotoImage(file='h10.gif',master=fen)
    Objet_Image49 = PhotoImage(file='hj.gif',master=fen)
    Objet_Image50 = PhotoImage(file='hq.gif',master=fen)
    Objet_Image51 = PhotoImage(file='hk.gif',master=fen)

    text="abcdefghijklmnopqrstuvwxyz 0123456789"
    images=[Objet_Image0,Objet_Image1,Objet_Image2,Objet_Image3,Objet_Image4,Objet_Image5,Objet_Image6,Objet_Image7,Objet_Image8,Objet_Image9,Objet_Image10,Objet_Image11,Objet_Image12,Objet_Image13,Objet_Image14,Objet_Image15,Objet_Image16,Objet_Image17,Objet_Image18,Objet_Image19,Objet_Image20,Objet_Image21,Objet_Image22,Objet_Image23,Objet_Image24,Objet_Image25,Objet_Image26,Objet_Image27,Objet_Image28,Objet_Image29,Objet_Image30,Objet_Image31,Objet_Image32,Objet_Image33,Objet_Image34,Objet_Image35,Objet_Image36,Objet_Image37,Objet_Image38,Objet_Image39,Objet_Image40,Objet_Image41,Objet_Image42,Objet_Image43,Objet_Image44,Objet_Image45,Objet_Image46,Objet_Image47,Objet_Image48,Objet_Image49,Objet_Image50,Objet_Image51]


MotsEnCartes2()
