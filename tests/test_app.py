from playwright.sync_api import Page, expect

"""
There's the correct header"""

def test_sign_up_header(db_connection, page, test_web_address):
    db_connection.seed("seeds/seeds_users.sql")
    # We load a virtual browser and navigate to the /signup page
    page.goto(f"http://{test_web_address}/signup")

    # We look at all the <li> tags
    header_tags = page.locator("h1")

    # We assert that it has the books in it
    expect(header_tags).to_have_text("Sign Up")


"""
There is a sign up a form
"""
def test_sign_up_form_works(db_connection, page, test_web_address):
    db_connection.seed("seeds/seeds_users.sql")
    # We load a virtual browser and navigate to the /signup page
    page.goto(f"http://{test_web_address}/")
    page.click("text=Sign Up")
    page.fill("input[name='email']", "dave@me.com")
    page.fill("input[name='password']", "hot123")
    page.fill("input[name='name']", "Dave OD")
    page.fill("input[name='username']", "Sound Motives")
    page.click("text=Submit and sign in")

    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Welcome to Chitter")
    # expect(home_title).to_have_text("Welcome Sound Motives")

"""
There is a sign in a form
"""
def test_signin_form_works(db_connection, page, test_web_address):
    db_connection.seed("seeds/seeds_users.sql")
    page.goto(f"http://{test_web_address}/signin")
    page.fill("input[name='email']", "dod@hotmail.com")
    page.fill("input[name='password']", "passass")
    page.click("text=Sign in")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("Sign In")

