#fichier regorgeant les fonctions du jeu pendu
import random
import pickle
import os
from donnees import *

def choisir_mots():
    mot=random.choice(mots_pendu)
    mot=str(mot)
    mot=mot.lower()
    return mot

def verificateur(mot):
    mot_liste=list(mot)
    mot_saisie=["*" for i in range(len(mot))]
    entres=[]
    nb_chances=tent
    print("Il s'agit d'un mot de ", len(mot) ," lettres")
    print("".join(mot_saisie))
    tour=1
    while nb_chances > 0:
        
        try :
            if tour != 1 :
                print("les lettres errone  que vous avez deja essaye sont \n ",entres)
            choix=str(input("entrez votre lettre: "))
            assert len(choix)==1
        except AssertionError :
            choix=str(input("veuliez entre entrer une lettre : "))
            while len(choix)!=1:
                choix=str(input("veuliez entre entrer une lettre : "))
        finally: 
            comp=0
            for i in range(len(mot)):
                a=mot_liste[i]
                if  a == choix:
                    mot_saisie[i]=choix
                    comp+=1
            if comp==0  :
                print(f"la lettre {choix} entree n'est pas dans le mot")
                nb_chances-=1
                entres.append(choix)
                
            
            if comp>=1:
                    print("le lettre {0} est bien dans le mots a {1} reprise ".format(choix,comp))
            if comp==0 and choix in entres and tour !=1:
                    print("Vous avez deja essaye {0} et elle n'est pas dans le mot".format(choix))
        print(" Etat actuel de decouverte du mot: ","".join(mot_saisie) )
        print(f"Il vous reste {nb_chances} essaies")
        tour +=1
        if nb_chances == 0:
            print("vous avez perdu")
            print(f"Le mot etait {mot} ")
            return 0
            break
        if mot_saisie == mot_liste :
            print(f"felicitations vous avez trouve le mot \
                  votre score est de {nb_chances}")
            return nb_chances
            break
def recup_score():
    if os . path . exists ( nom_fichier ) : 
        fichier_scores = open ( nom_fichier , "rb" )
        mon_depickler = pickle.Unpickler ( fichier_scores )
        scores = mon_depickler.load()
        fichier_scores . close ()
    else : 
        scores = {}
    return scores
def save_score(scores):
    fichier_scores = open ( nom_fichier , "wb" ) # On é craseles anciens scores
    mon_pickler = pickle.Pickler ( fichier_scores )
    mon_pickler.dump( scores )
    fichier_scores.close ()
    
def recup_nom_utilisateur ():
    nom_utilisateur = str(input("Tapez votre nom: "))
    nom_utilisateur=nom_utilisateur.capitalize()
    return nom_utilisateur

    
