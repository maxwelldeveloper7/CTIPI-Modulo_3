""" Importa e inicializa dependências """
import sqlite3
from flask import Flask

app = Flask(__name__)

def conectar_bd():
    """ Cria banco de dados se não existir e retorna conexão"""
    return sqlite3.connect('meu_banco.db')

from app import routes