import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import date

class PedidoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestão de Pedidos")
        self.geometry("900x600")
        self.configure(bg='#f5f5f5')
        
        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Menu.TButton", padding=(10, 5), width=25, font=("Arial", 10), background='#ffcd00')
        self.style.map("Menu.TButton", background=[("active", "#3883ba"), ("pressed", "#3883ba")])
        self.style.configure("MenuFrame.TFrame", background='#fff')
        self.style.configure("TLabel", background="#fff")
        self.style.configure("TEntry", padding=5)

        # Frame Menu
        self.menu_frame = ttk.Frame(self, width=200, padding=10, style="MenuFrame.TFrame")
        self.menu_frame.grid(row=0, column=0, sticky='ns')
        
        # Carregar Imagem
        try:
            self.logo_image = Image.open("cimed.png").resize((150, 60), Image.LANCZOS)
            self.logo_tk = ImageTk.PhotoImage(self.logo_image)
            ttk.Label(self.menu_frame, image=self.logo_tk).pack(pady=(0, 20))
        except FileNotFoundError:
            print("Logo não encontrado!")
        
        # Frame Conteúdo
        self.content_frame = ttk.Frame(self, padding=20)
        self.content_frame.grid(row=0, column=1, sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Botões do Menu
        botoes_menu = [
            ("Consulta por Pedido", "pedidos"),
            ("Consulta por Item", "consulta"),
            ("Consulta de Fornecedor", "fornecedor"),
            ("Relatório", "relatorio"),
            ("Cadastro de Fornecedor", "cadastro")
        ]

        for texto, pagina in botoes_menu:
            botao = ttk.Button(self.menu_frame, text=texto, style="Menu.TButton", command=lambda p=pagina: self.show_page(p))
            botao.pack(pady=(0, 5))

        self.show_page("pedidos")

    def show_page(self, page):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if page == "pedidos":
            self.page_pedidos()
        elif page == "cadastro":
            self.page_cadastro()
        else:
            ttk.Label(self.content_frame, text=f"Página {page.capitalize()} em construção.", font=("Arial", 16)).pack(pady=20)

    def page_pedidos(self):
        # Configuração de grid para controle de tamanho
        self.content_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Labels e Inputs com controle de largura
        def create_entry(label_text, row, col, width=30):
            ttk.Label(self.content_frame, text=label_text, font=("Arial", 10)).grid(row=row, column=col, sticky="w", padx=5, pady=5)
            entry = ttk.Entry(self.content_frame, width=width)
            entry.grid(row=row, column=col+1, padx=5, pady=5,sticky='w')
            return entry

        self.num_pedido = create_entry("Número do Pedido:", 0, 0, 15)
        self.comprador = create_entry("Comprador:", 0, 2, 25)
        self.fornecedor = create_entry("Fornecedor:", 1, 0, 25)
        
        ttk.Label(self.content_frame, text="Item:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.item_combo = ttk.Combobox(self.content_frame, values=["Item A", "Item B", "Item C"], width=18)
        self.item_combo.grid(row=3, column=1, padx=5, pady=5,sticky='w')
        self.item_combo.current(0)

        self.material = create_entry("Material:", 3, 2, 20)

        self.data_remessa = create_entry("Data de Remessa:", 4, 0, 15)
        self.data_remessa.insert(0, date.today().strftime("%d/%m/%Y"))

        self.status = create_entry("Status:", 5, 0, 15)
        self.follow_up = create_entry("Follow Up:", 5, 2, 25)

        # Botões com espaçamento controlado
        botoes_frame = ttk.Frame(self.content_frame)
        botoes_frame.grid(row=6, column=0, columnspan=4, pady=20)
        
        ttk.Button(botoes_frame, text="Editar", command=self.edit_pedido, width=15).grid(row=0, column=0, padx=10)
        ttk.Button(botoes_frame, text="Salvar", command=self.save_pedido, width=15).grid(row=0, column=1, padx=10)
        ttk.Button(botoes_frame, text="Cancelar", command=self.cancel_pedido, width=15).grid(row=0, column=2, padx=10)
        ttk.Button(botoes_frame, text="Excluir", command=self.delete_pedido, width=15).grid(row=0, column=3, padx=10)

    def page_cadastro(self):
        self.content_frame.grid_columnconfigure((0, 1), weight=1)
        ttk.Label(self.content_frame, text="Nome do Fornecedor:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
        nome_fornecedor = ttk.Entry(self.content_frame, width=25)
        nome_fornecedor.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.content_frame, text="Código SAP:", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5)
        codigo_sap = ttk.Entry(self.content_frame, width=15)
        codigo_sap.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.content_frame, text="E-mail de Contato:", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5)
        email_contato = ttk.Entry(self.content_frame, width=25)
        email_contato.grid(row=2, column=1, padx=5, pady=5)

        botoes_frame = ttk.Frame(self.content_frame)
        botoes_frame.grid(row=3, column=0, columnspan=2, pady=20)

        ttk.Button(botoes_frame, text="Editar", command=self.edit_cadastro, width=15).grid(row=0, column=0, padx=10)
        ttk.Button(botoes_frame, text="Salvar", command=self.save_cadastro, width=15).grid(row=0, column=1, padx=10)
        ttk.Button(botoes_frame, text="Cadastrar", command=self.cadastrar_fornecedor, width=15).grid(row=0, column=2, padx=10)

    # Métodos simulados para ações
    def edit_pedido(self):
        messagebox.showinfo("Editar", "Modo de edição ativado.")

    def save_pedido(self):
        messagebox.showinfo("Salvar", "Pedido salvo com sucesso!")

    def cancel_pedido(self):
        messagebox.showwarning("Cancelar", "Operação cancelada!")

    def delete_pedido(self):
        messagebox.showerror("Excluir", "Pedido excluído!")

    def edit_cadastro(self):
        messagebox.showinfo("Editar", "Modo de edição ativado para cadastro.")

    def save_cadastro(self):
        messagebox.showinfo("Salvar", "Cadastro salvo com sucesso!")

    def cadastrar_fornecedor(self):
        messagebox.showinfo("Cadastrar", "Fornecedor cadastrado!")

if __name__ == "__main__":
    app = PedidoApp()
    app.mainloop()
