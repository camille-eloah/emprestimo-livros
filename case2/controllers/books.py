from flask import Flask, render_template, url_for, request, Blueprint, redirect
from models.user import User
from models.book import Book
from models.borrow import Borrow

bp = Blueprint('books', __name__, url_prefix='/books')

@bp.route('/')
def index():
    return render_template('books/index.html', books = Book.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        titulo = request.form['titulo']
        user = request.form['user']

        book = Book(titulo, user)
        book.save()
        return redirect(url_for('books.index'))

    return render_template('books/register.html', users=User.all())

@bp.route('/delete/<int:book_id>', methods=['POST', 'GET'])
def delete(book_id): 
    book = Book.get_by_id(book_id)

    if book:
        borrowed_books = Borrow.get_by_book_id(book_id)
        
        if borrowed_books:
            for borrowed_book in borrowed_books:
                borrowed_book.delete()

        book.delete()
        return redirect(url_for('books.index'))
    
    else:
        return redirect(url_for('books.index', mensagem="Livro não encontrado"))
    
@bp.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = Book.get_by_id(book_id)
    if not book:
        return redirect(url_for('books.index', mensagem="Empréstimo não encontrado"))
    
    if request.method == 'POST':
        new_titulo = request.form['titulo']
        new_user_id = request.form['user_id']

        book.update(new_titulo, new_user_id)
        return redirect(url_for('books.index'))
    
    return render_template('books/edit.html', book=book, users=User.all(), books=Book.all())