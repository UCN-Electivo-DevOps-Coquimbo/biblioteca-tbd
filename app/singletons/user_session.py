from singletons.singleton import Singleton


class UserSession(Singleton):
    initialized = False
    
    def __init__(self, id=None, name: str = "", email: str = "", 
                 password: str = "", rol: str = ""):
        if not UserSession.initialized:
            self.id = id
            self.name = name
            self.email = email
            self.password = password
            self.rol = rol
            UserSession.initialized = True
    
    def logout(self):
        """Reset the user session"""
        self.id = None
        self.name = ""
        self.email = ""
        self.password = ""
        self.rol = ""
        UserSession.initialized = False
        UserSession._instance = None
