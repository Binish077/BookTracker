from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    title = db.Column(db.String(100))
    thoughts = db.Column(db.String(1000))
    pageNumber = db.Column(db.Integer)

# CREATE TABLE books (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     beginDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     title TEXT NOT NULL,
#     thoughts TEXT NOT NULL,
#     pageNumber INTEGER
# );