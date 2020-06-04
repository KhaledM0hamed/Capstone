import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie


class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        # self.database_name = "example"
        # self.database_path = "postgres://{}/{}".format(
        #     'localhost:5432', self.database_name)
        self.DATABASE_URI = 'postgres://postgres:ASDasd225588@localhost:5432/testcap'
        setup_db(self.app, self.DATABASE_URI)

        self.producer_headers = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjBJTDlPakIteVFQX2hLZU9LNVVndiJ9.eyJpc3MiOiJodHRwczovL2Jha2EtZGV2LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2OGI0Y2QzMmZjODBiZGY3NDNmMjkiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MTI2MDAzOSwiZXhwIjoxNTkxMjY3MjM5LCJhenAiOiJaRXhmMTlQUVM1MXh3ak1nSkg0TVUzME96YWJtMUw0UCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.D8-DKe84BUj7Um5UC2u9T2o-PPKXPjJ7_BNAP75ujOHHQKVOp4FP8IrzNaTUh_WOjEUpMQsfM6815GK7EBtuUk9pE4nlfww9gFB7cFFoI4bqXHwNF7NwXzksF02qOudr10PEIoDjLVuyhJh4JRfByOFC_IZGfYnyLDcjXX0LZ8BZwpdNNV8-xg8QIdpQhA4VhxTi_QiJNdTkoMO4F3kO1nW9MH25YO0tDES0ZbgpgwL9gmGiy3CWvLBCv3dyClSwRCrKBHRaxBB7A85szpoIwl-HdTgOGp4vif5s0EmRiAmt2kLU-VknS0fbDyQ9MUB6TECORXMOoPlQ0iu59NqMHA"
        self.assistant_headers = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjBJTDlPakIteVFQX2hLZU9LNVVndiJ9.eyJpc3MiOiJodHRwczovL2Jha2EtZGV2LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ2OGI0Y2QzMmZjODBiZGY3NDNmMjkiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MTI2MDAzOSwiZXhwIjoxNTkxMjY3MjM5LCJhenAiOiJaRXhmMTlQUVM1MXh3ak1nSkg0TVUzME96YWJtMUw0UCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.D8-DKe84BUj7Um5UC2u9T2o-PPKXPjJ7_BNAP75ujOHHQKVOp4FP8IrzNaTUh_WOjEUpMQsfM6815GK7EBtuUk9pE4nlfww9gFB7cFFoI4bqXHwNF7NwXzksF02qOudr10PEIoDjLVuyhJh4JRfByOFC_IZGfYnyLDcjXX0LZ8BZwpdNNV8-xg8QIdpQhA4VhxTi_QiJNdTkoMO4F3kO1nW9MH25YO0tDES0ZbgpgwL9gmGiy3CWvLBCv3dyClSwRCrKBHRaxBB7A85szpoIwl-HdTgOGp4vif5s0EmRiAmt2kLU-VknS0fbDyQ9MUB6TECORXMOoPlQ0iu59NqMHA"

        self.new_actor = {
            'name': 'karim',
            'age': 23,
            'gender': 'male'
        }
        self.new_movie = {
            'title': 'Avengers4',
            'description': 'description'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        with self.app.app_context():
            for i in range(10):
                new_actor = Actor(
                    name='ahmed',
                    age=30,
                    gender='male'
                )
                new_movie = Movie(
                    title='new movie',
                    description='dsadsa-dsa-dsa'
                )
                new_actor.insert()
                new_movie.insert()

    def tearDown(self):
        """Executed after reach test"""
        pass

    ###########
    # Test Actor get
    ###################
    def test_get_all_actors(self):
        res = self.client().get(
            '/actors', headers={
                "Authorization": self.producer_headers
            })
        # print(res)
        data = res.get_json()
        # print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["actors"]))

    def test_401_get_actors(self):
        res = self.client().get('/actors')
        data = res.get_json()

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unauthorized Error")

    ###############
    # Test Movie Get
    ##################
    def test_get_all_movies(self):
        res = self.client().get(
            '/Movies', headers={
                "Authorization": self.producer_headers
            })
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["movies"]))

    def test_405_get_movies(self):
        res = self.client().get('/movies')
        data = res.get_json()

        self.assertEqual(res.status_code, 405)

    ###################
    # Test Post Actor
    ###################
    def test_post_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers={
                                     "Authorization": self.producer_headers
                                 })
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_401_post_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor)
        data = res.get_json()

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unauthorized Error")

    ###################
    # Test Post Moive
    ###################
    def test_post_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers={
                                     "Authorization": self.producer_headers
                                 })
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_401_post_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = res.get_json()

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unauthorized Error")

    ###################
    # Test Patch Actor
    ###################

    def test_patch_actor(self):
        self.client().post('/actors', json=self.new_actor,
                           headers={
                               "Authorization": self.producer_headers
                           })
        res = self.client().patch('/actors/4', json={'name': 'ahmed',
                                                     'age': 25,
                                                     'gender': 'male'},
                                  headers={
                                      "Authorization": self.producer_headers
                                  })
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_404_patch_actor(self):
        res = self.client().patch('/actors/1000', json={'name': 'ahmed',
                                                        'age': 25,
                                                        'gender': 'male'},
                                  headers={"Authorization": self.producer_headers})
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)

    # ###################
    # # Test Patch Movie
    # ###################

    def test_patch_movie(self):
        self.client().post('/movies', json=self.new_movie,
                           headers={
                               "Authorization": self.producer_headers
                           })
        res = self.client().patch(
            '/movies/5', json={'title': 'ahmed',
                               'description': "dsdsads"},
            headers={
                "Authorization": self.producer_headers
            })
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        # self.assertTrue(len(data['movies']))

    ###################
    # Test Delete Actor
    ###################

    def test_422_delete_actor(self):
        self.client().post('/actors', json=self.new_actor, headers={"Authorization": self.producer_headers})
        self.client().post('/actors', json=self.new_actor, headers={"Authorization": self.producer_headers})
        res = self.client().delete('/actors/2',
                                   headers={"Authorization": self.producer_headers})
        data = res.get_json()

        self.assertEqual(res.status_code, 422)
        # self.assertEqual(data["success"], True)
        # self.assertTrue(len(data['actors']))

    # def test_404_delete_actor(self):
    #     res = self.client().delete('/actors/500',
    #                                headers={"Authorization": self.producer_headers})
    #     data = res.get_json()
    #
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Resource Not Found")
    #     self.assertTrue(len(data['actors']))

    ###################
    # Test Delete Movie
    ###################

    def test_422_delete_movie(self):
        res = self.client().delete('/movies/2',
                                   headers={"Authorization": self.producer_headers})
        data = res.get_json()

        self.assertEqual(res.status_code, 422)
        # self.assertEqual(data["success"], True)
        # self.assertTrue(len(data['movies']))

    # def test_404_delete_movie(self):
    #     res = self.client().delete('/movies/50',
    #                                headers={"Authorization": self.producer_headers})
    #     data = res.get_json()
    #
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Resource Not Found")
    #     self.assertTrue(len(data['movies']))

    ################
    # Test for assitant
    # Test Actor get
    ###################
    def test_get_all_actors_assistant(self):
        res = self.client().get(
            '/actors', headers={"Authorization": self.producer_headers})
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["actors"]))

    def test_401_get_actors_by_assistant(self):
        res = self.client().get('/actors')
        data = res.get_json()

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unauthorized Error")

    ###############
    # Test Movie Get
    ##################
    # def test_get_all_movies_assistant(self):
    #     res = self.client().get(
    #         '/movies', headers={"Authorization": self.producer_headers})
    #     data = res.get_json()
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(len(data["movies"]))


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
