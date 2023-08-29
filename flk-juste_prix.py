from flask import Flask, render_template, request
import random

app = Flask(__name__)
i = None
cible = None
pseudo = None


@app.route('/')
def debut():
    global i, cible
    i = 1
    # Tirage d'un prix (entier) au hasard entre 1 et 10
    cible = random.randint(1, 10)
    return render_template('debut.html')


# Recuperation du pseudo
@app.route('/bienvenue')
def bienvenue():
    global pseudo
    pseudo = request.values['pseudo']
    return render_template('bienvenue.html', pseudo=pseudo)


# Essai d'un prix
@app.route('/essai')
def essai():
    return render_template('essai.html', i=str(i), pseudo=pseudo)


@app.route('/verif')
def verif():

    try:
        essai = int(request.values['essai'])
    except:
        return render_template('verif.html', msg="Valeur incorrecte...",
                                action = "/essai", bouton = "Recommencez")

    # +1 pour le prochain tour...
    global i
    i += 1

    # Message "BRAVO" si le prix est trouvé
    if (cible == essai):
        return render_template('verif.html', msg="BRAVO !!!",
                               action="/", bouton="Nouvelle partie")
    # Message "PERDU..." au bout de 5 essais
    elif i > 5:
        return render_template('verif.html', msg="PERDU...",
                               action="/", bouton="Nouvelle partie")
    # Message "PAS ASSEZ" si le prix est trop bas
    elif (cible > essai):
        return render_template('verif.html', msg="PAS ASSEZ...",
                               action="/essai", bouton="Nouvel essai")
    # Message "TROP ELEVE" si le prix est trop haut
    else:
        return render_template('verif.html', msg="TROP ELEVE...",
                               action="/essai", bouton="Nouvel essai")


app.run(host="0.0.0.0")
