import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.post_repository import PostRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

@app.route("/", methods=['GET'])
def load_index_page():
    return render_template('index.html')

@app.route("/signup", methods=["GET"])
def load_signup_page():
    return render_template("signup.html")

@app.route("/signup", methods=['POST'])
def submit_signup():
    return render_template("index.html")

@app.route("/signin", methods=['GET'])
def load_signin():
    return render_template("signin.html")

@app.route("/signin", methods=['POST'])
def submit_signin():
    return render_template("home.html")

@app.route("/home", methods=["GET"])
def load_home():
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
