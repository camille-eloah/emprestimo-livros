from database import get_connection

class User:
    def __init__(self, nome, email, id=None):
        self.nome = nome
        self.email = email
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