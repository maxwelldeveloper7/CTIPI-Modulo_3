""" Executa o app"""
from app import app
from app.models import criar_tabela

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
