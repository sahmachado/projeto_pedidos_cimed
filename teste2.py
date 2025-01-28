import pandas as pd
from datetime import datetime

# Ler a base de dados
base = pd.read_excel('base teste.xlsx', dtype={"Data de Remessa": "datetime64[ns]", "Data do Pedido": "datetime64[ns]"})

# Obter a data de hoje
hoje = pd.to_datetime(datetime.today())

fornercedores_fup = []
# Iterar sobre os códigos
for linha, codigo in enumerate(base['Codigo'], start=2):
    # Obter a data de remessa correspondente ao código
    data_remessa = base.loc[base['Codigo'] == codigo, 'Data de Remessa'].values[0]
    
    # Verificar se a diferença em dias é menor ou igual a 10
    if (data_remessa - hoje).days <= 10:
        fornercedores_fup.append(base.loc[base['Codigo'] == codigo, 'Fornecedor'].values[0])
        fornercedores_fup = set(fornercedores_fup)

for fornecedor in fornercedores_fup:
    if base.loc[base['Fornecedor']] == fornecedor:
        pass



# print(set(fornercedores_fup))