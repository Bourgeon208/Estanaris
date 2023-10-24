import os

from flask import Flask, session
from flask_socketio import join_room, leave_room, send, SocketIO

from . import auth
from .db import init_db
from . import blog
from . import game

from pathlib import Path


test_config = None

# Create and configure the app
app = Flask(__name__, instance_relative_config=True)

DB_PATH = Path(app.instance_path) / 'project.sqlite'

app.config.from_mapping(SECRET_KEY='dev', DATABASE=DB_PATH)

# Dict of users chat rooms
app.rooms = {}

socketio = SocketIO(app)

if test_config is None:
    # Load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
else:
    # Load the test config if passed in
    app.config.from_mapping(test_config)

# Ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# Create database if not exists
with app.app_context():
    if not DB_PATH.is_file():
        init_db()

# Register blueprints
app.register_blueprint(auth.bp)

app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')

app.register_blueprint(game.bp)
app.add_url_rule('/game', endpoint='language')

@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in app.rooms:
        return 
    
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    app.rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in app.rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    app.rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in app.rooms:
        app.rooms[room]["members"] -= 1
        if app.rooms[room]["members"] <= 0:
            del app.rooms[room]
    
    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")

# Project entry point
def main():
    socketio.run(app, debug=True)

# Run via command line `python app.py`
if __name__ == "__main__":
    main()