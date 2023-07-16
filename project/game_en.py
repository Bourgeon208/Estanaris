from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from . import player
from . import naissance
from werkzeug.exceptions import abort

from project.auth import login_required
from project.db import get_db

bp = Blueprint('game_en', __name__, url_prefix='/game_en')

@bp.route('/start')
@login_required
def start():
    db = get_db()
    user_id = session.get('user_id')
    # try:
    temp_character = db.execute(
        'SELECT * FROM character WHERE (user_id = ? AND alive = 1)', (user_id,)
    ).fetchone()
    if not temp_character:
        return render_template('game_en/start.html')
    else:
        global character
        character = player.Player()
        character = temp_character
        print('Profession: ' + character['profession'])
        print('Name: ' + character['name'])
        print('Location: ' + character['location'])
        print('Level: ' + str(character['lv']))
        print('Renown: ' + str(character['renown']))
        print('Character: ' + str(character))
        character.player.initialize('en')
        return render_template('game_en/adventure.html', prof=character['profession'])

@bp.route('/map')
def map():
    return render_template('game_en/map.html')

# End part of creation and validation or restart creation
@bp.route('/profession', methods=['GET', 'POST'])
@login_required
def profession():
    if request.method == 'POST':
        global character
        character = player.Player()
        choix = request.form
        print('Choix   : ' + str(choix))
        naissance.creation(character, choix)
        alignment = character.calculate_alignement('en')
        prof = getattr(character, 'profession')
        prof_en = getattr(character, 'profession_en')
        prof_description = naissance.profession_description(prof, 'en')
        picture_wh = naissance.profession_picture(prof)
        strength = getattr(character, 'strength')
        dexterity = getattr(character, 'dexterity')
        constitution = getattr(character, 'constitution')
        intelligence = getattr(character, 'intelligence')
        wisdom = getattr(character, 'wisdom')
        charisma = getattr(character, 'charisma')
        character.initialize('en')
        character.hp = character.total_hp
        print('-----------------------')
        print('pic_width    : ' + str(picture_wh[0]))
        print('pic_height   : ' + str(picture_wh[1]))
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

    return render_template('game_en/profession.html', alignment=alignment, prof=prof, prof_en=prof_en, prof_description=prof_description,
                           Fo=strength, De=dexterity,Co=constitution, In=intelligence, Sa=wisdom, Ch=charisma,
                           Fo1=strength, De1=dexterity, Co1=constitution, In1=intelligence, Sa1=wisdom, Ch1=charisma,
                           pic_width=picture_wh[0], pic_height=picture_wh[1])

@bp.route('/name', methods=['GET', 'POST'])
@login_required
def name():
    if request.method == 'POST':
        choix = request.form
        print('Choix   : ' + str(choix))
        naissance.final_creation(character, choix)
        strength = getattr(character, 'strength')
        print('Strength     : ' + str(strength))
        return render_template('game_en/name.html')

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

        if not chouse_name:
            error = 'House name is required.'
        elif not cname:
            error = 'Character name is required.'
        elif not chouse_name.isalpha() or not cname.isalpha():
            error = 'Both names must be only in alphabetic letters.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO character "
                    "(user_id, alive, name, house, attribute, profession, profession_en, xp, alignment_lc, alignment_ge, "
                    "location, lv, hp, skills, classe, renown, reputation, dv) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (g.user['id'], getattr(character, 'alive'), cname, chouse_name,
                     getattr(character, 'attributes_aggregated'), getattr(character, 'profession'),
                     getattr(character, 'profession_en'), getattr(character, 'xp'), getattr(character, 'alignement_LC'),
                     getattr(character, 'alignement_GE'), getattr(character, 'location'), getattr(character, 'lv'),
                     getattr(character, 'hp'), getattr(character, 'skills_aggregated'), getattr(character, 'classe'),
                     getattr(character, 'renown'), getattr(character, 'reputation'), getattr(character, 'dv'))
                )
                db.commit()
            except db.IntegrityError:
                error = f"House name {chouse_name} is already registered."
            else:
                return render_template('game_en/adventure.html')

        flash(error)

        return render_template('game_en/name.html')

def save_character(character):
    user_id = session.get('user_id')
    db = get_db()
    try:
        db.execute(
            "UPDATE character "
            "SET "
            "(alive, attribute, profession, profession_en, xp, alignment_lc, alignment_ge, "
            "location, lv, hp, skills, classe, renown, reputation, dv) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (getattr(character, 'alive'), getattr(character, 'attributes_aggregated'), getattr(character, 'profession'),
             getattr(character, 'profession_en'), getattr(character, 'xp'), getattr(character, 'alignement_LC'),
             getattr(character, 'alignement_GE'), getattr(character, 'location'), getattr(character, 'lv'),
             getattr(character, 'hp'), getattr(character, 'skills_aggregated'), getattr(character, 'classe'),
             getattr(character, 'renown'), getattr(character, 'reputation'), getattr(character, 'dv')),
            "WHERE (user_id = ? AND alive = 1)", (user_id,)
        )
    except Exception as e:
        print(e)
    return