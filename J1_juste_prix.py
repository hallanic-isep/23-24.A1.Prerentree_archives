# Tirage d'un prix (entier) au hasard entre 1 et 10
import random


def verif(cible,essai):
    # Message "BRAVO" si le prix est trouvé
    if (cible == essai):
        print("BRAVO !!!")

        # Fin au bout de 5 esssais ou si le prix est trouvé
        return True

    # Message "PAS ASSEZ" si le prix est trop bas
    elif (cible > essai):
        print("PAS ASSEZ...")
    # Message "TROP ELEVE" si le prix est trop haut
    else:
        print("TROP ELEVE...")

    return False

# Empêche d'exécuter la suite en cas d' "import" de "juste_prix"
# ... comme dans le cas du lancement d'un test unitaire depuis PyCharm
if __name__ == '__main__':

    # Coeur du jeu

    cible = random.randint(1,10)

    # 5 essais...
    for i in range(5):

        # Essai d'un prix
        try:
            essai = int(input(f"essai {i+1} : "))
        except:
            print("Valeur incorrecte...")
            essai = 0 # pour éviter l'erreur si aucune saisie est valide...
            continue

        if verif(cible, essai):
            break

    # Message "PERDU" au bout de 5 essais
    if (cible != essai):
        print("PERDU...")

    print("FIN...")