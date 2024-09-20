""" Define métodos para criação de tabelas"""
from app import conectar_bd

def criar_tabela():
    """ Cria tabela de usuários"""
    with conectar_bd() as con:
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100)
            )
        ''')
        con.commit()
