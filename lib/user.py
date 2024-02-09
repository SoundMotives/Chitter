class User:
    def __init__(self, id, email, password, name, username):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.username = username

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"User({self.id}, {self.email}, {self.password}, {self.name}, {self.username})"
    
    def is_valid(self):
        if self.email == None or self.email == "":
            return False
        if self.password == None or self.password == "":
            return False
        if self.name == None or self.name == "":
            return False
        if self.username == None or self.username == "":
            return False
        return True
    