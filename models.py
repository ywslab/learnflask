from learnflask.app import db

class User(db.Model):
    name = db.Column(db.String,primary_key=True)
    password = db.Column(db.String)