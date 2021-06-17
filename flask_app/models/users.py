from ..config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id  = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        print(results)
        users = []
        
        for pal in results:
            users.append(cls(pal))
        return users

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at ) VALUES (%(first_name)s, %(last_name)s,%(email)s, NOW(),NOW());"
        
        users_id = connectToMySQL('users_schema').query_db(query,data)
        return users_id
         
         
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query)
        
    