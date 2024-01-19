import os
import sqlite3

class DataBase:
    def __init__(self, db_file="../data/login_database.db"):
        db_path = os.path.abspath(db_file)
        
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
        '''
        self.cursor.execute(query)
        self.conn.commit()

    def add_user(self, username, password):
        try:
            query = "INSERT INTO users (username, password) VALUES (?, ?)"
            self.cursor.execute(query, (username, password))
            self.conn.commit()
            print(f"Usuário {username} adicionado com sucesso.")
        except sqlite3.IntegrityError:
            print(f"Usuário {username} já existe. Escolha outro nome de usuário.")

    def remove_user(self, username):
        query = "DELETE FROM users WHERE username = ?"
        self.cursor.execute(query, (username,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Usuário {username} removido com sucesso.")
        else:
            print(f"Usuário {username} não encontrado.")

    def verify_login(self, username, password):
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()
        if user:
            print(f"Login bem-sucedido para o usuário {username}.")
            return True
        else:
            print("Login falhou. Verifique seu nome de usuário e senha.")
            return False

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    db = DataBase()

    # Adicionando usuários
    db.add_user("user1", "senha123")
    db.add_user("user2", "senha456")

    # Verificando login
    db.verify_login("user1", "senha123")
    db.verify_login("user1", "senha456")

    # Removendo usuário
    db.remove_user("user2")
    db.remove_user("user3")  # Tentando remover um usuário que não existe

    # Fechando a conexão
    db.close_connection()
