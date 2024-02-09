from lib.user import User

def test_constructs_user():
    user = User(1, "email@email", "securePass123", "Emmy", "EmmyTheGreat")
    assert user.id == 1
    assert user.email == "email@email"
    assert user.password == "securePass123"
    assert user.name == "Emmy"
    assert user.username == "EmmyTheGreat"

def test_users_are_equal():
    user1 = User(1, "email@email", "securePass123", "Emmy", "EmmyTheGreat")
    user2 = User(1, "email@email", "securePass123", "Emmy", "EmmyTheGreat")
    assert user1 == user2

def test_user_is_represented_nicely_as_string():
    user1 = User(1, "email@email", "securePass123", "Emmy", "EmmyTheGreat")
    assert str(user1) == "User(1, email@email, securePass123, Emmy, EmmyTheGreat)"

def test_user_validity():
    assert User(1, "email@email", "securePass123", "Emmy", "EmmyTheGreat").is_valid() == True
    assert User(1, "", "securePass123", "Emmy", "EmmyTheGreat").is_valid() == False
    assert User(1, "email@email", "", "Emmy", "EmmyTheGreat").is_valid() == False
    assert User(1, "email@email", "securePass123", "", "EmmyTheGreat").is_valid() == False
    assert User(1, "email@email", "securePass123", "Emmy", "").is_valid() == False
 
