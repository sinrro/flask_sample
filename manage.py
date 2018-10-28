from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models.user import User

app = create_app('default')

migrate = Migrate(app=app, db=db)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager = Manager(app)
manager.add_command('runserver', Server(host='127.0.0.1', port=80, use_debugger=True, use_reloader=True))
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run(default_command='runserver')
    # manager.run(default_command='shell')




# 这里可以创建shell模式，在shell模式下可以使用命令删除或创建数据库
# 删除的命令是：db.drop_all()，创建的命令是：db.create_all()
# 创建和删除哪些表需要提前将ORM模型引入进来（就是加到make_shell_context函数里）
 # manager.run(default_command='shell')

# 数据库迁移使用的命令
# python manage.py db init
# python manage.py db migrate -m "initial migrate"
# python manage.py db upgrade

# 更新requirements文件的命令
# pip freeze >requirements\common.txt