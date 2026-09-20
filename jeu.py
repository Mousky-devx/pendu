#c'est le fichier qui assemble le jeu pendu
from donnees import*
from fonctions import*

user=recup_nom_utilisateur()
scores=recup_score()
if user not in scores . keys () :
    scores [user] = 0
else :
    print("vous avez deja {0} points".format(scores.get(user)))
cont="o"
score=0
while cont=="o":
    
    print("Joueur {0}".format(user))
    nb_chances =tent
    mot=choisir_mots()
    score+=verificateur(mot)
    scores [ user ] += score
    cont = input("Souhaitez-vous continuer la partie (O/N) ?")
    cont=cont.lower()
print ( " Vous finissez la partie avec {0} points .cumul ={1}  point " . format ( score ,scores[user]))
save_score(scores)
