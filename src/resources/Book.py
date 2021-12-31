import http
from flask_restful import Resource, reqparse
from http import HTTPStatus

from ..models.Book import Book

parser = reqparse.RequestParser()
parser.add_argument(
            'name',
            type=str,
            help="filter books by name"
        )
parser.add_argument(
    'author',
    type=str,
    help="filter books by author"
)
parser.add_argument(
    'id',
    type=int,
    help="book id"
)


class BookResource(Resource):
    def get(self):
        data = parser.parse_args()
        if (data['name'] != None and data['author'] != None):
            result = Book.query.filter((Book.author==data['author']) & (Book.name==data['name'])).all()   
        elif data['name'] is not None:
            result = Book.query.filter_by(name=data['name']).all()
        elif data['author'] is not None:
            result = Book.query.filter_by(author=data['author']).all()
        else:
            result = Book.query.all()
        return {'books': [book.json() for book in result]}, HTTPStatus.OK


class BookId(Resource):
    def get(self, id):
        return Book.query.get_or_404(id, description="Book doesn't exist in database").json()

    def post(self, id):
        book = Book.query.get(id)
        if book:
            return {'message': "book already exists in database"}, HTTPStatus.FORBIDDEN
        data = parser.parse_args()
        book_obj = Book(id=data.id, name=data.name, author=data.author)
        book_obj.insert_to_db()
        return book_obj.json(), HTTPStatus.CREATED

    def put(self, id):
        data = parser.parse_args()
        book_obj = Book(id=data.id, name=data.name, author=data.author)
        book_obj.save_to_db()
        return book_obj.json(), HTTPStatus.OK
    
    def delete(self, id):
        book_obj = Book.query.get(id)
        book_obj.delete_from_db()
        return book_obj.json(), HTTPStatus.OK