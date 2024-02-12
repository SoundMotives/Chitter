from datetime import datetime

class Post:
    def __init__(self, id, content, time_post, user_id):
        self.id = id
        self.content = content
        self.time_post = time_post
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"Post({self.id}, {self.content}, {self.time_post}, {self.user_id})"
    
    def is_valid(self):
        if self.content == None or self.content == "":
            return False
        # if self.time_post == None or self.time_post == "":
            # return False
        if self.user_id == None or self.user_id == "":
            return False
        return True
    