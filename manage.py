from app import create_app
from flask_script import Manager, Server

app = create_app()
manager = Manager(app)
manager.add_command('runserver', Server(host='127.0.0.1', port=80, use_debugger=True, use_reloader=True))

if __name__ == '__main__':
    manager.run(default_command='runserver')
