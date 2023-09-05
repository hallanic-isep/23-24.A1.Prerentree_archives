from flask import Flask, render_template, request, session
import random
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
print(app.secret_key)

# Liste vide
#joueurs = []
# Ensemble vide
#joueurs = set()
# Dictionaire vide
joueurs = {}

@app.route('/')
def debut():
    session['i'] = 1
    # Tirage d'un prix (entier) au hasard entre 1 et 10
    session['cible'] = random.randint(1, 10)
    return render_template('debut.html')


# Recuperation du pseudo
@app.route('/bienvenue')
def bienvenue():
    session['pseudo'] = request.values['pseudo']

    # Mise à jour du conteneur
    #joueurs.append(request.values['pseudo'])
    #joueurs.add(request.values['pseudo'])
    if request.values['pseudo'] in joueurs:
        joueurs[ request.values['pseudo'] ] += 1
    else:
        joueurs[request.values['pseudo']] = 1

    return render_template('bienvenue.html',
                           pseudo=session['pseudo'])


# Essai d'un prix
@app.route('/essai')
def essai():
    return render_template('essai.html',
                           i=str(session['i']), pseudo=session['pseudo'])


@app.route('/verif')
def verif():

    try:
        essai = int(request.values['essai'])
    except:
        return render_template('verif.html', msg="Valeur incorrecte...",
                                action = "/essai", bouton = "Recommencez")

    # +1 pour le prochain tour...
    session['i'] += 1

    # Message "BRAVO" si le prix est trouvé
    if (session['cible'] == essai):
        return render_template('verif.html', msg="BRAVO !!!",
                               action="/", bouton="Nouvelle partie")
    # Message "PERDU..." au bout de 5 essais
    elif session['i'] > 5:
        return render_template('verif.html', msg="PERDU...",
                               action="/", bouton="Nouvelle partie")
    # Message "PAS ASSEZ" si le prix est trop bas
    elif (session['cible'] > essai):
        return render_template('verif.html', msg="PAS ASSEZ...",
                               action="/essai", bouton="Nouvel essai")
    # Message "TROP ELEVE" si le prix est trop haut
    else:
        return render_template('verif.html', msg="TROP ELEVE...",
                               action="/essai", bouton="Nouvel essai")

@app.route("/joueurs")
def aff_joueurs():
    page = str(joueurs)

    for elem in joueurs:
        page += f"<br>\n{ elem } : { joueurs[elem] }"

    return page

app.run(host="0.0.0.0")
