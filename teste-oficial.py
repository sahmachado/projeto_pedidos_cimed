import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from PIL import Image, ImageTk

itens = ['teste','teste2','teste3']

def pesquisa(num_pedido,comprador):
    num_pedido = int(num_pedido.get())
    base = pd.read_excel('base teste.xlsx')
   
    resultado = base.loc[base['Pedido'] == num_pedido, 'Comprador'].values[0]
    comprador.state = 'normal'
    comprador.delete(0, tk.END)
    comprador.insert(0,resultado)
    comprador.state = 'readonly'    

def editar():
    pass
def save_pedido():
    messagebox.showinfo("Salvar", "Pedido salvo com sucesso!")
def cancel_pedido():
    messagebox.showwarning("Cancelar", "Operação cancelada!")
def delete_pedido():
    messagebox.showerror("Excluir", "Pedido excluído!")

def show_page(page):
    for widget in content_frame.winfo_children():
        widget.destroy()

    if page == "pedidos":

        ttk.Label(content_frame, text='Nº do Pedido', font=("Arial", 11),background='#DCDAD5').grid(row=0, column=0, sticky="w", padx=(15,5), pady=(15, 5))
        num_pedido = ttk.Entry(content_frame, width=25)
        num_pedido.grid(row=0, column=1, padx=5, pady=(15, 5),sticky='w',)

        ttk.Label(content_frame, text='Comprador', font=("Arial", 11),background='#DCDAD5').grid(row=0, column=2, sticky="w", padx=(15,5), pady=(15, 5))
        comprador = ttk.Entry(content_frame, width=25)
        comprador.grid(row=0, column=3, padx=5, pady=(15, 5),sticky='w')

        ttk.Label(content_frame, text='Fornecedor', font=("Arial", 11),background='#DCDAD5').grid(row=1, column=0, sticky="w", padx=(15,5), pady=5)
        fornecedor = ttk.Entry(content_frame, width=40,state="readonly")
        fornecedor.grid(row=1, column=1, padx=5, pady=5,sticky='w')

        ttk.Label(content_frame, text='Item do Pedido', font=("Arial", 11),background='#DCDAD5').grid(row=2, column=0, sticky="w", padx=(15,5), pady=5)
        item_combo = ttk.Combobox(content_frame, values=itens, width=18)
        item_combo.grid(row=2, column=1, padx=5, pady=5,sticky='w')
        item_combo.current(0)

        ttk.Label(content_frame, text='Material', font=("Arial", 11),background='#DCDAD5').grid(row=2, column=2, sticky="w", padx=(15,5), pady=5)
        material = ttk.Entry(content_frame, width=40,state="readonly")
        material.grid(row=2, column=3, padx=5, pady=5,sticky='w')

        ttk.Label(content_frame, text='Data de Remessa', font=("Arial", 11),background='#DCDAD5').grid(row=3, column=0, sticky="w", padx=(15,5), pady=5)
        remessa = ttk.Entry(content_frame, width=20)
        remessa.grid(row=3, column=1, padx=5, pady=5,sticky='w')
        remessa.insert(0, date.today().strftime("%d/%m/%Y"))

        ttk.Label(content_frame, text='Status', font=("Arial", 11),background='#DCDAD5').grid(row=3, column=2, sticky="w", padx=(15,5), pady=5)
        status = ttk.Entry(content_frame, width=20,state="readonly")
        status.grid(row=3, column=3, padx=5, pady=5,sticky='w')

        ttk.Label(content_frame, text='Follow Up', font=("Arial", 11),background='#DCDAD5').grid(row=4, column=0, sticky="w", padx=(15,5), pady=5)
        follow_up = ttk.Entry(content_frame, width=40)
        follow_up.grid(row=4, column=1,columnspan=2, padx=5, pady=5,sticky='w')

        # Botões com espaçamento controlado
        botoes_frame = ttk.Frame(content_frame)
        botoes_frame.grid(row=6, column=0, columnspan=4, pady=20)

        ttk.Button(botoes_frame, text="Pesquisar", command=lambda: pesquisa(num_pedido,comprador), width=15).grid(row=0, column=0, padx=10)
        ttk.Button(botoes_frame, text="Editar", command=editar, width=15).grid(row=0, column=1, padx=10)
        ttk.Button(botoes_frame, text="Salvar", command=save_pedido, width=15,style='s.TButton').grid(row=0, column=2, padx=10)
        ttk.Button(botoes_frame, text="Cancelar", command=cancel_pedido, width=15).grid(row=0, column=3, padx=10)
        ttk.Button(botoes_frame, text="Excluir", command=delete_pedido, width=15).grid(row=0, column=4, padx=10)
    
    elif page == 'atrasados':
        
        for i in range(5):  # 5 colunas no seu exemplo
            content_frame.columnconfigure(i, weight=1)

            ttk.Label(content_frame, text='Pedido', font=("Arial", 11), background='#DCDAD5').grid(row=0, column=0, sticky="ew", padx=(15, 5), pady=(15, 5))
            ttk.Label(content_frame, text='Item', font=("Arial", 11), background='#DCDAD5').grid(row=0, column=1, sticky="ew", padx=(15, 5), pady=(15, 5))
            ttk.Label(content_frame, text='Fornecedor', font=("Arial", 11), background='#DCDAD5').grid(row=0, column=2, sticky="ew", padx=(15, 5), pady=(15, 5))
            ttk.Label(content_frame, text='Comprador', font=("Arial", 11), background='#DCDAD5').grid(row=0, column=3, sticky="ew", padx=(15, 5), pady=(15, 5))
            ttk.Label(content_frame, text='Data de Remessa', font=("Arial", 11), background='#DCDAD5').grid(row=0, column=4, sticky="ew", padx=(15, 5), pady=(15, 5))

    elif page == 'fornecedor':
        pass
    
    elif page == 'realtorio':
        pass
    
    elif page == 'cadastro':
        ttk.Label(content_frame, text='Nome do Fornecedor', font=("Arial", 11),background='#DCDAD5').grid(row=0, column=0, sticky="w", padx=(15,5), pady=(15, 5))
        fornecedor = ttk.Entry(content_frame, width=50)
        fornecedor.grid(row=0, column=1, padx=5, pady=(15, 5),sticky='w',)

        ttk.Label(content_frame, text='Código SAP', font=("Arial", 11),background='#DCDAD5').grid(row=0, column=2, sticky="w", padx=(15,5), pady=(15, 5))
        codigo = ttk.Entry(content_frame, width=20)
        codigo.grid(row=0, column=3, padx=5, pady=(15, 5),sticky='w',)

        ttk.Label(content_frame, text='E-mail Fornecedor', font=("Arial", 11),background='#DCDAD5').grid(row=1, column=0, sticky="w", padx=(15,5), pady=(15, 5))
        email = ttk.Entry(content_frame, width=50)
        email.grid(row=1, column=1, padx=5, pady=(15, 5),sticky='w',)
     
        botoes_frame = ttk.Frame(content_frame)
        botoes_frame.grid(row=6, column=0, columnspan=4, pady=20)

        ttk.Button(botoes_frame, text="Pesquisar", command=lambda: pesquisa(num_pedido,comprador), width=15).grid(row=0, column=0, padx=10)
        ttk.Button(botoes_frame, text="Editar", command=editar, width=15).grid(row=0, column=1, padx=10)
        ttk.Button(botoes_frame, text="Salvar", command=save_pedido, width=15,style='s.TButton').grid(row=0, column=2, padx=10)
        ttk.Button(botoes_frame, text="Cancelar", command=cancel_pedido, width=15).grid(row=0, column=3, padx=10)
        ttk.Button(botoes_frame, text="Excluir", command=delete_pedido, width=15).grid(row=0, column=4, padx=10)
#---------------------------------------------------------------------estrutura da janela---------------------------------------------------------------------#

janela = tk.Tk()
janela.title("Pedidos")
janela.title("Gestão de Pedidos")
janela.geometry("1000x600")
janela.configure(bg='#fff000')
style = ttk.Style()

style.theme_use('clam')
style.configure("Menu.TButton", padding=(10, 5), width=21, font=("Arial", 10), background='#ffcd00')
style.map("Menu.TButton", 
          background=[("active", "#3883ba"), ("pressed", "#3883ba")],
          foreground=[('active', 'white')])

style.configure('s.TButton',background='#7DFF00')
style.map('s.TButton',
          background=[("active", "#178017"), ("pressed", "#178017")],
          foreground=[('active', 'white')])

style.configure("MenuFrame.TFrame", background='#f0f0f0')
style.configure("TLabel", background="#f0f0f0")
style.configure("TEntry", padding=5)
style.configure('C.TFrame', background='#ff0000')

content_frame = ttk.Frame(janela, padding=20,style='C.TFrame')
content_frame.grid(row=0, column=1, sticky='nsew')

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

menu_frame = ttk.Frame(janela, width=200, padding=10, style="MenuFrame.TFrame")
menu_frame.grid(row=0, column=0, sticky='ns')

try:
    logo_image = Image.open("cimed.png")
    logo_image = logo_image.resize((150, 60), Image.LANCZOS)
    logo_tk = ImageTk.PhotoImage(logo_image)
except FileNotFoundError:
    print("Erro: Logo não encontrado.")
    logo_tk = None

if logo_tk:
    logo_label = ttk.Label(menu_frame, image=logo_tk, style="TLabel")
    logo_label.pack(pady=(0, 10))

content_frame = ttk.Frame(janela)
content_frame.grid(row=0, column=1, sticky='nsew')

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

botoes_menu = [
    ("Consulta por Pedido", "pedidos"),
    ("Pedidos Atrasados", "atrasados"),
    ("Consulta Por Fornecedor", "fornecedor"),
    ("Relatorio", "relatorio"),
    ("Cadastro de Fornecedor", "cadastro")
]

for texto, pagina in botoes_menu:
    botao = ttk.Button(menu_frame, text=texto, style="Menu.TButton", command=lambda p=pagina: show_page(p))
    botao.pack(pady=(0, 5))

show_page("pedidos")

janela.mainloop()