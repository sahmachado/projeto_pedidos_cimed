import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Criar a janela principal do Tkinter
root = tk.Tk()
root.title("Gráfico de Pedidos Atrasados")
root.geometry("800x600")

# Frame principal onde o gráfico será exibido
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Variáveis globais para armazenar os gráficos
canvas = None
btn_voltar = None

def criar_grafico():
    """Gera um gráfico de pedidos atrasados por comprador e permite clicar para ver detalhes por fornecedor."""
    global canvas, btn_voltar  # Para manipular os widgets globais

    def abrir_grafico_fornecedor(event):
        """Gera um segundo gráfico mostrando os 5 fornecedores com mais pedidos atrasados para o comprador clicado."""
        global canvas, btn_voltar

        # Obter o comprador clicado
        comprador_clicado = compradores[int(event.xdata)]

        # Conectar ao banco de dados
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        # Buscar pedidos atrasados desse comprador agrupados por fornecedor
        cursor.execute("""
            SELECT Fornecedor FROM pedidos WHERE DataRemessa < ? AND Comprador = ?
        """, (data_atual, comprador_clicado))
        
        fornecedores_atrasados = [row[0] for row in cursor.fetchall()]
        conn.close()

        # Verificar se há pedidos atrasados para esse comprador
        if not fornecedores_atrasados:
            messagebox.showinfo("Sem Atrasos", f"{comprador_clicado} não tem pedidos atrasados por fornecedor.")
            return

        # Contar os pedidos atrasados por fornecedor e pegar os 5 maiores
        contagem_fornecedores = Counter(fornecedores_atrasados).most_common(10)

        # Remover gráfico anterior antes de exibir o novo
        limpar_grafico()

        # Criar segundo gráfico (Top 5 Fornecedores com mais pedidos atrasados)
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        
        fornecedores = [item[0] for item in contagem_fornecedores]
        quantidades = [item[1] for item in contagem_fornecedores]

        bars2 = ax2.bar(fornecedores, quantidades, color='orange')
        ax2.bar_label(bars2, padding=5, fmt='%d', fontsize=12)  # Adiciona rótulos nos valores

        ax2.set_title(f'Top 5 Fornecedores em Atraso ({comprador_clicado})')
        ax2.set_xlabel('Fornecedores')
        ax2.set_ylabel('Número de Pedidos Atrasados')
        ax2.set_xticks(range(len(fornecedores)))
        ax2.set_xticklabels(fornecedores, rotation=30, ha="right")
        ax2.grid(axis='y')
        plt.tight_layout()

        # Exibir gráfico no Tkinter
        canvas = FigureCanvasTkAgg(fig2, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.draw()

        # Criar botão de voltar ao gráfico principal
        btn_voltar = ttk.Button(frame, text="Voltar", command=criar_grafico)
        btn_voltar.pack(pady=10)

    def limpar_grafico():
        """Remove o gráfico e o botão 'Voltar', se existirem."""
        global canvas, btn_voltar
        if canvas:
            canvas.get_tk_widget().destroy()
            canvas = None
        if btn_voltar:
            btn_voltar.destroy()
            btn_voltar = None

    # Conectar ao banco de dados
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()

    # Obter a data atual
    data_atual = pd.to_datetime("today").date()

    # Buscar pedidos atrasados no banco
    cursor.execute("SELECT Comprador FROM pedidos WHERE DataRemessa < ?", (data_atual,))
    pedidos_atrasados = [row[0] for row in cursor.fetchall()]
    conn.close()

    # Contar quantos pedidos atrasados cada comprador tem
    contagem = Counter(pedidos_atrasados)

    if not contagem:
        messagebox.showinfo("Sem Atrasos", "Nenhum pedido atrasado encontrado.")
        return

    # Limpar gráfico anterior antes de exibir o novo
    limpar_grafico()

    # Criar primeiro gráfico (Pedidos atrasados por comprador)
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(contagem.keys(), contagem.values(), color='skyblue')
    ax.bar_label(bars, padding=5, fmt='%d', fontsize=12)  # Adiciona rótulos nos valores

    ax.set_title('Pedidos Atrasados por Comprador', fontsize=14)
    ax.set_xlabel('Compradores', fontsize=12)
    ax.set_ylabel('Número de Pedidos Atrasados', fontsize=12)

    ax.set_xticks(range(len(contagem)))
    compradores = list(contagem.keys())
    ax.set_xticklabels(compradores, rotation=30, ha="right")

    ax.grid(axis='y')
    plt.tight_layout()

    # Associar clique no gráfico ao abrir_grafico_fornecedor
    fig.canvas.mpl_connect("button_press_event", abrir_grafico_fornecedor)

    # Exibir gráfico no Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()

# Criar o primeiro gráfico ao iniciar a aplicação
criar_grafico()

# Iniciar o loop da interface
root.mainloop()
