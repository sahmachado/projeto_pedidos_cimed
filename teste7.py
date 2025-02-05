import pandas as pd
import sqlite3

# Configuração dos arquivos
excel_file = "base teste.xlsx"  # Nome do arquivo Excel
sheet_name = "fornecedores"  # Nome da aba específica no Excel
db_file = "base.db"  # Nome do arquivo do banco de dados SQLite
table_name = "fornecedores"  # Nome da tabela no banco de dados

# Conectar ao SQLite
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Criar a tabela se não existir
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    fornecedor TEXT,
    nome TEXT NOT NULL,
    codigo TEXT,
    email TEXT
);
""")
conn.commit()

# Ler dados do Excel
df = pd.read_excel(excel_file, sheet_name=sheet_name, dtype=str)

# Substituir NaN e espaços vazios por um valor padrão
df = df[['Fornecedor', 'Nome', 'Codigo', 'Email']].copy()  # Garante apenas as colunas necessárias
df.fillna("", inplace=True)  # Substitui NaN por string vazia
df.replace(r'^\s*$', "Desconhecido", regex=True, inplace=True)  # Substitui espaços vazios

# Remover linhas onde 'nome' ainda esteja vazio
df = df[df['Nome'].str.strip() != ""]

# Exibir o DataFrame antes de inserir
print(df.head())

# Inserir dados no banco de dados
df.to_sql(table_name, conn, if_exists='append', index=False)

# Fechar conexão
conn.close()
print("Dados inseridos com sucesso!")