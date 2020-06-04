# Casting Agency API - Capstone Project

### Project Motivation
The last and the most beautiful project in the whole nanodegree.        
it's an API for casting agency with different roles and different permissions.      
you can do CRUD operations for both actors and movies  
****

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

****

#### Virtual Environment

We recommend working within a virtual environment. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

****

#### PIP Dependencies

install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages from the `requirements.txt` file.

****

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database.  

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

****

### Database Setup

Ensure you have PostgreSQL installed and running on your local machine
Create the Database by running the following in the terminal:
```
createdb casting
```

****

## Running the server

From within the current directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python app.py
```

****

## API Endpoints

#### GET '/'
- Request Arguments: None
- Returns:
    - It will return an error from our error handlers cause this route is not found.
    
#### GET '/movies'
- Request Arguments: None
- Returns:
    - List of movies consisting of total movies number, description and title 
 ```
{
    "movies": [
        {
            "descriptins": "wow it's a",
            "title": "IMT KILL ALL"
        }
    ],
    "success": true,
    "total_movies": 15
}
```  
#### POST '/movies'
- Request Arguments: 
```
{
    "title": "Hollywood",
    "description": "dsadsadsadas",
}
```
- Returns:
    - the newly created movie id and success key.
 ```
{
    "created": <movie ID>,
    "success": True
}
``` 
#### PATCH '/movies/<int:movie_id>'
- Request Arguments:
    - A movie id must be passed in the URL
```
{
    "title": "Time",
    "description": "pla pla pla",
}
```
- Returns:
    - the patched movie id and success key.
 ```
{
    "movie_id": <movie ID>,
    "success": True
}
``` 
#### DELETE '/movies/<int:movie_id>'
- Request Arguments: None. However, a movie id must be passed in the URL.
- Returns:
    - the deleted movie id and success key.
 ```
{
    "delete": <movie ID>,
    "success": True
}
``` 
#### GET '/actors'
- Request Arguments: None
- Returns:
    - List of actors consisting of actor name, actor age and gender. 
 ```
{
    "actors": [
        {
            "age": 54,
            "gender": "male",
            "name": "Brad Pitt"
        }
    ],
    "success": true
}
```  
#### POST '/actors'
- Request Arguments: 
```
{
    'name': 'Brad Pitt',
    'age': 54,
    'gender': 'male'
}
```
- Returns:
    - the newly created actor id and success key.
 ```
{
    "actor_ID": <actor_id>,
    "success": true
}
``` 
#### PATCH '/actors/<int:actor_id>'
- Request Arguments:
    - An actor id must be passed in the URL 
```
{
    'name': 'Brad Pitttttt',
    'age': 54,
    'gender': 'male'
}
```
- Returns:
    - the patched actor id and success key.
 ```
{
    "actor_id": <actor.id>,
    "success": true
}
``` 
#### DELETE '/actors/<int:actor_id>'
- Request Arguments: None. However, an actor id must be passed in the URL.
- Returns:
        - the deleted actor id and success key.
 ```
{
    "delete": <actor.id>,
    "success": true
}
``` 

****

## Authentication

The project also allows for users with different roles and privileges, namely:

#### Casting Assistant: 
- Permissions: Ability to view actors and movies.
#### Executive Producer: 
- Permissions: Includes Casting assistant permissions as well as being able to create an delete movies

****

## Testing Application
In order to run tests run the following commands: 

```
$ dropdb casting
$ python test_app.py
```


## Accessing Application
- The application hosted by heroku can be accessed [here](https://capfsnd.herokuapp.com/)
- Please note the JWT Tokens for the different roles mentioned above can be found in ```test_app.py``` and should be included in requests.
- If JWT tokens are expired you can create new ones by logging in at [this](https://baka-dev.auth0.com/authorize?audience=capstone&response_type=token&client_id=ZExf19PQS51xwjMgJH4MU30Ozabm1L4P&redirect_uri=http://localhost:8080/login-capstone) URL 
- Use the following credentials for different roles 
    - Casting Assistant: ```email``` = assistant@gmail.com | ```password``` = Udacity123
    - Executive Producer: ```email``` = producer@gmail.com | ```password``` = Udacity123