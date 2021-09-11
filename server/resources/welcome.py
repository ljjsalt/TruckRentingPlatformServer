from flask_restful import fields, marshal_with, reqparse, Resource

class welcome(Resource):

    def get(self):
        return "LOOKS NOT BAD!"