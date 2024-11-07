from database import get_connection

class Emprestimos:
    def __init__(self, email, titulo, data):
        self.email = email
        self.titulo = titulo
        self.data = data
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO emprestimos(email, titulo, data_eptm) values(?,?,?)", (self.email, self.titulo, self.data,))
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def all(cls):
        conn = get_connection()
        users = conn.execute("SELECT * FROM emprestimos").fetchall()
        return users
    