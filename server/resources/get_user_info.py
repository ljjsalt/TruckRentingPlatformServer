from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase
from resources.token_lt import *

post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'token', type=str,
    dest='token',
)

# Output
user_info_fields = {
    # TODO blabla...
    'result': fields.Integer,
    'username': fields.String,
    'nickname': fields.String,
    'history_order': fields.String,
    'present_order': fields.String,
    'dc': fields.String,
    'ap': fields.Integer,
    'drivers': fields.String,
}


class get_user_info(Resource):
    @marshal_with(user_info_fields)
    def post(self):
        args = post_parse.parse_args()
        token = args.token
        info = check_token(token)

        if info:
            _username = info[0]
            _duty = info[1]
            db = LTDatabase(_duty)
            list = db.get_info(0, ('USERNAME', _username))[0]
            return {
                'result': 1,
                'username': list[1],
                'nickname': list[3],
                'history_order': list[5],
                'present_order': list[6],
                'dc': list[7],
                'ap': list[8],
                'drivers': list[9]
            }
        else:
            return {'result': 0}


if __name__ == '__main__':
    db = LTDatabase('USER')
    print(db.get_info(0, ('USERNAME','ljjjx1997'))[0])