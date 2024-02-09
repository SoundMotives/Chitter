from lib.user import User
# EXAMPLE Table name: users
# Repository class(in lib/user_repository.py)

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    # Selecting all records
    # No arguments
    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            item = User(row["id"], row["email"], row["password"], row["name"], row["username"])
            users.append(item)
        return users
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [id])
        row = rows[0]
        return User(row["id"], row["email"], row["password"], row["name"], row["username"])
        
        pass
        # Executes the SQL query:
        # SELECT id, email, password, name, username FROM users WHERE id = %s;
        # Returns a single User object.

    def create(self, user):
        rows = self._connection.execute("INSERT INTO users (email, password, name, username) VALUES (%s, %s, %s, %s) RETURNING id", [user.email, user.password, user.name, user.username])
        row = rows[0]
        user.id = row["id"] 
        return user 

        # Executes the SQL query:
        # INSERT INTO users (id, email, password, name, username) VALUES (%s, %s, %s, %s), [user.email, user.password, user.name,user.username];

# Returns nothing

    def update_password(self, id, password):
        self._connection.execute("UPDATE users SET password = %s WHERE id = %s", [password, id])

    # Executes the SQL query:
# UPDATE users
# SET email = %s, password = %s, name = %s, username %s WHERE user_id = %s
  
# Returns nothing

    def delete(self, id):
        self._connection.execute("DELETE from users * WHERE id = %s", [id])
pass
    # Executes the SQL query:
    # 
# DELETE FROM users WHERE id = %s, [user_id]

# Returns nothing   