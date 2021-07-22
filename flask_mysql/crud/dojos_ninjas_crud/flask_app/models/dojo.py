from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
# model the class after the users table from our database
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    @classmethod
    def get_ninjas_from_dojo(cls, data):
        query = "SELECT * FROM dojo LEFT JOIN ninja ON ninja.dojo_id = dojo.id WHERE dojo.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data) 
        dojo = cls(results[0])
        # dojo = Dojo(results[0]) ANOTHER WAY TO DO IT
        for row_from_db in results:
            ninja_data = {
                'id': row_from_db['ninja.id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'age': row_from_db['age'],
                'dojo_id': row_from_db['dojo_id'],
                'created_at': row_from_db['ninja.created_at'],
                'updated_at': row_from_db['ninja.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojo;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of users
        dojos = []
        # Iterate over the db results and create instances of users with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def save_dojo(cls, data ):
        query = "INSERT INTO dojo (name) VALUES (%(name)s)"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)
