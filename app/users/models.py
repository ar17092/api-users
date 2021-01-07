from app.db import db, BaseModelMixin

class User(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User({self.email})'

    def __str__(self):
        return f'{self.id}'

    def get_by_email(email):
        return User.query.filter_by(email=email).first()
