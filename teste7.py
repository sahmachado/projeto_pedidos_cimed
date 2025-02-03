import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite
conn = sqlite3.connect("base.db")

# Executar uma consulta SQL (exemplo: filtrar pedidos da categoria "Eletrônicos")
query = "SELECT * FROM pedidos WHERE Comprador = 'Leonardo'"
df_resultado = pd.read_sql_query(query, conn)

# Fechar conexão
conn.close()

# Exibir os resultados
print(df_resultado)
