from flask import Flask
from controllers import users, books, borrowed, routes

app = Flask(__name__)

app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
app.register_blueprint(borrowed.bp)
app.register_blueprint(routes.bp)