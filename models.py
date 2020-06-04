from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app = Flask(__name__)

db = SQLAlchemy()

DATABASE_URI = 'postgres://wdmyetjeqbkndp:615bc5953ae270575b30347962d72791bdae915286fcf5957ce274a6801abfb1@ec2-54-86-170-8.compute-1.amazonaws.com:5432/dbnf6h56rtevtj'


def setup_db(app, DATABASE_URI = DATABASE_URI):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)


class Actor(db.Model):
    __tablename__ = "Actor"
    actor_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'actor_id': self.actor_id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


class Movie(db.Model):
    __tablename__ = "Movie"
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)

    def format(self):
        return {
            'movie_id': self.movie_id,
            'title': self.title,
            'description': self.description
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
