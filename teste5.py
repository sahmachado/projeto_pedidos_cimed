import pandas as pd
from tkinter import Tk, ttk

# Função para carregar os itens do pedido
def carregar_itens(pedido_desejado):
    # Passo 1: Carregar o arquivo Excel
    caminho_arquivo = 'seu_arquivo.xlsx'  # Substitua pelo caminho do seu arquivo
    nome_planilha = 'Plan1'               # Nome da planilha, se necessário
    dados = pd.read_excel(caminho_arquivo, sheet_name=nome_planilha)
    
    # Passo 2: Filtrar pelo pedido desejado
    itens_filtrados = dados[dados['ID_Pedido'] == pedido_desejado]['Item'].tolist()
    return itens_filtrados

# Função para popular a combobox com os itens
def popular_combobox():
    pedido = input_pedido.get()  # Obtém o ID do pedido inserido pelo usuário
    itens = carregar_itens(pedido)
    combobox['values'] = itens  # Adiciona os itens na ComboBox
    if itens:
        combobox.current(0)  # Seleciona o primeiro item por padrão
    else:
        combobox.set('Sem itens encontrados')  # Mostra mensagem caso não haja itens

# Criar a interface Tkinter
root = Tk()
root.title("Itens do Pedido")

# Entrada para ID do pedido
ttk.Label(root, text="ID do Pedido:").grid(row=0, column=0, padx=10, pady=10)
input_pedido = ttk.Entry(root)
input_pedido.grid(row=0, column=1, padx=10, pady=10)

# Botão para carregar itens
botao_carregar = ttk.Button(root, text="Carregar Itens", command=popular_combobox)
botao_carregar.grid(row=0, column=2, padx=10, pady=10)

# ComboBox para mostrar os itens
ttk.Label(root, text="Itens:").grid(row=1, column=0, padx=10, pady=10)
combobox = ttk.Combobox(root, state="readonly", width=30)
combobox.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Iniciar a interface
root.mainloop()
