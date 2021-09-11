from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase
from resources.token_lt import accio_token


def login(username, password, duty):
    # TODO LOGIN
    db = LTDatabase(duty)
    content = db.get_info(['USERNAME','PASSWORD'],('USERNAME', username))[0]
    _username, _password = content
    if _password:
        if password == _password:
            return accio_token(_username, duty)
        return 0
    else:
        return 0


post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'username', type=str,
    dest='username',
)

post_parse.add_argument(
    'password', type=str,
    dest='password',
)
post_parse.add_argument(
    'duty', type=str,
    dest='duty',
)


# Output
login_fields = {
    'result': fields.Integer,
    'token': fields.String(default='default'),
}


def check():
    pass


class user_login(Resource):
    @marshal_with(login_fields)
    def post(self):
        args = post_parse.parse_args()
        answer = login(args.username, args.password, args.duty)
        if answer:
            return {'result': 1, 'token': answer}
        else:
            return {'result': 0, 'token': answer}


if __name__ == '__main__':
    print(login('ljjjx1997','123456', 'USER'))
