CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS borrowed_books (
    bor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bor_bk_id INTEGER NOT NULL, 
    bor_user_id INTEGER NOT NULL,
    bor_data_emprestimo DATETIME NOT NULL,
    FOREIGN KEY(bor_bk_id) REFERENCES books(id) ON DELETE CASCADE, -- ON DELETE CASCADE: Caso o usuário apague um livro, os empréstimos relacionados a ele serão apagados automaticamente.
    FOREIGN KEY(bor_user_id) REFERENCES users(id)
);
