import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, Blueprint
from werkzeug.exceptions import abort # to provide 404 page
from . import db
from .models import Books

main = Blueprint('main', __name__)


# def get_db_connection():
#     conn = sqlite3.connect('database.db')
    
#     conn.row_factory = sqlite3.Row
#     return conn

# parse the database for this ID, if not present then return 404 error
def get_book(book_id):
    # conn = get_db_connection()
    
    # book = conn.execute('SELECT * FROM books WHERE id = ?',
    #                     (book_id,)).fetchone()
    book = Books.query.filter_by(id=book_id).first()
    # conn.close()
    if book is None:
        abort(404)
    return book

@main.route('/')
def index():
    books = Books.query.all()

    return render_template('index.html', books=books) # pass the books as an argument to HTML page

@main.route('/<int:book_id>')
def book(book_id):
    book = get_book(book_id)
    return render_template('book.html', book=book)

@main.route('/create', methods=('GET', 'POST'))
def create():
    # conn = get_db_connection()

    if request.method == 'POST':
        option = request.form['option']
        user_input = request.form['thoughts']
    
        if option == 'addNew':
            new_book_title = request.form['newBookTitle']
            # Insert the new book into the database
            new_book = Books(title = new_book_title, pageNumber = 0)

            # add the new user to the database
            db.session.add(new_book)
            db.session.commit()
            # Fetch all books including the new one
            books = Books.query.all()
        else:
            book_id = request.form['book_id']
            # Fetch the existing book's thoughts
            # existing_thoughts = conn.execute('SELECT thoughts FROM books WHERE id = ?', (book_id,)).fetchone()
            existing_book = Books.query.filter_by(id = book_id).first()
            existing_thoughts = existing_book.thoughts
            if existing_thoughts:
                new_thoughts = f"{existing_thoughts[0]}\n{user_input}"
                # conn.execute('UPDATE books SET thoughts = ? WHERE id = ?', (new_thoughts, book_id))
                # conn.commit()
                existing_book.thoughts = existing_thoughts
                db.session.commit()
            #books = conn.execute('SELECT id, title FROM books').fetchall()
            books = Books.query.all()
        # conn.close()
        return render_template('create.html', books=books)
    
    else:
        # books = conn.execute('SELECT * FROM books').fetchall() # get all entries from database
        # conn.close()
        books = Books.query.all()
        return render_template('create.html', books=books)