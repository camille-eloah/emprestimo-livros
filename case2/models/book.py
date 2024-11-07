from database import get_connection

class Book:
    def __init__(self, titulo, user_id, id=None):
        self.titulo = titulo
        self.user_id = user_id
        self.book_id = id 

    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO books(titulo, user_id) values(?,?)", (self.titulo, self.user_id))
        conn.commit()
        conn.close()
        return True

    @classmethod
    def all(cls):
        conn = get_connection()
        books = conn.execute("SELECT * FROM books").fetchall()
        return books
    
    @classmethod 
    def get_by_id(cls, book_id): 
        conn = get_connection()
        result = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
        conn.close()

        if result:
            return cls(result['titulo'], result['user_id'], result['id'],)
        return None 
    
    def delete(self):
        if self.book_id is None: 
            raise ValueError("Não foi possível encontrar o ID do livro.")
        
        conn = get_connection()
        conn.execute("DELETE FROM books WHERE id = ?", (self.book_id,))
        conn.commit()
        conn.close()
        return True
    
    def update(self, new_titulo, new_user_id):
        conn = get_connection()
        conn.execute("""
            UPDATE books
            SET titulo = ?, user_id = ?
                     WHERE id = ? 
                     """, (new_titulo, new_user_id, self.book_id))
        conn.commit()
        conn.close()
        return True 
        