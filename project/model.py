from project import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text(100),nullable = False)


    def __init__(self,title,body):
        self.title = title
        self.body = body