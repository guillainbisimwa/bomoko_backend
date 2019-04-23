from flask import Flask
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

from base import db, Utilisateurs, Groups
db.init_app(app)
app.app_context().push()
db.create_all()

class Utilisateur_List(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nom', type=str, required=True, help='nom du User') 
    parser.add_argument('postnom', type=str, required=False, help='postnom du User') 
    parser.add_argument('password', type=str, required=False, help='password du User') 
    parser.add_argument('adress', type=str, required=False, help='adress du User') 
    parser.add_argument('is_validate', type=int, required=False, help='is_validate du User') 
    parser.add_argument('id_group', type=str, required=False, help='id_group du User') 
    parser.add_argument('type', type=int, required=False, help='type du User') 
    parser.add_argument('sexe', type=int, required=False, help='sexe du User') 
    
    def get(self, user):
        item = Utilisateurs.find_by_phone(user)
        if item:
            return item.json()
        return {'Message': 'User is not found'}
    
    def post(self, user):
        if Utilisateurs.find_by_phone(user):
            return {' Message': 'User with the phone {} already exists'.format(user)}
        args = Utilisateur_List.parser.parse_args()
        item = Utilisateurs(user, args['nom'], args['postnom'], args['password'], args['adress'], args['is_validate'], args['id_group'],args['type'],args['sexe'] )
        item.save_to()
        return item.json()
        
    def put(self, user):
        args = Utilisateur_List.parser.parse_args()
        item = Utilisateurs.find_by_phone(user)
        if item:
            item.nom = args['nom']
            item.postnom = args['postnom']
            item.password = args['password']
            item.adress = args['adress']
            item.is_validate = args['is_validate']
            item.id_group = args['id_group']
            item.type = args['type']
            item.sexe = args['sexe']
            item.save_to()
            return {'User': item.json()}
        item = Utilisateurs(user, args['nom'], args['postnom'], args['password'], args['adress'], args['is_validate'], args['id_group'],args['type'],args['sexe'])
        item.save_to()
        return item.json()
            
    def delete(self, user):
        item  = Utilisateurs.find_by_phone(user)
        if item:
            item.delete_()
            return {'Message': '{} has been deleted from records'.format(user)}
        return {'Message': '{} is already not on the list'.format()}
    
class All_Utilisateurs(Resource):
    def get(self):
        return {'Utilisateurs ': list(map(lambda x: x.json(), Utilisateurs.query.all()))}


class Group_List(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('adress', type=str, required=False, help='Adress of the group')
    parser.add_argument('type', type=int, required=True, help='Gross collection of the group')
    
    def get(self, group):
        item = Groups.find_by_nom(group)
        if item:
            return item.json()
        return {'Message': 'Groups is not found'}
    
    def post(self, group):
        if Groups.find_by_nom(group):
            return {' Message': 'Groups with the name {} already exists'.format(group)}
        args = Group_List.parser.parse_args()
        item = Groups(group, args['adress'], args['type'])
        item.save_to()
        return item.json()
        
    def put(self, group):
        args = Group_List.parser.parse_args()
        item = Groups.find_by_nom(group)
        if item:
            item.type = args['type']
            item.save_to()
            return {'Groups': item.json()}
        item = Groups(group, args['adress'], args['type'])
        item.save_to()
        return item.json()
            
    def delete(self, group):
        item  = Groups.find_by_nom(group)
        if item:
            item.delete_()
            return {'Message': '{} has been deleted from records'.format(group)}
        return {'Message': '{} is already not on the list'.format()}
    
class All_Groups(Resource):
    def get(self):
        return {'Groups': list(map(lambda x: x.json(), Groups.query.all()))}


api.add_resource(All_Utilisateurs, '/users/')
api.add_resource(Utilisateur_List, '/user/<string:user>')
api.add_resource(All_Groups, '/groups/')
api.add_resource(Group_List, '/group/<string:group>')

if __name__=='__main__':
    
    app.run(debug=True)
