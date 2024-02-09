from lib.user import User
from lib.user_repository import UserRepository

def test_gets_all_users(db_connection):
    db_connection.seed("seeds/seeds_users.sql")
    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == [
        User(1, 'dod@hotmail.com', 'passass', 'Dave', 'DoD'),
        User(2, 'dad@hotmail.com', 'passass123', 'Dad', 'Daddy'),
    ]

def test_find_for_id_1(db_connection):
    db_connection.seed("seeds/seeds_users.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    assert user == User(1, 'dod@hotmail.com', 'passass', 'Dave', 'DoD')

def test_find_for_id_2(db_connection):
    db_connection.seed("seeds/seeds_users.sql")
    repository = UserRepository(db_connection)
    user = repository.find(2)
    assert user == User(2, 'dad@hotmail.com', 'passass123', 'Dad', 'Daddy')

def test_create_a_user(db_connection):
    db_connection.seed("seeds/seeds_users.sql")
    repository = UserRepository(db_connection)
    created_user = repository.create(User(None, "me@me.com", "hot123", "Dave", "It's me!"))
    assert created_user == User(3, "me@me.com", "hot123", "Dave", "It's me!")

    users = repository.all()
    assert users == [
        User(1, 'dod@hotmail.com', 'passass', 'Dave', 'DoD'),
        User(2, 'dad@hotmail.com', 'passass123', 'Dad', 'Daddy'),
        User(3, "me@me.com", "hot123", "Dave", "It's me!")
    ]

def test_update_a_user_password(db_connection):
    db_connection.seed("seeds/seeds_users.sql")
    repository = UserRepository(db_connection)
    repository.update_password(1, "newPass")

    users = repository.all()
    sorted_users = sorted(users, key=lambda user: user.id)
    assert sorted_users == [
        User(1, 'dod@hotmail.com', 'newPass', 'Dave', 'DoD'),
        User(2, 'dad@hotmail.com', 'passass123', 'Dad', 'Daddy')]


def test_deleting_user(db_connection):
    db_connection.seed("seeds/seeds_users.sql")
    repository = UserRepository(db_connection)
    repository.delete(2)
    users = repository.all()
    assert users == [
        User(1, 'dod@hotmail.com', 'passass', 'Dave', 'DoD')
    ]
    