from database import get_connection

class User:
    def __init__(self, nome, email, senha, id=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.id = id
        
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO users(email, nome) values(?,?)", (self.email, self.nome))
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def all(cls):
        conn = get_connection()
        users = conn.execute("SELECT * FROM users").fetchall()
        return users
    
    @classmethod
    def find_by_email(cls, email):
        # Retorna o usuário pelo email
        conn = get_connection()
        result = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()

        if result:
            return cls(result['nome'], result['email'], result['senha'], result['id'])
        return None
    
    def check_password(self, senha):
        # Comparação da senha fornecida com a senha do usuário (aqui, você deve usar um hash seguro)
        return self.senha == senha  # Em produção, use bcrypt ou uma alternativa segura

    def get_id(self):
        return str(self.user_id)  # O Flask-Login exige que seja uma string    
    @classmethod 
    def get_by_id(cls, user_id): 
        conn = get_connection()
        result = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        conn.close()

        if result:
            return cls(result['nome'], result['email'], result['id'])
        return None 
    
    def delete(self):
        if self.id is None: 
            raise ValueError("Não foi possível encontrar o ID do usuário.")
        
        conn = get_connection()
        conn.execute("DELETE FROM users WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()
        return True