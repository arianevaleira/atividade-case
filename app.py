from flask import Flask
from controllers import users, books, emprestimos

app = Flask(__name__)
app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
app.register_blueprint(emprestimos.bp)

