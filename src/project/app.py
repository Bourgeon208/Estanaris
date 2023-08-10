import os

from flask import Flask, session
from flask_socketio import join_room, leave_room, send, SocketIO

import auth
import db
import blog
import game


test_config = None

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'project.sqlite'),
)

# dict of users rooms
app.rooms = {}

socketio = SocketIO(app)

if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

db.init_app(app)

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


if __name__ == "__main__":
    socketio.run(app, debug=True)