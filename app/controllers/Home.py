"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import ctypes

class Home(Controller):
    def __init__(self, action):
        super(Home, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('User')
        self.db = self._app.db    
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        if not session.get('userId'):
            session['userId']=''
            session['first_name']=''
            session['last_name']=''
            return redirect('/users/login')

        #user_detail = self.models['User'].get_user(session['userId'])
        friend_details = self.models['User'].get_all_friends(session['userId'])
        #user_details = self.models['User'].get_friends(session['userId'])
        print friend_details
        not_friends = self.models['User'].get_not_friends(session['userId'])
        return self.load_view('/home/index.html', friend_details = friend_details, not_friends =not_friends)