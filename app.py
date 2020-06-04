import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie, db
from auth import requires_auth, AuthError

app = Flask(__name__)


def create_app(test_config=None):
    # create and configure the app
    CORS(app)
    setup_db(app)

    # GET all Actors
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(jwt):
        try:
            actors_list = list(map(Actor.format, Actor.query.all()))
            return jsonify({"success": True,
                            "actors": actors_list,
                            "total_actors": len(Actor.query.all())
                            }), 200
        except Exception:
            abort(404)

    # GET all Movies
    @app.route('/Movies')
    @requires_auth('get:movies')
    def get_movies(jwt):
        try:
            movies_list = list(map(Movie.format, Movie.query.all()))
            return jsonify({"success": True,
                            "movies": movies_list,
                            "total_movies": len(Movie.query.all())
                            }), 200
        except Exception:
            abort(404)

    # POST an actor
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def post_actor(jwt):
        try:
            body = request.get_json(force=True)
            new_name = body.get('name', None)
            new_age = body.get('age', None)
            new_gender = body.get('gender', None)
        except Exception:
            abort(400)
        try:
            new_actor = Actor(name=new_name,
                              age=new_age,
                              gender=new_gender)
            db.session.add(new_actor)
            db.session.commit()
            return jsonify({
                "success": True,
                "actor_ID": new_actor.actor_id
            }), 200
        except Exception:
            abort(422)

    # POST a new movie
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def post_movie(jwt):
        body = request.get_json(force=True)
        new_title = body.get('title', None)
        new_description = body.get('description', None)
        try:
            new_movie = Movie(title=new_title,
                              description=new_description)
            db.session.add(new_movie)
            db.session.commit()
            return jsonify({
                'success': True,
                'created': new_movie.movie_id
            }), 200
        except Exception:
            abort(422)

    # edit an actor
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def patch_actor(jwt, actor_id):
        # find_actor = Actor.query.get(actor_id)
        actor = Actor.query.filter(Actor.actor_id == actor_id).one_or_none()
        # print(actor.format())
        if actor is None:
            abort(404)

        body = request.get_json(force=True)
        try:
            actor.name = body.get('name')
            actor.age = body.get('age')
            actor.gender = body.get('gender')
            db.session.commit()
            return jsonify({
                'success': True,
                'actor_id': actor.actor_id
            })
        except Exception:
            abort(500)

    # edit a movie
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def patch_movie(jwt, movie_id):
        movie = Movie.query.filter(Movie.movie_id == movie_id).one_or_none()
        print(movie.format())
        if movie is None:
            abort(404)

        body = request.get_json(force=True)
        try:
            movie.title = body.get('title')
            movie.description = body.get('description')
            db.session.commit()
            return jsonify({
                'success': True,
                'movie_id': movie.movie_id
            })
        except Exception:
            abort(500)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(jwt, actor_id):
        try:
            actor = Actor.query.filter(Actor.actor_id == actor_id).one_or_None()
            if actor is None:
                abort(404)
            db.session.delete(actor)
            db.session.commit()

            # actor.delete()     --> ?
            return jsonify({
                'success': True,
                'delete': actor_id
            }), 200
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(jwt, movie_id):
        try:
            movie = Movie.query.filter(Movie.movie_id == movie_id).one_or_None()
            if movie is None:
                abort(404)
            db.session.delete(movie)
            db.session.commit()

            # movie.delete()
            return jsonify({
                'success': True,
                'delete': movie_id
            }), 200
        except Exception:
            abort(422)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(401)
    def Unauthorized_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized Error"
        }), 401

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response
    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)
