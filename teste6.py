import sqlite3
import pandas as pd

# Nome do banco de dados
db_name = "base.db"

# Criando conexão com o banco de dados SQLite
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Criando a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        Codigo INTEGER PRIMARY KEY,
        Pedido TEXT,
        DataPedido DATE,
        Item TEXT,
        Material TEXT,
        Categoria TEXT,
        Comprador TEXT,
        DataRemessa DATE,
        Fornecedor TEXT,
        Followup TEXT
    )
''')

conn.commit()

# Nome do arquivo Excel (certifique-se de que ele esteja no mesmo diretório do script)
excel_file = "Pasta1.xlsx"

# Carregando os dados do Excel para um DataFrame do Pandas
df = pd.read_excel(excel_file)

# Inserindo os dados na tabela do SQLite
df.to_sql('pedidos', conn, if_exists='append', index=False)

# Fechando a conexão
conn.close()

print("Banco de dados criado e dados carregados com sucesso!")
