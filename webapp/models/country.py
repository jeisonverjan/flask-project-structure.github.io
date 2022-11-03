from ..extensions import db

class Country(db.Model):
    name= db.Column(db.String, primary_key=True)
    code = db.Column(db.Integer)
    population = db.Column(db.Integer)

    