# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# model the class after the user table from our database
# our class user that takes displays from the user table 
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# creating new users in SQL table
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email ) VALUES ( %(first_name)s , %(last_name)s , %(email)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data )

# retreving and displaying all users
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        all_users = []
        # Iterate over the db results and create instances of friends with cls.
        for users in results:
            all_users.append(cls(users))
        return all_users

# used to retreive only one user used when showing or editing a user 
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('users_schema').query_db(query, data)
        if len(results) > 0:
            return cls(results[0])
        return False

# edit user updating SQL 
    @classmethod
    def edit_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)

# delete user delete from SQL
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)
