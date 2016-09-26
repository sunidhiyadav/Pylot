"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('User')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
	
    def login_form(self):
        print ("in login_form")
        if session['userId'] != '':
            return redirect('/')
        else:
            return self.load_view('/users/index.html')
        
        

    def login(self):
        print ("in login")
        login_info = {
            "email": request.form['email'], 
            "password": request.form['password']
        }
        login_status = self.models['User'].login_user(login_info)

        #Log in the user if user is authenticated
        if login_status['status']:
            session['userId'] = login_status['user']['id']
            session['first_name'] = login_status['user']['first_name']
            session['last_name'] = login_status['user']['last_name']
            print session['last_name']
            return redirect('/')

        if login_status['status'] == False:
            error_dict = login_status['error_dict']
            for key, val in error_dict.items():
                flash(val, key)
            return redirect('/users/login')       


    def register(self):
        register_info = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "alias": request.form['alias'],
            "email": request.form['email'], 
            "password": request.form['password'],
            "confirm_password": request.form['confirm_password']
        }

        register_status = self.models['User'].register(register_info)

        #Flash errors if registration fails
        if register_status['status'] == False:
            error_dict = register_status['error_dict']
            for key, val in error_dict.items():
                flash(val, key)
            return redirect ('/users/login')    

        #Log in the user if user is registered successfully
        else:
            session['userId'] = register_status['user']['id']
            session['first_name'] = register_status['user']['first_name']
            session['last_name'] = register_status['user']['last_name']
            print session['last_name']

            return redirect ('/')
            
    def user_detail(self, id):
       user_detail = self.models['User'].get_user(id)
       return self.load_view('/home/edit.html', user_detail = user_detail)
       
    def edit_user_details(self, id):
        edit_info = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "alias": request.form['alias'],
            "email": request.form['email'], 
            "password": request.form['password'],
            "confirm_password": request.form['confirm_password'],
        }
        
        edit_status = self.models['User'].edit_user_details(edit_info, id)

        if edit_status['status'] == False:
            error_dict = edit_status['error_dict']
            for key, val in error_dict.items():
                flash(val, key)
            return redirect ('/home/edit/'+str(id))    

        else:
            session['userId'] = edit_status['user']['id']
            session['first_name'] = edit_status['user']['first_name']
            session['last_name'] = edit_status  ['user']['last_name']
            return self.load_view('/home/index.html', user_detail = edit_status['user'])    

    def logoff(self):
        session['userId'] = ''
        session['First_name'] = ''
        session['last_name'] = ''
        return redirect ('/')	   