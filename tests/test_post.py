from lib.post import Post

def test_constructs_post():
    post = Post(1, "This is my post!", "???", 1)
    assert post.id == 1
    assert post.content == "This is my post!"
    assert post.time_post == "???"
    assert post.user_id == 1
    
def test_posts_are_equal():
    post1 = Post(1, "This is my post!", "???", 1)
    post2 = Post(1, "This is my post!", "???", 1)
    assert post1 == post2

def test_post_is_represented_nicely_as_string():
    post1 = Post(1, "This is my post!", "???", 1)
    assert str(post1) == "Post(1, This is my post!, ???, 1)"

def test_post_validity():
    assert Post(1, "This is my post!", "???", 1).is_valid() == True
    assert Post(1, None, "???", 1).is_valid() == False
    # assert Post(1, "This is my post!", None, 1).is_valid() == False
    assert Post(1, "This is my post!", "???", None).is_valid() == False

    

