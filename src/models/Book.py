from ..utils import db

class Book(db.Model):
    __tablename__ = "Book"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)

    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author

    def json(self):
        return {'id': self.id, 'name': self.name, 'author': self.author}

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    def save_to_db(self):
        book = Book.query.get(self.id)
        if book:
            book.name = self.name
            book.author = self.author
        else:
            db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
