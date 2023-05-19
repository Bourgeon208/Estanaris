from flask import Flask, render_template, request
from Player import Player
from naissance import creation

app = Flask(__name__)

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# Character creation
@app.route('/naissance', methods=['GET', 'POST'])
def naissance():
    global player
    player = Player()
    return render_template('naissance.html')


# End part of creation and validation or restart creation
@app.route('/profession', methods=['GET', 'POST'])
def profession():
    global player
    if request.method == 'POST':
        choix = request.form
        creation(player, choix)
        alignment = player.calculate_alignement()
        prof = getattr(player, 'profession')
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

        return render_template('profession.html', fonction_test=fonction_test(),alignment=alignment, prof=prof, Fo=strength, De=dexterity,
                               Co=constitution, In=intelligence, Sa=wisdom, Ch=charisma, )

@app.route('/adventure', methods=['GET', 'POST'])
def adventure():
    global player
    if request.method == 'POST':
        pass
    return render_template('adventure.html')\

@app.route('/world_map', methods=['GET', 'POST'])
def world_map():
    return render_template('world_map.html')

def fonction_test():
    global player
    player.increase_attribute(40, 'charisma')

app.run()
