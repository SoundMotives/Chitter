import os
from datetime import datetime
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.post_repository import PostRepository
from lib.user_repository import UserRepository
from lib.post import Post
from lib.user import User

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'mysecretkey123'

# LANDING PAGE
@app.route("/", methods=['GET'])
def load_index_page():
    return render_template('index.html')

# SIGN UP PAGE
@app.route("/signup", methods=["GET", 'POST'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        username = request.form['username']
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        user = User(None, email, password, name, username)
        if not user.is_valid():
            return render_template("signup.html", user=user, errors=user.generate_errors()), 400
        else: 
            repository.create(user)
            return render_template("index.html")
    else:
        return render_template("signup.html")

# SIGN IN PAGE
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print("Request Body of signin:", request.data)
        connection = get_flask_database_connection(app)
        user_repository = UserRepository(connection)
        if user_repository.check_password(email, password):
            print("signin successful")
            user = user_repository.find_by_email(email)
            # Set the user ID in session
            session['user_id'] = user.id
            print(f"app.py(55) Login successful. Session ID:{session['user_id']}")
            post = PostRepository(connection)
            posts = post.all()
            posts.sort(key=lambda post:post.time_post, reverse=True)
            return render_template('home_auth.html', user=user.username, user_repository=user_repository, posts=posts)
        else:
            print("signin not successful")
            return render_template('signin.html', errors="Username and password did not match")
    else:
        print("signin is a get request")
        return render_template('signin.html')

# SIGN OUT PAGE
@app.route("/signout", methods=["GET", "POST"])
def signout():
    # Clear the user_id from the session
    print(f"app.py(68) Session ID:{session['user_id']}")
    session.pop('user_id', None)
    print(f"app.py(70) Session ID has been well and truly popped")
    # Redirect to the root URL or any desired URL after logout
    return redirect('/')

# POSTS PAGE
@app.route("/home", methods=["GET", "POST"])
def load_home():
    if request.method == "POST":
            if session.get('user_id') is not None:
                connection = get_flask_database_connection(app)
                # print(f"Request Body {datetime.now}:", request.data)
                content = request.form.get("content")
                user_id = session["user_id"]
                # username = request.form.get("username")
                user_repository= UserRepository(connection)
                logged_user = user_repository.find(user_id)
                # user_id = user.id

                time_post = datetime.now()
                post = Post(None, content, time_post, user_id)
                print("post successfully created")
                repository = PostRepository(connection)
                repository.create(post)
                print("post successfully added to database")
                posts = repository.all()
                posts.sort(key=lambda post:post.time_post, reverse=True)   
                print("posts successfully requests")
                return render_template("home_auth.html", posts=posts, user_repository=user_repository, user=logged_user.username)
            else:
                return render_template("index.html")
    
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    user_repository = UserRepository(connection)
    posts = repository.all()
    posts.sort(key=lambda post:post.time_post, reverse=True)
    return render_template("home.html", posts=posts, user_repository=user_repository)
# user=logged_user.username

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
