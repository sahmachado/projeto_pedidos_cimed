import ttkbootstrap as ttk 
from ttkbootstrap.constants import * 

janela = ttk.Window(title="Minha Aplicação ttkbootstrap", themename="darkly")

botao = ttk.Button(janela, text="Botão Primary", bootstyle=PRIMARY)
botao.pack(pady=5)

botao_sec = ttk.Button(janela, text="Botão Secondary", bootstyle=SECONDARY)
botao_sec.pack(pady=5)

botao_info = ttk.Button(janela, text="Botão Info", bootstyle=INFO)
botao_info.pack(pady=5)

label = ttk.Label(janela, text="Este é um label com ttkbootstrap", font=("Arial", 14))
label.pack()

janela.mainloop()