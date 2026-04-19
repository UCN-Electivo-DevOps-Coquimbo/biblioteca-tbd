class User:
    def __init__(self, id, name, email, password, role, reading_list=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.rol = role
        self.reading_list = reading_list
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}, Password: {self.password}, Role: {self.rol} , Reading list: {self.reading_list}"