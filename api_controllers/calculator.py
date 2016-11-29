from flask_restplus import Namespace, Resource


api = Namespace('calc', 'A calculator controller')


@api.route('/add/<int:id1>/<int:id2>')
class Addition(Resource):

    def get(self, id1, id2):
        return id1 + id2


@api.route('/mult/<int:id1>/<int:id2>')
class Multiplication(Resource):

    def get(self, id1, id2):
        return id1 * id2
