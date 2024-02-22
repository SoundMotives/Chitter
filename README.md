# Chitter Twitter Clone

As part of reviewing [Makers' Web Applications In Python](https://github.com/makersacademy/web-applications-in-python/) this is the Chitter challenge in 'Phase 6'. 

Once installed, as a user on Chitter, you can:
- browse posts without signing in (but not post!)
- Sign up to have your own account, allowing you to post yourself
- Login and log out

This project includes hashed passwords and use of session authentication. 

## Setup

```shell

# Clone the repository to your local machine
; git clone https://github.com/SoundMotives/Chitter.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell


# Install the virtual browser we will use for testing
; playwright install

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py
# Now visit http://localhost:5001/ in your browser

```shell
