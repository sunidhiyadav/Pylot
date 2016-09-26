""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
import re
from system.core.model import Model

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def login_user(self, login_info):
        email = login_info['email']
        password = login_info['password']
        error_dict = {}
        error = False

        #Check if both fields are inputted
        if email == '':
            error_dict ['loginEmailError'] = "Please enter Email!"
            error = True
        elif not emailRegex.match(email): 
            error_dict ['loginEmailError'] = "Invalid email address!"
            error = True

        if password == '':
            error_dict ['loginPasswordError'] = "Please enter Password!"
            error = True
        elif len(password) < 8 :
            error_dict ['loginPasswordError'] = "Password must be greater than 8 characters!"
            error = True    
        elif not passwordRegex.match(password):
            error_dict['loginPasswordError'] = "Password must contain at least one lowercase letter, one uppercase letter, and one digit"
            error = True

                    

        #Check if user exists with the given email and password
        if not error:
            query = "SELECT * FROM users WHERE email = :email"
            email_data = {'email': login_info['email']}
            users = self.db.query_db(query, email_data)

            if not users:
                error_dict['loginEmailError'] = "Wrong Email entered."
                error = True
                return {"status":False, "error_dict": error_dict}

            elif users and self.bcrypt.check_password_hash(users[0]['password'], password):
               return {"status": True, "user": users[0]}
                  
            else:
                error_dict['loginPasswordError'] = "Wrong Password entered."
                error = True
                return {"status":False, "error_dict": error_dict}
        else:
            return {"status":False, "error_dict": error_dict}
        
            #User has been authenticated, log the user in
            #query = "SELECT * FROM users WHERE email = :email"
            #email_data = {'email': login_info['email']}
            #user = self.db.query_db(query, email_data)
 

    def get_user (self, id):
        query = "SELECT * FROM users WHERE id =:id"
        data = {'id' : id}
        user = self.db.query_db(query, data)
        return user[0]

    def register(self, register_info):

        first_name = register_info['first_name']
        last_name = register_info['last_name']
        alias = register_info['alias']
        email = register_info['email']
        password = register_info['password']
        confirm_password = register_info['confirm_password']
        dob = register_info['dob']

        error_dict = {}
        error = False

        #Check first name is atleast 2 chars
        if first_name == '' or len(first_name) < 2:
            error_dict['firstNameError'] = "First name must be atleast 2 characters."
            error = True
        elif any(char.isdigit() for char in first_name) == True:
            error_dict['firstNameError'] = "First name cannot have numbers"

        if last_name == '' or len(last_name) < 2:
            error_dict['lastNameError'] = "Last name must be atleast 2 characters."
            error = True
        elif any(char.isdigit() for char in last_name) == True:
            error_dict['lastNameError'] = "Last name cannot have numbers"    

        if len(alias) < 2:
            error_dict['aliasError'] = "Alias must be atleast 2 characters."
            error = True

        #Validate email
        if email == '':
            error_dict['emailError'] = "Email can not be blank."
            error = True
        elif not emailRegex.match(email):
            error_dict['emailError'] = "Invalid email address."
            error = True       

        #Check if email already exists in database
        query = "SELECT * FROM users WHERE email =:email"
        data = {'email':email}
        user = self.db.query_db(query, data)
        if len(user) > 0:
            error_dict['emailError'] = "Email address already exists. Please try registering with another email, or login using this email."
            error = True

        #Validate password
        if password == '':
            error_dict['passwordError'] = "Password cannot be blank."
            error = True
        elif len(password) < 8:
            error_dict['passwordError'] = "Password must be greater than 8 characters"

            error = True

        elif not passwordRegex.match(password):
            error_dict['passwordError'] = "Password must contain at least one lowercase letter, one uppercase letter, and one digit"
            error = True

        if confirm_password == '':
            error_dict['confirmPasswordError'] = "Confirm Password cannot be blank."
            error = True
        elif confirm_password != password :
             error_dict['confirmPasswordError'] = "Passwords do not match."
             error = True        

        #Check if there were any errors in the previous validation process
        if error:
            return {"status" : False, "error_dict": error_dict}

        #Add user to database if no errors then return the id for login purposes
        pw_hash = self.bcrypt.generate_password_hash(password)
        insert_query = "INSERT INTO users (first_name, last_name, alias, email, password,dob, created_at, updated_at) VALUES (:first_name, :last_name, :alias, :email, :password,:dob, NOW(), NOW())"
        data = {'first_name':first_name,
            'last_name':last_name,
            'alias':alias,
            'email':email,
            'password':pw_hash,
            'dob':dob}
        self.db.query_db(insert_query, data)

        query = "SELECT * FROM users where email=:email"
        data = {'email':email}
        user = self.db.query_db(query, data)
        return{"status": True, "user": user[0]}
        
    def edit_user_details(self, edit_info, id):

        first_name = edit_info['first_name']
        last_name = edit_info['last_name']
        alias = edit_info['alias']
        email = edit_info['email']
        password = edit_info['password']
        confirm_password = edit_info['confirm_password']

        error_dict = {}
        error = False

        #Check first name is atleast 2 chars
        if first_name == '' or len(first_name) < 2:
            error_dict['firstNameError'] = "First name must be atleast 2 characters."
            error = True
        elif any(char.isdigit() for char in first_name) == True:
            error_dict['firstNameError'] = "First name cannot have numbers"

        if last_name == '' or len(last_name) < 2:
            error_dict['lastNameError'] = "Last name must be atleast 2 characters."
            error = True
        elif any(char.isdigit() for char in last_name) == True:
            error_dict['lastNameError'] = "Last name cannot have numbers"    

        if len(alias) < 2:
            error_dict['aliasError'] = "Alias must be atleast 2 characters."
            error = True
        
        #Validate email
        if email == '':
            error_dict['emailError'] = "Email can not be blank."
            error = True
        elif not emailRegex.match(email):
            error_dict['emailError'] = "Invalid email address."
            error = True       

        #Check if email already exists in database
        query = "SELECT * FROM users WHERE email=:email and id!=:userId"
        data = {'email':email,
                'userId':id
               }
        user = self.db.query_db(query, data)
        if len(user) > 0:
            error_dict['emailError'] = "Email address already exists."
            error = True

        #Validate password
        if password != '':

            if len(password) < 8:
                error_dict['passwordError'] = "Password must be greater than 8 characters"
                error = True

            elif not passwordRegex.match(password):
                error_dict['passwordError'] = "Password must contain at least one lowercase letter, one uppercase letter, and one digit"
                error = True

            if confirm_password == '':
                error_dict['confirmPasswordError'] = "Confirm Password cannot be blank."
                error = True
            elif confirm_password != password :
                 error_dict['confirmPasswordError'] = "Passwords do not match."
                 error = True
            pw_hash = self.bcrypt.generate_password_hash(password)
            password_update_query = "UPDATE users set password = :password where id = :userId"
            password_data = {'password': pw_hash, 'userId':id}
            self.db.query_db(password_update_query, password_data)     
               

        #Check if there were any errors in the previous validation process
        if error:
            return {"status" : False, "error_dict": error_dict}

        #Add user to database if no errors then return the id for login purposes
        
        update_query = "UPDATE users set first_name =:first_name, last_name=:last_name, alias=:alias, email=:email, updated_at=NOW() where id=:userId"
        print update_query
        data = {'first_name':first_name,
            'last_name':last_name,
            'alias':alias,
            'email':email,
            'userId' :id}
        self.db.query_db(update_query, data)

        query = "SELECT * FROM users where id=:userId"
        data ={'userId': id}
        users = self.db.query_db(query, data)
        return{"status": True, "user": users[0]}

    def get_all_friends (self, id):
        query = "SELECT u.id as friendId, u.alias from friendLists f inner join users u on f.friend_id = u.id where user_id =:userId"
        data ={'userId': id}
        users = self.db.query_db(query,data)   
        return users
    def get_friends (self, id):
        query = "SELECT u.id as friendId, u.alias from friendLists f inner join users u on f.user_id = u.id where friend_id =:userId"
        data ={'userId': id}
        friends = self.db.query_db(query,data)   
        return friends     

    def get_not_friends (self, id):
        query = "select u.alias,u.id as uId from users u where u.id not in(select f.friend_id from friendLists f where f.user_id =:userId) and u.id!=:userId"
        data ={'userId': id}
        not_friend = self.db.query_db(query,data)   
        return not_friend

    def delete_friend (self, friend_id,uId):
        query = "DELETE from friendLists WHERE friend_id =:friend_id and user_id=:uId"
        data = {'friend_id' : friend_id,
                'uId':uId}
        res = self.db.query_db(query, data)
        return res

    def delete (self, uId, friend_id):
        query = "DELETE from friendLists WHERE friend_id =:friend_id and user_id=:uId"
        data = {'friend_id' : uId,
                'uId':friend_id}
        res = self.db.query_db(query, data)
        return res    

    def add_friend (self, friend_id,uId):
        query = "INSERT into friendLists (friend_id, user_id) values(:friend_id,:uId)"
        data = {'friend_id' : friend_id,
                'uId':uId}
        self.db.query_db(query, data)

    def add (self,uId,friend_id):
        query = "INSERT into friendLists (user_id, friend_id) values(:uId,:friend_id)"
        data = {'friend_id' : uId,
                'uId':friend_id}
        self.db.query_db(query, data)    
                 