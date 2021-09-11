from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase
from resources.token_lt import *
import json

def content_analysis(content):
    info = base64.b64decode(content.encode()).decode()
    dict = json.loads(info)
    return dict

post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'token', type= str,
    dest= 'token',
)

post_parse.add_argument(
    'content', type= str,
    dest= 'content'
)


# Output
user_info_fields = {
    # TODO blabla...
    'result': fields.Integer,
}

class update_user_info(Resource):

    @marshal_with(user_info_fields)
    def post(self):
        args = post_parse.parse_args()
        token = args.token
        content = content_analysis(args.content)
        info = check_token(token)

        if info:
            _username = info[0]
            _duty = info[1]
            db = LTDatabase(_duty)
            db.set_info(content, ('USERNAME', _username))
            return {'result':1}
        else:
            return {'result':0}


if __name__ == '__main__':
    db = LTDatabase('USER')
    db.set_info({'NICKNAME':'Snow','HISTORY_ORDER':'100000000','PRESENT_ORDER':'1000000001', 'DC':'ASDKJLJ123SA', 'AP':123,'DRIVERS': 'Imp'},('ID', 1))

