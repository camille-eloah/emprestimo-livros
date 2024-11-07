from database import get_connection
from flask_login import UserMixin
from werkzeug.security import check_password_hash

class User(UserMixin):
    def __init__(self, nome, email, senha, id=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.id = id 
        
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO users(email, nome, senha) VALUES (?, ?, ?)", (self.email, self.nome, self.senha))
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def all(cls):
        conn = get_connection()
        users = conn.execute("SELECT * FROM users").fetchall()
        conn.close()
        return users
    
    @classmethod
    def find_by_email(cls, email):
        conn = get_connection()
        result = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()
        if result:
            return cls(result['nome'], result['email'], result['senha'], result['id'])
        return None
    
    def check_password(self, senha):
        return check_password_hash(self.senha, senha)

    def get_id(self):
        return str(self.id)  
    
    @classmethod 
    def find(cls, user_id): 
        conn = get_connection()
        result = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        conn.close()
        if result:
            return cls(result['nome'], result['email'], result['senha'], result['id'])
        return None 
    
    def delete(self):
        if self.id is None: 
            raise ValueError("Não foi possível encontrar o ID do usuário.")
        
        conn = get_connection()
        conn.execute("DELETE FROM users WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()
        return True
    
    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False
