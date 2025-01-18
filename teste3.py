import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox

def show_page(page):
    for widget in content_frame.winfo_children():
        widget.destroy()

    if page == "pedidos":
        # Labels e Entradas
        ttk.Label(content_frame, text="Número do Pedido:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        num_pedido = ttk.Entry(content_frame)
        num_pedido.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(content_frame, text="Comprador:", style="TLabel").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        comprador = ttk.Entry(content_frame)
        comprador.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(content_frame, text="Fornecedor:", style="TLabel").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        fornecedor = ttk.Entry(content_frame)
        fornecedor.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(content_frame, text="Item:", style="TLabel").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        itens = ["Item A", "Item B", "Item C"]  # Substitua por seus itens reais
        item_combobox = ttk.Combobox(content_frame, values=itens)
        item_combobox.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(content_frame, text="Material:", style="TLabel").grid(row=4, column=0, padx=5, pady=5, sticky='w')
        material = ttk.Entry(content_frame)
        material.grid(row=4, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(content_frame, text="Data de Remessa:", style="TLabel").grid(row=5, column=0, padx=5, pady=5, sticky='w')
        data_remessa = ttk.Entry(content_frame)  # Pode usar um DateEntry se precisar de um seletor de datas
        data_remessa.grid(row=5, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(content_frame, text="Status:", style="TLabel").grid(row=6, column=0, padx=5, pady=5, sticky='w')
        status = ttk.Entry(content_frame)
        status.grid(row=6, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(content_frame, text="Follow Up:", style="TLabel").grid(row=7, column=0, padx=5, pady=5, sticky='w')
        follow_up = ttk.Entry(content_frame)
        follow_up.grid(row=7, column=1, padx=5, pady=5, sticky='ew')

        # Botões
        ttk.Button(content_frame, text="Editar").grid(row=8, column=0, padx=5, pady=5, sticky='w')
        ttk.Button(content_frame, text="Salvar", command=lambda: salvar_pedido(num_pedido.get(), comprador.get(), fornecedor.get(), item_combobox.get(), material.get(), data_remessa.get(), status.get(), follow_up.get())).grid(row=8, column=1, padx=5, pady=5, sticky='e')
        ttk.Button(content_frame, text="Cancelar").grid(row=9, column=0, padx=5, pady=5, sticky='w')
        ttk.Button(content_frame, text="Excluir").grid(row=9, column=1, padx=5, pady=5, sticky='e')
        for i in range(9):
            content_frame.grid_rowconfigure(i, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)

    elif page == "cadastro":
        ttk.Label(content_frame, text="Nome do Fornecedor:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        nome_fornecedor = ttk.Entry(content_frame)
        nome_fornecedor.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(content_frame, text="Código SAP:", style="TLabel").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        codigo_sap = ttk.Entry(content_frame)
        codigo_sap.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(content_frame, text="Email de Contato:", style="TLabel").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        email_contato = ttk.Entry(content_frame)
        email_contato.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        ttk.Button(content_frame, text="Editar").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        ttk.Button(content_frame, text="Salvar", command=lambda: salvar_fornecedor(nome_fornecedor.get(), codigo_sap.get(), email_contato.get())).grid(row=3, column=1, padx=5, pady=5, sticky='e')
        ttk.Button(content_frame, text="Cadastrar").grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
        content_frame.grid_columnconfigure(1, weight=1)
        for i in range(5):
            content_frame.grid_rowconfigure(i, weight=1)
    else:  # Páginas sem conteúdo específico por enquanto
        ttk.Label(content_frame, text=f"Página de {page.capitalize()}", style="TLabel", font=("Arial", 16)).pack(pady=20)

def salvar_pedido(num_pedido, comprador, fornecedor, item, material, data_remessa, status, follow_up):
    messagebox.showinfo("Pedido Salvo", f"Pedido {num_pedido} salvo com sucesso!")
    print(f"Número do Pedido: {num_pedido}")
    print(f"Comprador: {comprador}")
    print(f"Fornecedor: {fornecedor}")
    print(f"Item: {item}")
    print(f"Material: {material}")
    print(f"Data de remessa: {data_remessa}")
    print(f"Status: {status}")
    print(f"Follow up: {follow_up}")
    # Aqui você adicionaria a lógica para salvar os dados em um banco de dados ou arquivo.

def salvar_fornecedor(nome_fornecedor, codigo_sap, email_contato):
    messagebox.showinfo("Fornecedor Salvo", f"Fornecedor {nome_fornecedor} salvo com sucesso!")
    print(f"Nome do Fornecedor: {nome_fornecedor}")
    print(f"Código SAP: {codigo_sap}")
    print(f"Email de Contato: {email_contato}")

janela = tk.Tk()
janela.title("Pedidos")
janela.geometry("900x600")
janela.configure(bg='#f5f5f5')
style = ttk.Style()

style.theme_use('alt')
style.configure("Menu.TButton", padding=(10, 5), width=20, font=("Arial", 10), background='#ffcd00')
style.map("Menu.TButton", background=[("active", "#3883ba"), ("pressed", "#3883ba")])
style.configure("MenuFrame.TFrame", background='#fff')
style.configure("TLabel", background="#fff")

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
    ("Consulta Por Item", "consulta"),
    ("Consulta de Fornecedor", "fornecedor"),
    ("Relatorio", "relatorio"),
    ("Cadastro de Fornecedor", "cadastro")
]

for texto, pagina in botoes_menu:
    botao = ttk.Button(menu_frame, text=texto, style="Menu.TButton", command=lambda p=pagina: show_page(p))
    botao.pack(pady=(0, 5))

show_page("pedidos")

janela.mainloop()