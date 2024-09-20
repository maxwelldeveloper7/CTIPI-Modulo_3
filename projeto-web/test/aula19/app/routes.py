"""
Definição de rotas
"""
from flask import render_template, request, redirect, url_for
from app import app, conectar_bd

# Rota para exibir os usuários
@app.route('/')
def listar_usuarios():
    """
    Rota para listar usuários
    """
    with conectar_bd() as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM usuarios')
        usuarios = cur.fetchall()
    return render_template('usuarios.html', usuarios=usuarios)

# Rota para adicionar um novo usuário
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_usuario():
    """
    Rota para adicionar um novo usuário.
    Se a requisição for GET, renderiza o template 'adicionar_usuario.html'.
    Se a requisição for POST, obtém os dados do formulário, insere no banco de dados e redireciona para a rota 'listar_usuarios'.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        with conectar_bd() as con:
            cur = con.cursor()
            cur.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
            con.commit()
        return redirect(url_for('listar_usuarios'))
    return render_template('adicionar.html')
