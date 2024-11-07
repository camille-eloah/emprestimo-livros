from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required
from models.user import User 

auth_bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates/auth')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Redireciona para a rota de login se o usuário não estiver autenticado

@login_manager.user_loader
def load_user(user_id):
    return User.find(user_id)  # Método 'find' no model User para buscar o usuário pelo ID

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    message = None  

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = User.find_by_email(email)

        if user and user.check_password(senha):  
            login_user(user)
            message = 'Login realizado com sucesso!'

            return redirect(url_for('books.index'))  # Redirecionar após o login
        else:
            message = 'Email ou senha incorretos.'


    return render_template('login.html', message=message)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index', message='Você foi deslogado.'))
