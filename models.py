from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Puppy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    puppy_name = db.Column(db.String(80), nullable=False)
    def __init__(self, name):
        self.puppy_name = name

        