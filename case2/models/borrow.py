from database import get_connection

class Borrow:
    def __init__(self, bor_bk_id, bor_user_id, bor_data_emprestimo, bor_id=None):
        self.bor_bk_id = bor_bk_id
        self.bor_user_id = bor_user_id
        self.bor_data_emprestimo = bor_data_emprestimo
        self.bor_id = bor_id 

    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO borrowed_books(bor_bk_id, bor_user_id, bor_data_emprestimo) values(?,?,?)", (self.bor_bk_id, self.bor_user_id, self.bor_data_emprestimo))
        conn.commit()
        conn.close()
        return True

    @classmethod
    def all(cls):
        conn = get_connection()
        borrowed_books = conn.execute("SELECT * FROM borrowed_books").fetchall()
        return borrowed_books
    
    @classmethod 
    def get_by_id(cls, bor_id): 
        conn = get_connection()
        result = conn.execute("SELECT * FROM borrowed_books WHERE bor_id = ?", (bor_id,)).fetchone()
        conn.close()
        if result:
            return cls(result['bor_bk_id'], result['bor_user_id'], result['bor_data_emprestimo'], result['bor_id'])
        return None 
    
    @classmethod
    def get_by_book_id(cls, book_id):
        conn = get_connection()
        borrowed_books = conn.execute("SELECT * FROM borrowed_books WHERE bor_bk_id = ?", (book_id,)).fetchall()
        conn.close()

        for result in borrowed_books:
            return [cls(result['bor_bk_id'], result['bor_user_id'], result['bor_data_emprestimo'], result['bor_id'])]
    
    def delete(self):
        if self.bor_id is None: 
            raise ValueError("Não foi possível encontrar o ID do empréstimo.")
        
        conn = get_connection()
        conn.execute("DELETE FROM borrowed_books WHERE bor_id = ?", (self.bor_id,))
        conn.commit()
        conn.close()
        return True
    
    def update(self, new_bk_id, new_user_id, new_data_emprestimo):
        conn = get_connection()
        conn.execute("""
            UPDATE borrowed_books
            SET bor_bk_id = ?, bor_user_id = ?, bor_data_emprestimo = ?
                     WHERE bor_id = ? 
                     """, (new_bk_id, new_user_id, new_data_emprestimo, self.bor_id))
        conn.commit()
        conn.close()
        return True 
        