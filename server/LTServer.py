from flask import Flask
from flask_restful import Api

from resources.user_login import user_login
from resources.user_register import user_register
from resources.get_user_info import get_user_info
from resources.update_user_info import update_user_info
from resources.get_photo import get_photo

from resources.database.database import LTDatabase

# TODO TEST!
from resources.welcome import welcome
from resources.test import test

app = Flask(__name__)
api = Api(app)

api.add_resource(user_login, '/user_login')
api.add_resource(get_user_info, '/get_user_info')
api.add_resource(user_register, '/user_register')
api.add_resource(update_user_info, '/update_user_info')
api.add_resource(get_photo, '/get_photo')



@app.cli.command('createdb')
def create_db():
    db = LTDatabase('USER')
    db.create_db()

'''
@app.cli.command('savedb')
def save_db():
    LTDatabase.save_db()

@app.cli.command('creatdb')
def create_db():
    LTDatabase.create_db()

'''

# TODO TEST!
api.add_resource(welcome, '/')
api.add_resource(test, '/test')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
