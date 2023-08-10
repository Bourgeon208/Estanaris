from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session, Flask
)
from .classes import player
from .classes import naissance
from werkzeug.exceptions import abort

from project.auth import login_required
from project.db import get_db
bp = Blueprint('game', __name__, url_prefix='/game')

@bp.route('/')
@login_required
def language():
    return render_template('game/language.html')

@bp.route('/start', methods=['GET', 'POST'])
@login_required
def start():
    if request.method == 'POST':
        # ---------------------------------------------------------------
        name = 'Momo'
        room = generate_unique_code(4)
        rooms[room] = {"members": 0, "messages": []}
        session["room"] = room
        session["name"] = name
        # --------------------------------------------------
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
            return render_template(f'game/{language}/adventure.html', prof=getattr(character, 'profession'), code=room, messages=rooms[room]["messages"])

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

    return render_template(f'game/{language}/profession.html', alignment=alignment, prof=prof, prof_en=prof_en, prof_description=prof_description,
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
        return render_template(f'game/{language}/name.html')



@bp.route('/adventure', methods=['GET', 'POST'])
@login_required
def adventure():
    if request.method == 'POST':
        # ---------------------------------------------------------------
        name = 'Momo'
        room = generate_unique_code(4)
        rooms[room] = {"members": 0, "messages": []}
        session["room"] = room
        session["name"] = name
        # --------------------------------------------------

        # finishes character creation and store it in the database
        choix = request.form
        chouse_name = choix.get('chouse_name')
        cname = choix.get('cname')
        db = get_db()
        error = None

        if not chouse_name:
            error = 'House name is required.'
        elif not cname:
            error = 'Character name is required.'
        elif not chouse_name.isalpha() or not cname.isalpha():
            error = 'Both names must be only in alphabetic letters.'

        if error is None:
            try:
                character.db_character_create(g.user['id'], cname, chouse_name)
            except db.IntegrityError:
                error = f"House name {chouse_name} is already registered."
            else:
                return render_template(f'game/{language}/adventure.html', code=room, messages=rooms[room]["messages"])

        flash(error)

        return render_template(f'game/{language}/name.html')

# ------------------------------------------------------------------------------------------

from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase
# from . import create_app


app = Flask(__name__)
socketio = SocketIO(app)

rooms = {}


def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)

        if code not in rooms:
            break

    return code

# @bp.route("/room")
# def room():
#     room = session.get("room")
#     return render_template("adventure.html", code=room, messages=rooms[room]["messages"])

@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return

    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return

    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]

    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")


