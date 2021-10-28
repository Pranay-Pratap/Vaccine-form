from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Employees(db.Model):
    __tablename__ = 'info_table'
 
    name = db.Column(db.String(), primary_key = True)
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    vaccine = db.Column(db.String())
 
    def __init__(self, name,age,gender,vaccine):
        self.name = name
        self.age = age
        self.gender = gender
        self.vaccine = vaccine
 
    def __repr__(self):
        return f"{self.name}:{self.age}:{self.gender}:{self.vaccine}"