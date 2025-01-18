import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk  # Importe as bibliotecas PIL

root = tk.Tk()

# Frame para o menu lateral
menu_frame = tk.Frame(root, width=200, bg='#ffcd00') # Largura fixa para o menu
menu_frame.grid(row=0, column=0, sticky='ns')

# Frame para o conteúdo principal
content_frame = tk.Frame(root)
content_frame.grid(row=0, column=1, sticky='nsew') # Expande para preencher o resto

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Funções para mostrar as páginas
def show_page(page):
    for widget in content_frame.winfo_children():
        widget.destroy() # Limpa o frame de conteúdo

    if page == "pedidos":
        label = tk.Label(content_frame, text="Conteúdo da página de Pedidos")
        label.pack()
        # Adicione aqui os widgets específicos para a página de pedidos
    elif page == "fornecedor":
        label = tk.Label(content_frame, text="Conteúdo da página de Consulta")
        label.pack()
        # Adicione aqui os widgets específicos para a página de consulta
    # ... outras páginas

try:
    imagem_logo = Image.open("cimed.png")  # Substitua pelo caminho da sua imagem
    imagem_logo = imagem_logo.resize((20, 50), Image.LANCZOS) #Redimensiona a imagem para não ficar muito grande
    imagem_logo = ImageTk.PhotoImage(imagem_logo)
except FileNotFoundError:
    print("Erro: Imagem não encontrada.")
    imagem_logo = None
# Botões do menu
logo_cimed = tk.Image('imagem_logo')

botao_pedidos = tk.Button(menu_frame, text="Consulta Por Pedidos", command=lambda: show_page("pedidos"),width=20)
botao_pedidos.pack(pady=5, padx=10)
botao_fornecedor = tk.Button(menu_frame, text="Consulta Por Fornecedor", command=lambda: show_page("fornecedor"),width=20)
botao_fornecedor.pack(pady=5,padx=10)
# ... outros botões

show_page("pedidos") # Mostra a página inicial
root.update()
root.mainloop()