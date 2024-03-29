from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session, current_app
)
from secrets import token_hex

from .auth import login_required
from .classes import player
from .classes import naissance
from .db import get_db


bp = Blueprint('game', __name__, url_prefix='/game')


@bp.route('/')
@login_required
def language():
    return render_template('game/language.html')


@bp.route('/start', methods=['GET', 'POST'])
@login_required
def start():
    if request.method == 'POST':
        global language
        language = request.form.get('language')
        db = get_db()
        user_id = session.get('user_id')
        # try:
        temp_character = db.execute(
            'SELECT * FROM character WHERE (user_id = ? AND alive = 1)', (user_id,)
        ).fetchone()
        if not temp_character:
            return render_template(f'game/{language}/start.html')
        else:
            global character
            character = player.Player()
            character.initialize(temp_character, language)
            # return render_template(f'game/{language}/adventure.html')
            return redirect(url_for('game.adventure'))
            # return redirect(url_for(f'game.{language}.adventure'))


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
    if request.method == 'POST':
        # Determine the character's profession (including attributes and various stats) using the start.html form
        global character
        character = player.Player()
        choix = request.form
        print('Choix   : ' + str(choix))
        naissance.creation(character, choix)
        alignment = character.calculate_alignement(language)
        prof = getattr(character, 'profession')
        prof_en = getattr(character, 'profession_en')
        prof_description = naissance.profession_description(prof, language)
        picture_wh = naissance.profession_picture(prof)
        strength = getattr(character, 'strength')
        dexterity = getattr(character, 'dexterity')
        constitution = getattr(character, 'constitution')
        intelligence = getattr(character, 'intelligence')
        wisdom = getattr(character, 'wisdom')
        charisma = getattr(character, 'charisma')
        character.calculate_all(language)
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

    return render_template(f'game/{language}/profession.html', alignment=alignment, prof=prof, prof_en=prof_en,
                           prof_description=prof_description,
                           Fo=strength, De=dexterity, Co=constitution, In=intelligence, Sa=wisdom, Ch=charisma,
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
        return render_template(f'game/{language}/name.html')


@bp.route('/adventure', methods=['GET', 'POST'])
@login_required
def adventure():
    main_room = "Aléhandre"
    create_room(main_room)

    # Character creation
    if request.method == 'POST':
        # finishes character creation and store it in the database
        choix = request.form
        chouse_name = choix.get('chouse_name')
        character_name = choix.get('cname')
        db = get_db()
        error = None

        if not chouse_name:
            error = 'House name is required.'
        elif not character_name:
            error = 'Character name is required.'
        elif not chouse_name.isalpha() or not character_name.isalpha():
            error = 'Both names must be only in alphabetic letters.'

        if error is None:
            try:
                character.db_character_create(g.user['id'], character_name, chouse_name)
            except db.IntegrityError:
                error = f"House name {chouse_name} is already registered."
            else:
                join_room(main_room, character_name)
                return render_template(f'game/{language}/adventure.html')
        flash(error)
        return render_template(f'game/{language}/name.html')
    # If character exists
    else:
        join_room(main_room, character.name)
        return render_template(f'game/{language}/adventure.html')
    # return render_template(f'game/{language}/adventure.html', code=room, name=cname, messages=rooms[room]["messages"])


def join_room(room_name, character_name):
    """Set room attributes in current session."""
    rooms = current_app.rooms

    session["room"] = room_name
    session["name"] = character_name

    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("/"))

def create_room(room_name):
    """Create a room."""
    rooms = current_app.rooms
    rooms[room_name] = {"members": 0, "messages": []}

