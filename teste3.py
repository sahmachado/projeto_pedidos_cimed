import pandas as pd

base = pd.read_excel('base teste.xlsx')

pedido = 4600055981

itens_pedido = base.loc[base['Pedido'] == pedido, 'Item'].tolist()

pedido = str(pedido)
if pedido[:2] == '45':
    final_pedido = pedido[4:]
elif pedido[:2] == '46':
    final_pedido = pedido[5:]
elif pedido[:2] == '43':
    final_pedido = pedido[6:]
else:
    final_pedido = None  # ou trate o caso em que o pedido não é reconhecido

texto = ''
if final_pedido is not None:
    for item in itens_pedido:
        codigo = f'{final_pedido}{item}'
        material =  base.loc[base['Codigo'] == int(codigo), 'Material']
        texto += f'{pedido}: Item {item} - {material.values[0]}\n'
print(texto)