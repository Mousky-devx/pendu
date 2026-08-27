#c'est le fichier qui assemble le jeu pendu
from donnees import*
from fonctions import*

user=recup_nom_utilisateur()
scores=recup_score()
if user not in scores.keys():
    scores[user] = 0
cont="o"
while cont=="o":
    print("Joueur {0}: {1} point(s)".format(user, scores[user]))
    nb_chances =tent
    mot=choisir_mots()
    nb_chances=verificateur(mot)
    scores[user] += nb_chances  
    cont = input("Souhaitez-vous continuer la partie (O/N) ?")
    cont=cont.lower()
save_score()
print("Vous finissez la partie avec {0} points .Votre score tottal est de :{1}".format(nb_chances,scores[user]))