from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the users table from our database
class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save_ninja(cls, data ):
        query = "INSERT INTO ninja (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s , %(last_name)s , %(age)s, %(dojo_id)s)"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)
