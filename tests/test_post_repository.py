from lib.post import Post
from lib.post_repository import PostRepository

from freezegun import freeze_time

def test_gets_all_posts(db_connection):
    with freeze_time("2022-02-01 12:00:00"):
        db_connection.seed("seeds/seeds_users.sql")
        repository = PostRepository(db_connection)

        posts = repository.all()

        assert posts == [
            Post(1, 'Just posting something for lols', "2022-02-01 12:00:00", 1),
            Post(2, 'This is my first post!', "2022-02-01 12:00:00", 2),
        ]

def test_find_for_id_1(db_connection):
    db_connection.seed("seeds/seeds_users.sql")
    repository = PostRepository(db_connection)
    post = repository.find(1)
    assert post == Post(1, 'Just posting something for lols', "2022-02-01 12:00:00", 1)

def test_find_for_id_2(db_connection):
    db_connection.seed("seeds/seeds_users.sql")
    repository = PostRepository(db_connection)
    post = repository.find(2)
    assert post == Post(2, 'This is my first post!', "2022-02-01 12:00:00", 2)

def test_create_a_post(db_connection):
    db_connection.seed("seeds/seeds_users.sql")
    repository = PostRepository(db_connection)
    repository.create(Post(None, 'Im going to say something shocking!', None, 2))
    posts = repository.all()
    assert posts == [
        Post(1, 'Just posting something for lols', "2022-02-01 12:00:00", 1),
        Post(2, 'This is my first post!', "2022-02-01 12:00:00", 2),
        Post(3, 'Im going to say something shocking!', None, 2)
    ]

# def test_update_a_post_password(db_connection):
#     db_connection.seed("seeds/seeds_users.sql")
#     repository = PostRepository(db_connection)
#     repository.update_password(1, "newPass")

#     posts = repository.all()
#     sorted_posts = sorted(posts, key=lambda post: post.id)
#     assert sorted_posts == [
#         Post(1, 'dod@hotmail.com', 'newPass', 'Dave', 'DoD'),
#         Post(2, 'dad@hotmail.com', 'passass123', 'Dad', 'Daddy')]


def test_deleting_post(db_connection):
    db_connection.seed("seeds/seeds_users.sql")
    repository = PostRepository(db_connection)
    repository.delete(2)
    posts = repository.all()
    assert posts == [
        Post(1, 'Just posting something for lols', "2022-02-01 12:00:00", 1),
    ]
    