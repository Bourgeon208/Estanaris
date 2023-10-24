import os
from flask_socketio import join_room, leave_room, send, SocketIO
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    # test_config=None
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'project.sqlite'),
    )
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

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    from . import game
    app.register_blueprint(game.bp)
    app.add_url_rule('/game', endpoint='language')

    # app.config["SECRET_KEY"] = "hjhjsdahhds"
    # socketio = SocketIO(app)
    socketio.run(app)
    return app

    #
# if __name__ == '__main__':
#     socketio.run(app)




