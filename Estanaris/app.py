from flask import Flask, render_template, request
from python.Player import Player
from python.naissance import creation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/naissance', methods=['GET', 'POST'])
def naissance():
    global player
    player = Player()
    return render_template('naissance.html')

@app.route('/profession', methods=['GET', 'POST'])
def profession():
    global player
    if request.method == 'POST':
        choix = request.form
        creation(player, choix)

        prof = 'Dep'
        strength = getattr(player, 'strength')
        dexterity = getattr(player, 'dexterity')
        constitution = getattr(player, 'constitution')
        intelligence = getattr(player, 'intelligence')
        wisdom = getattr(player, 'wisdom')
        charisma = getattr(player, 'charisma')
        print('-----------------------')
        print('Profession   : ' + prof)
        print('Strength     : ' + str(strength))
        print('Dexterity    : ' + str(dexterity))
        print('Constitution : ' + str(constitution))
        print('Intelligence : ' + str(intelligence))
        print('Wisdom       : ' + str(wisdom))
        print('Charisma     : ' + str(charisma))
        print('-----------------------')



    return render_template('profession.html', fonction_test=fonction_test(), prof=prof, Fo=strength, De=dexterity, Co=constitution, In=intelligence, Sa=wisdom, Ch=charisma)

def fonction_test():
    global player
    player.increase_attribute(40, 'charisma')
    return getattr(player, 'charisma')

app.run()