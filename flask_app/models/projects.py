from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.__init__ import DATABASE

class User: # CHANGE PROJECT TO FILE NAME
    def __init__( self , data ): 
        self.id = data['id']        # CHANGE SELF.__ TO MATCH SCHEMA
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


'''
EACH LINE FROM HERE IS SUBJECT TO CHANGE, 
BUT THIS IS A TEMPLATE FOR WHAT YOU WANT FOR EACH CRUD STEP 
'''
# READ ALL
@classmethod
def get_all(cls):
    query = '''
        SELECT * FROM users;
    '''
    results = connectToMySQL(DATABASE).query_db(query)

    users = []

    for row in results:
        new_user = cls(row)
        users.append(new_user)

    return users


#READ ONE
@classmethod
def get_one(cls, id):
    data = {'id': id}
    query = '''
        SELECT * FROM users WHERE id = %(id)s;
    '''
    result = connectToMySQL(DATABASE).query_db(query, data)
    return User(result[0])


#UPDATE
@classmethod
def update(cls, data):
    query = '''
        UPDATE users 
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(id)s;
    '''
    results = connectToMySQL(DATABASE).query_db(query, data)
    return results


#DELETE
@classmethod
def delete(cls, id):
    data = {'id': id}
    query = '''
    DELETE FROM users WHERE id = %(id)s;
    '''
    result = connectToMySQL(DATABASE).query_db(query, data)
    return result