from flask import render_template, Blueprint, url_for, request, flash, redirect
from models.user import User
from database import get_connection

# módulo de usuários
bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/')
def index():
    return render_template('users/index.html', users = User.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nome = request.form['nome']

        if not email:
            flash('Email é obrigatório')
        else:
            user = User(nome, email)
            user.save()
            return redirect(url_for('users.index'))
    
    return render_template('users/register.html')

@bp.route('/delete/<int:user_id>', methods=['POST', 'GET'])
def delete(user_id): 
    user = User.get_by_id(user_id)
    print(user)

    if user:
        conn = get_connection()
        conn.execute("UPDATE books SET user_id = NULL WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()

        user.delete()
        return redirect(url_for('users.index'))
    
    else:
        return redirect(url_for('users.index', mensagem="Usuário não encontrado"))