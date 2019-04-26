from flask import Flask
from flask_restful import Resource, reqparse, Api
import os

app = Flask(__name__)
api = Api(app)
#SQL_ALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

from base import db, Utilisateurs, Groups, Coops, Credits
db.init_app(app)
app.app_context().push()
db.create_all()

class Utilisateur_List(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone', type=str, required=False, help='Phone du User')
    parser.add_argument('nom', type=str, required=True, help='nom du User')
    parser.add_argument('postnom', type=str, required=False, help='postnom du User')
    parser.add_argument('password', type=str, required=False, help='password du User')
    parser.add_argument('adress', type=str, required=False, help='adress du User')
    parser.add_argument('is_validate', type=int, required=False, help='is_validate du User')
    parser.add_argument('id_group', type=str, required=False, help='id_group du User')
    parser.add_argument('type', type=int, required=False, help='type du User')
    parser.add_argument('sexe', type=str, required=False, help='sexe du User')
    
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
            item.phone = args['phone']
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
        return {' Message': 'User with the phone {} does not exist'.format(user)}
            
    def delete(self, user):
        item  = Utilisateurs.find_by_phone(user)
        if item:
            item.delete_()
            return {'Message': '{} has been deleted from records'.format(user)}
        return {'Message': '{} is already not on the list'.format(user)}
    
class All_Utilisateurs(Resource):
    def get(self):
        return {'Utilisateurs ': list(map(lambda x: x.json(), Utilisateurs.query.all()))}


class Group_List(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nom', type=str, required=False, help='Nom of the group')
    parser.add_argument('adress', type=str, required=False, help='Adress of the group')
    parser.add_argument('type', type=int, required=True, help='Gross collection of the group')
    parser.add_argument('phone_chef', type=str, required=False, help='Phone_chef of the group')
    parser.add_argument('id_coop', type=str, required=False, help='id_coop du Group')
    
    def get(self, group):
        item = Groups.find_by_nom(group)
        if item:
            return item.json()
        return {'Message': 'Groups is not found'}
    
    def post(self, group):
        if Groups.find_by_nom(group):
            return {' Message': 'Groups with the name {} already exists'.format(group)}
        args = Group_List.parser.parse_args()
        item = Groups(group, args['adress'], args['type'], args['phone_chef'] , args['id_coop'])
        item.save_to()
        return item.json()
        
    def put(self, group):
        args = Group_List.parser.parse_args()
        item = Groups.find_by_nom(group)
        if item:
            item.nom = args['nom']
            item.phone_chef = args['phone_chef']
            item.adress = args['adress']
            item.type = args['type']
            item.id_coop = args['id_coop']
            item.save_to()
            return {'Groups': item.json()}
        return {' Message': 'Group with the name {} does not exist'.format(group)}

    def delete(self, group):
        item  = Groups.find_by_nom(group)
        if item:
            item.delete_()
            return {'Message': '{} has been deleted from records'.format(group)}
        return {'Message': '{} is already not on the list'.format(group)}
    
class All_Groups(Resource):
    def get(self):
        return {'Groups': list(map(lambda x: x.json(), Groups.query.all()))}


class Coop_List(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nom', type=str, required=False, help='Nom of the coop')
    parser.add_argument('adress', type=str, required=False, help='Adress of the coop')
    parser.add_argument('type', type=int, required=True, help='Gross collection of the coop')
    parser.add_argument('phone_chef', type=str, required=False, help='Phone_chef of the coop')
    
    def get(self, coop):
        item = Coops.find_by_nom(coop)
        if item:
            return item.json()
        return {'Message': 'Coops is not found'}
    
    def post(self, coop):
        if Coops.find_by_nom(coop):
            return {' Message': 'Coops with the name {} already exists'.format(coop)}
        args = Coop_List.parser.parse_args()
        item = Coops(coop, args['adress'], args['type'], args['phone_chef'])
        item.save_to()
        return item.json()
        
    def put(self, coop):
        args = Coop_List.parser.parse_args()
        item = Coops.find_by_nom(coop)
        if item:
            item.nom = args['nom']
            item.phone_chef = args['phone_chef']
            item.adress = args['adress']
            item.type = args['type']
            item.save_to()
            return {'Coops': item.json()}
        return {' Message': 'Coop with the name {} does not exist'.format(coop)}

    def delete(self, coop):
        item  = Coops.find_by_nom(coop)
        if item:
            item.delete_()
            return {'Message': '{} has been deleted from records'.format(coop)}
        return {'Message': '{} is already not on the list'.format(coop)}
    
class All_Coops(Resource):
    def get(self):
        return {'Coops': list(map(lambda x: x.json(), Coops.query.all()))}


class Credit_List(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('somme', type=int, required=True, help='somme collection of the credit')
    parser.add_argument('date_demand', type=int, required=True, help='date_demand collection of the credit')
    parser.add_argument('taux', type=int, required=True, help='taux collection of the credit')
    parser.add_argument('duree', type=int, required=True, help='duree collection of the credit')
    parser.add_argument('etat', type=int, required=True, help='etat collection of the credit')
    parser.add_argument('motif', type=str, required=True, help='motif collection of the credit')
    # parser.add_argument('phone_user', type=str, required=False, help='phone_user collection of the credit')

    def get(self, credit):
        item = Credits.find_by_phone_user(credit)
        if item:
            return item.json()
        return {'Message': 'Credits is not found'}
    
    def post(self, credit):
        if Credits.find_by_phone_user(credit):
            return {' Message': 'Credits with the same phone user {} already exists'.format(credit)}
        args = Credit_List.parser.parse_args()
        item = Credits(credit, args['somme'], args['date_demand'], args['taux'], args['duree'], args['etat'], args['motif'])
        item.save_to()
        return item.json()
        
    def put(self, credit):
        args = Credit_List.parser.parse_args()
        item = Credits.find_by_phone_user(credit)
        if item:
            item.somme = args['somme']
            item.date_demand = args['date_demand']
            item.taux = args['taux']
            item.duree = args['duree']
            item.etat = args['etat']
            item.motif = args['motif']
            item.phone_user = args['phone_user']

            item.save_to()
            return {'Credits': item.json()}
        return {' Message': 'Credit with the phone {} does not exist'.format(credit)}

    def delete(self, credit):
        item  = Credits.find_by_phone_user(credit)
        if item:
            item.delete_()
            return {'Message': '{} has been deleted from records'.format(credit)}
        return {'Message': '{} is already not on the list'.format(credit)}
    
class All_Credits(Resource):
    def get(self):
        return {'Credits': list(map(lambda x: x.json(), Credits.query.all()))}


api.add_resource(All_Utilisateurs, '/users/')
api.add_resource(Utilisateur_List, '/user/<string:user>')

api.add_resource(All_Groups, '/groups/')
api.add_resource(Group_List, '/group/<string:group>')

api.add_resource(All_Coops, '/coops/')
api.add_resource(Coop_List, '/coop/<string:coop>')

api.add_resource(All_Credits, '/credits/')
api.add_resource(Credit_List, '/credit/<string:credit>')

if __name__=='__main__':
    
    app.run(debug=True)
