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
    phone_chef = db.Column(db.String(30), unique=False, nullable=False)
    id_coop = db.Column(db.String(30), unique=False, nullable=True)

    
    def __init__(self, nom, adress, type, phone_chef, id_coop):
        self.nom = nom
        self.adress = adress
        self.type = type
        self.phone_chef = phone_chef
        self.id_coop = id_coop
        
    def json(self):
        return {'Nom': self.nom, 'Adress': self.adress, 'Type': self.type,'id_coop':self.id_coop, 'Phone_chef':self.phone_chef, 'id':self.id}
    
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
    phone_chef = db.Column(db.String(30), unique=False, nullable=False)
    
    def __init__(self, nom, adress, type, phone_chef):
        self.nom = nom
        self.adress = adress
        self.type = type
        self.phone_chef = phone_chef
        
    def json(self):
        return {'Nom': self.nom, 'Adress': self.adress, 'Type': self.type, 'Phone_chef':self.phone_chef, 'id':self.id}
    
    @classmethod
    def find_by_nom(cls, nom):
        return cls.query.filter_by(nom=nom).first()
    
    def save_to(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_(self):
        db.session.delete(self)
        db.session.commit()
