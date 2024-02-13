from lib.user import User
import hashlib

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

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

    def find_by_username(self, username):
        rows = self._connection.execute("SELECT * FROM users WHERE username = %s", [username])
        row = rows[0]
        return User(row["id"], row["email"], row["password"], row["name"], row["username"])
    
    def find_username_by_user_id(self, user_id):
        id = user_id
        rows = self._connection.execute("SELECT username FROM users WHERE id = %s", [id])
        username = rows[0]
        return username
       
    def find_by_email(self, email):
        rows = self._connection.execute("SELECT * FROM users WHERE email = %s", [email])
        row = rows[0]
        return User(row["id"], row["email"], row["password"], row["name"], row["username"])
       
    def create(self, user):
        # password = user.password
        # binary_password = password.encode("utf-8")
        # hashed_password = hashlib.sha256(binary_password).hexdigest()
        """hashed_password"""
        rows = self._connection.execute("INSERT INTO users (email, password, name, username) VALUES (%s, %s, %s, %s) RETURNING id", [user.email, user.password, user.name, user.username])
        row = rows[0]
        user.id = row["id"] 
        return user 

    # def create_hash_pass(self, email, password):
    #     # Hash the password
    #     binary_password = password.encode("utf-8")
    #     hashed_password = hashlib.sha256(binary_password).hexdigest()

    #     # Store the email and hashed password in the database
    #     self._connection.execute(
    #         'INSERT INTO users (email, password) VALUES (%s, %s)',
    #         [email, hashed_password])

    def check_password(self, email, password_attempt):
        # Hash the password attempt
        # binary_password_attempt = password_attempt.encode("utf-8")
        # hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()


        # Check whether there is a user in the database with the given email
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            [email, password_attempt ])
        """hashed_password_attempt"""
        # If that SELECT finds any rows, the password is correct.
        password_correct = len(rows) > 0
        if password_correct:
            print(f"password correct: {password_correct}")
            return password_correct
        # else:
            
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

