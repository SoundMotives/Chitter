from playwright.sync_api import Page, expect

"""
Testing the landing page
"""
def test_index_header(db_connection, page, test_web_address):
    db_connection.seed("seeds/seeds_users.sql")
    # We load a virtual browser and navigate to the / page
    page.goto(f"http://{test_web_address}/")

    # We look at all the <h1> tags
    header_tags = page.locator("h1")

    # We assert that it has the title in it
    expect(header_tags).to_have_text("Welcome to Chitter")

"""
Testing the landing page buttons / links
"""

def test_index_buttons(db_connection, page, test_web_address):
    db_connection.seed("seeds/seeds_users.sql")
    # We load a virtual browser and navigate to the / page
    page.goto(f"http://{test_web_address}/")

    # We look at all the <h1> tags
    button_tags = page.locator("button")

    # We assert that it has the title in it
    expect(button_tags).to_have_text(["Sign Up", "Sign In", "Browse As A Guest"])

