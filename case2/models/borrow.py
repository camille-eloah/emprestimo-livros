from database import get_connection

class Borrow:
    def __init__(self, bor_bk_id, bor_user_id, bor_data_emprestimo):
        self.bor_bk_id = bor_bk_id
        self.bor_user_id = bor_user_id
        self.bor_data_emprestimo = bor_data_emprestimo


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