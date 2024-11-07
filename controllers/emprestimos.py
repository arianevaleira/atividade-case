from flask import render_template, Blueprint, url_for, request, flash, redirect
from models.emprestimos import Emprestimos

# módulo de usuários
bp = Blueprint('emprestimos', __name__, url_prefix='/emprestimos')

@bp.route('/')
def index():
    return render_template('emprestimos/index.html', emprestimos = Emprestimos.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        titulo= request.form['titulo']
        data = request.form['data']

        if not email:
            flash('Email é obrigatório')
        else:
            emprestimo = Emprestimos(email, titulo, data)
            emprestimo.save()
            return redirect(url_for('emprestimos.index'))
    
    return render_template('emprestimos/register.html')