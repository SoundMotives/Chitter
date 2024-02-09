from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        posts = []
        for row in rows:
            item = Post(row["id"], row["content"], row["time_post"], row["user_id"])
            posts.append(item)
        return posts
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM posts WHERE id = %s", [id])
        row = rows[0]
        return Post(row["id"], row["content"], row["time_post"], row["user_id"])
        
    def create(self, post):
        rows = self._connection.execute("INSERT INTO posts (content, time_post, user_id) VALUES (%s, %s, %s)", [post.content, post.time_post, post.user_id])

    def update_content(self, id, content):
        self._connection.execute("UPDATE posts SET content = %s WHERE id = %s", [content, id])

    def delete(self, id):
        self._connection.execute("DELETE from posts * WHERE id = %s", [id])
