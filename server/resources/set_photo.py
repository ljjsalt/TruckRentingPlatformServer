from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase
from resources.token_lt import *
from resources.img import accio_photo


post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'token', type=str,
    dest='token',
)
post_parse.add_argument(
    'photo', type=str,
    dest='token'
)

# Output
user_info_fields = {
    # TODO blabla...
    'result': fields.Integer,
}


class get_photo(Resource):
    @marshal_with(user_info_fields)
    def post(self):
        args = post_parse.parse_args()
        info = check_token(args.token)
        if info:
            _username = info[0]
            _duty = info[1]
            db = LTDatabase(_duty)
            head = db.get_info(['HEAD'], ('USERNAME', _username))[0][0]
            photo = accio_photo(head)
            return {'result':1, 'photo': photo}
        else:
            return {'result':0, 'photo':'lol'}



if __name__ == '__main__':
    db = LTDatabase('USER')
    print(type(db.get_info(['HEAD'], ('ID', 1))[0][0]))
