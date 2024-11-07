from flask import Flask
from controllers import users, books, borrowed, routes
from auth.bp import auth_bp, login_manager


app = Flask(__name__, template_folder='auth/templates')

app.secret_key = 'CHAVEULTRASECRETA'

app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
app.register_blueprint(borrowed.bp)
app.register_blueprint(routes.bp)
app.register_blueprint(auth_bp)

login_manager.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)