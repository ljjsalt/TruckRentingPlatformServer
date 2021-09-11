from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase


NAME = {
    'USER': 'USERNAME',
    'DRIVER': 'DRIVERNAME',
}


post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'username', type=str,
    dest = 'username',
)
post_parse.add_argument(
    'password', type=str,
    dest = 'password',
)
post_parse.add_argument(
    'duty', type=str,
    dest = 'duty',
)


#Output
register_fields = {
    'result' : fields.Integer,
}

def create_one(name, password, duty):
    db = LTDatabase(duty)
    if not db.has_info((NAME[duty],name)):
        db.add_info({
            NAME[duty]:name,
            'PASSWORD':password,
            'NICKNAME':name,
            'HEAD':'default.jpg',
        })
        return 1
    return 0


class user_register(Resource):
    @marshal_with(register_fields)
    def post(self):
        args = post_parse.parse_args()
        if create_one(args.username, args.password, args.duty):
            return {'result': 1}
        else:
            return {'result': 0}


if __name__ == '__main__':
    create_one('ljjcnm5438', '123456', 'DRIVER')
