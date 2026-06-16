import sqlite3


class DBProxy:
    # CONSTRUTOR
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name) #conecta no banco de dados
        self.connection.execute('''
                            CREATE TABLE IF NOT EXISTS dados(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                score INTEGER NOT NULL,
                                date TEXT NOT NULL)
                            ''')

    #insere os dados na tabela dados
    def save(self, score_dict: dict):
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()

    #exibe o score em tela dos top 10, em formato de lista
    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    #Fecha a conexão com o banco de dados
    def close(self):
        return self.connection.close()
