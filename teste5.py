import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para criar e exibir o gráfico
def criar_grafico():
    # Carregar dados (substitua pelo seu arquivo Excel)
    base = pd.read_excel('base teste.xlsx', dtype={"Data de Remessa": "datetime64[ns]"})
    data_atual = pd.to_datetime(datetime.now().date())

    pedidos_atrasados = []

    for index, row in base.iterrows():
        if row['Data de Remessa'] < data_atual:
            pedidos_atrasados.append(row['Comprador'])

    contagem = Counter(pedidos_atrasados)
    
    # Criar gráfico
    compradores = list(contagem.keys())
    quantidades = list(contagem.values())

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(compradores, quantidades, color='skyblue')
    ax.bar_label(bars)
    
    ax.set_title('Contagem de Pedidos Atrasados por Comprador')
    ax.set_xlabel('Compradores')
    ax.set_ylabel('Número de Pedidos Atrasados')
    ax.set_xticklabels(compradores, rotation=45)
    ax.grid(axis='y')

    # Adicionar o gráfico ao tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()

# Configuração da janela tkinter
root = tk.Tk()
root.title("Gráfico de Pedidos Atrasados")

# Frame para o gráfico
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Botão para criar gráfico
criar_grafico()


# Iniciar o loop da interface
root.mainloop()