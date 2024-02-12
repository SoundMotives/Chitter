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
    
    def generate_errors(self):
        errors = []
        if self.email == None or self.email == "":
            errors.append("Email can't be blank")
        if self.password == None or self.password == "":
            errors.append("Password name can't be blank")
        if self.name == None or self.name == "":
            errors.append("Name can't be blank")
        if self.username == None or self.username == "":
            errors.append("Username name can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)