import tkinter as tk

def processar_entrada(event):
    texto = entrada.get()
    print(f"Texto digitado (Enter pressionado): {texto}")
    # Aqui você pode adicionar o código para processar a entrada,
    # como salvar em um arquivo, enviar para um banco de dados, etc.

janela = tk.Tk()
janela.title("Exemplo de Evento <Return>")

entrada = tk.Entry(janela)
entrada.bind("<Return>", processar_entrada)  # Associa o evento <Return> à função
entrada.pack(padx=10, pady=10)
entrada.focus_set() #Coloca o foco na entry automaticamente

mensagem = tk.Label(janela, text="Digite algo e pressione Enter:")
mensagem.pack()

janela.mainloop()