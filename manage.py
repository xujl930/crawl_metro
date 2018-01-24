# -*- coding:utf8 -*-
import os
from flask_script import Manager, Shell, Server
from app import create_app

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')

manager = Manager(app)

def make_shell_context():
    from app.model.models import City, Metro
    return dict(app=app, city=City, metro=Metro)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host="127.0.0.1", use_debugger=True))



if __name__ == '__main__':
    manager.run()