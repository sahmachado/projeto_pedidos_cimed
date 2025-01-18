import pandas as pd

num_pedido = 4600073199

base = pd.read_excel('base teste.xlsx')
resultado = base.loc[base['Pedido'] == num_pedido, 'Comprador'].values[0]
print(resultado)