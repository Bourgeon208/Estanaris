from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from . import player
from . import naissance
from werkzeug.exceptions import abort

from project.auth import login_required
from project.db import get_db

bp = Blueprint('game', __name__, url_prefix='/game')

@bp.route('/')
@login_required
def start():
    db = get_db()
    user_id = session.get('user_id')
    # try:
    temp_character = db.execute(
        'SELECT * FROM character WHERE (user_id = ? AND alive = 1)', (user_id,)
    ).fetchone()
    if not temp_character:
        return render_template('game/start.html')
    else:
        global character
        character = player.Player()
        player.initialize(character, temp_character)
        character = temp_character
        print('Character Row: ' + str(character))
        print('Profession: ' + character['profession'])
        # return render_template('game/adventure.html')
        return render_template('game/adventure.html', prof=character['profession'])

@bp.route('/map')
def map():
    return render_template('game/map.html')


@bp.route('/test')
def test():
    return render_template('game/test.html')

# End part of creation and validation or restart creation
@bp.route('/profession', methods=['GET', 'POST'])
@login_required
def profession():
    # try:
    if request.method == 'POST':
        global character
        character = player.Player()
        choix = request.form
        print('Choix   : ' + str(choix))
        naissance.creation(character, choix)
        alignment = character.calculate_alignement()
        prof = getattr(character, 'profession')
        prof_description = naissance.profession_description(character, prof)
        strength = getattr(character, 'strength')
        dexterity = getattr(character, 'dexterity')
        constitution = getattr(character, 'constitution')
        intelligence = getattr(character, 'intelligence')
        wisdom = getattr(character, 'wisdom')
        charisma = getattr(character, 'charisma')
        print('-----------------------')
        print('Profession   : ' + prof)
        print('Alignment    : ' + alignment)
        print('Strength     : ' + str(strength))
        print('Dexterity    : ' + str(dexterity))
        print('Constitution : ' + str(constitution))
        print('Intelligence : ' + str(intelligence))
        print('Wisdom       : ' + str(wisdom))
        print('Charisma     : ' + str(charisma))
        print('-----------------------')
        # except:
        #     print('Error')

    return render_template('game/profession.html', alignment=alignment, prof=prof, prof_description=prof_description ,Fo=strength, De=dexterity,
                           Co=constitution, In=intelligence, Sa=wisdom, Ch=charisma, Fo1=strength, De1=dexterity,
                           Co1=constitution, In1=intelligence, Sa1=wisdom, Ch1=charisma)

@bp.route('/name', methods=['GET', 'POST'])
@login_required
def name():
    if request.method == 'POST':
        # finish character creation and store it in the database
        choix = request.form
        print('Choix   : ' + str(choix))
        naissance.final_creation(character, choix)
        strength = getattr(character, 'strength')
        print('Strength     : ' + str(strength))
        return render_template('game/name.html')

@bp.route('/adventure', methods=['GET', 'POST'])
@login_required
def adventure():
    if request.method == 'POST':
        # finishes character creation and store it in the database
        choix = request.form
        chouse_name = choix.get('chouse_name')
        cname = choix.get('cname')
        db = get_db()
        error = None
        attribute = 0
        alignment = 0

        if not chouse_name:
            error = 'House name is required.'
        elif not cname:
            error = 'Character name is required.'
        elif not chouse_name.isalpha() or not cname.isalpha():
            error = 'Both names must be only in alphabetic letters.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO character (user_id, alive, name, house, attribute, profession, xp, alignment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (g.user['id'], 1, cname, chouse_name, attribute, getattr(character, 'profession'), 0, alignment)
                )
                db.commit()
            except db.IntegrityError:
                error = f"House name {chouse_name} is already registered."
            else:
                return render_template('game/adventure.html')

        flash(error)

        return render_template('game/name.html')

