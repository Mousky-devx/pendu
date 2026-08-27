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
    nb_chances=tent
    print("Il s'agit d'un mot de ", len(mot) ," lettres")
    print("".join(mot_saisie))
    while nb_chances > 0:
        try :
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
            if comp==0:
                print(f"la lettre {choix} entree n'est pas dans le mot")
                nb_chances-=1
            else :
                print("le lettre {0} est bien dans le mots a {1} reprise ".format(choix,comp))
        
        print(" Etat actuel de decouverte du mot: ","".join(mot_saisie) )
        print(f"Il vous reste {nb_chances} essaies")
        if nb_chances == 0:
            print("vous avez perdu")
            print(f"Le mot etait {mot} ")
            break
        if mot_saisie == mot_liste :
            print(f"felicitations vous avez trouve le mot \
                  votre score est de {nb_chances}")
            break
def recup_score():
    if os.path.exists(nom_fichier_score): # Le fichier existe
        fichier_score = open(nom_fichier_score, "rb")
        mon_depickler = pickle.Unpickler(fichier_score)
        scores = mon_depickler.load()
        fichier_score.close()
    else: # Le fichier n’existe pas
        scores = {}
    return scores

def save_score():
    fichier_score = open(nom_fichier_score, "wb")
    mon_pickler = pickle.Pickler(fichier_score)
    mon_pickler.dump(nom_fichier_score)
    fichier_score.close()

def recup_nom_utilisateur():
    nom_utilisateur = input("Tapez votre nom: ")
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("Ce nom est invalide.")
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur
    