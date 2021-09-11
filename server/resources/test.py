from flask_restful import fields, marshal_with, reqparse, Resource

post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'part', type=str,
    dest= 'part'
)

test_fields = {
    'part' : fields.String,
    'info' : fields.String,
    'tt': {
        'one': fields.String,
        'two': fields.String,
    },
}

class test(Resource):
    @marshal_with(test_fields)
    def get(self):
        argus = post_parse.parse_args()
        wis = argus.part
        return {'info':wis,'part':wis, 'one':wis, 'two':wis,}