from flask import Flask, render_template, url_for, request, Blueprint, redirect
from models.user import User
from models.book import Book
from models.borrow import Borrow

bp = Blueprint('borrowed', __name__, url_prefix='/borrowed')

@bp.route('/')
def index():
    return render_template('borrowed/index.html', users=User.all(), books=Book.all(), borrowed_books = Borrow.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():
    
    if request.method == 'POST':
        book_id = request.form['book_id']
        user_id = request.form['user_id']
        data = request.form['data_emprestimo']

        borrowed_book = Borrow(book_id, user_id, data)
        borrowed_book.save()
        return redirect(url_for('borrowed.index'))


    return render_template('borrowed/register.html', users=User.all(), books=Book.all(), borrowed_books=Borrow.all())