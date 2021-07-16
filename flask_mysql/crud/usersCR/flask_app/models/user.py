from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the users table from our database
class user:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_crud').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users

# ... other class methods
    # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO user (first_name, last_name, email) VALUES ( %(first_name)s , %(last_name)s , %(email)s)"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_crud').query_db(query,data)