import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Utilisateurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(30), unique=True, nullable=False)
    nom = db.Column(db.String(30), unique=False, nullable=False)
    postnom = db.Column(db.String(30), unique=False, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)
    adress = db.Column(db.String(30), unique=False, nullable=False)

    is_validate = db.Column(db.Integer, unique=False, nullable=False)
    #is_validate = Column(Boolean, unique=False, default=TruFe)

    id_group = db.Column(db.String(30), unique=False, nullable=True)
    
    type = db.Column(db.Integer, unique=False, nullable=False)
    sexe = db.Column(db.String(1),  unique=False, nullable=False)
    
    def __init__(self, phone, nom, postnom, password, adress, is_validate, id_group, type, sexe):
        self.phone = phone
        self.nom = nom
        self.postnom = postnom
        self.password = password
        self.adress = adress
        self.is_validate = is_validate
        self.id_group = id_group
        self.type = type
        self.sexe = sexe
        
    def json(self):
        return {
            'id': self.id,
            'phone': self.phone,
            'nom': self.nom,
            'postnom': self.postnom,
            'password': self.password,
            'adress': self.adress,
            'is_validate': self.is_validate,
            'id_group': self.id_group,
            'type': self.type,
            'sexe': self.sexe
        }
    
    @classmethod
    def find_by_phone(cls, phone):
        return cls.query.filter_by(phone=phone).first()
    
    def save_to(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_(self):
        db.session.delete(self)
        db.session.commit()
        
class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), unique=True, nullable=False)
    adress = db.Column(db.String(30), unique=False, nullable=False)
    type = db.Column(db.Integer, unique=False, nullable=False)
    phone_chef = db.Column(db.String(30), unique=False, nullable=True)
    id_coop = db.Column(db.String(30), unique=False, nullable=True)

    def __init__(self, nom, adress, type, phone_chef, id_coop):
        self.nom = nom
        self.adress = adress
        self.type = type
        self.phone_chef = phone_chef
        self.id_coop = id_coop
        
    def json(self):
        return {'id':self.id, 'Nom': self.nom, 'Adress': self.adress, 'Type': self.type,'id_coop':self.id_coop, 'Phone_chef':self.phone_chef}
    
    @classmethod
    def find_by_nom(cls, nom):
        return cls.query.filter_by(nom=nom).first()
    
    def save_to(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_(self):
        db.session.delete(self)
        db.session.commit()
    
class Coops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), unique=True, nullable=False)
    adress = db.Column(db.String(30), unique=False, nullable=False)
    type = db.Column(db.Integer, unique=False, nullable=False)
    phone_chef = db.Column(db.String(30), unique=False, nullable=True)
    
    def __init__(self, nom, adress, type, phone_chef):
        self.nom = nom
        self.adress = adress
        self.type = type
        self.phone_chef = phone_chef
        
    def json(self):
        return {'id':self.id, 'Nom': self.nom, 'Adress': self.adress, 'Type': self.type, 'Phone_chef':self.phone_chef}
    
    @classmethod
    def find_by_nom(cls, nom):
        return cls.query.filter_by(nom=nom).first()
    
    def save_to(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_(self):
        db.session.delete(self)
        db.session.commit()

class Credits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    somme = db.Column(db.Integer, unique=False, nullable=False)
    # date_demand = db.Column(db.Integer, unique=False, nullable=False)
    date_demand = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    taux = db.Column(db.Integer, unique=False, nullable=False)
    duree = db.Column(db.Integer, unique=False, nullable=False)
    etat = db.Column(db.Integer, unique=False, nullable=False)
    motif = db.Column(db.String(100), unique=False, nullable=False)
    phone_user = db.Column(db.String(30), unique=False, nullable=False)
    
    def __init__(self, phone_user, somme, taux, duree, etat, motif):
        self.phone_user = phone_user        
        self.somme = somme
        # self.date_demand = date_demand
        self.taux = taux
        self.duree = duree
        self.etat = etat
        self.motif = motif

    def json(self):
        # https://stackoverflow.com/questions/35337299/python-datetime-to-float-with-millisecond-precision
        # timestamp
        # strftime('%Y-%m-%d %H%M%S')
        # fromtimestamp(ts)
        return {'id' : self.id, 'phone_user' : self.phone_user, 'somme' : self.somme, 'date_demand' : self.date_demand.strftime('%d-%m-%Y'),'date_demand_full' : self.date_demand.timestamp(), 'taux' : self.taux, 'duree' : self.duree, 'etat' : self.etat, 'motif' : self.motif}
    
    @classmethod
    def find_by_phone_user(cls, phone_user):
        return cls.query.filter_by(phone_user=phone_user).first()

    @classmethod
    def find_by_id_(cls, id):
        return cls.query.filter_by(id=id).first()
    
    def save_to(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_(self):
        db.session.delete(self)
        db.session.commit()

# Echeance
class Echeances(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    somme = db.Column(db.Float, unique=False, nullable=False)
    date_payement = db.Column(db.DateTime)

    # interet = db.Column(db.Float, unique=False, nullable=False)
    etat = db.Column(db.Integer, unique=False, nullable=False)
    id_credit = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, somme, date_payement, etat, id_credit):
        self.somme = somme
        self.date_payement = date_payement
        self.id_credit = id_credit
        self.etat = etat

    def json(self):
        # https://stackoverflow.com/questions/35337299/python-datetime-to-float-with-millisecond-precision
        # timestamp
        # strftime('%Y-%m-%d %H%M%S')
        # fromtimestamp(ts)
        return {'id' : self.id, 'somme' : self.somme, 'date_payement' : self.date_payement.strftime('%d-%m-%Y'), 'etat' : self.etat, 'id_credit' : self.id_credit}
    
    @classmethod
    def find_by_id_(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_id_credits(cls, id):
        return cls.query.filter_by(id_credit=id_credit).first()
    
    def save_to(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_(self):
        db.session.delete(self)
        db.session.commit()