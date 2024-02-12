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

@app.route("/", methods=['GET'])
def load_index_page():
    return render_template('index.html')

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


# @app.route("/signin", methods=['GET'])
# def load_signin():
#     return render_template("signin.html")

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
            return render_template('home_auth.html', user=user.username, posts=posts)
        else:
            print("signin not successful")
            return render_template('signin.html', errors="Username and password did not match")
    else:
        print("signin is a get request")
        return render_template('signin.html')
    
@app.route("/signout", methods=["GET", "POST"])
def signout():
    # Clear the user_id from the session
    print(f"app.py(68) Session ID:{session['user_id']}")
    session.pop('user_id', None)
    print(f"app.py(70) Session ID has been well and truly popped")
    # Redirect to the root URL or any desired URL after logout
    return redirect('/')

@app.route("/home", methods=["GET", "POST"])
def load_home():
    if request.method == "POST":
            if session.get('user_id') is not None:
                connection = get_flask_database_connection(app)
                # print(f"Request Body {datetime.now}:", request.data)
                content = request.form.get("content")
                user_id = session["user_id"]
                # username = request.form.get("username")
                user_rep= UserRepository(connection)

                user = user_rep.find(user_id)
                # user_id = user.id

                post = Post(None, content, datetime.now(), user_id)
                print("post successfully created")
                repository = PostRepository(connection)
                repository.create(post)
                print("post successfully added to database")
                posts = repository.all()
                print("posts successfully requests")
                return render_template("home_auth.html", posts=posts, user=user.username)
            else:
                return render_template("index.html")
    
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    posts = repository.all()
    return render_template("home.html", posts=posts)



# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     # We use `render_template` to send the user the file `emoji.html`
#     # But first, it gets processed to look for placeholders like {{ emoji }}
#     # These placeholders are replaced with the values we pass in as arguments
#     return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
