import tkinter as tk

def printar_texto(event):
    texto = texto2.get()
    print(texto)

def pesquisa():
    texto = texto1.get()
    texto2.delete(0, tk.END)  # Limpar texto anterior
    texto2.insert(0, texto)

janela = tk.Tk()

texto1 = tk.Entry(janela)
texto1.pack()

texto2 = tk.Entry(janela)
texto2.pack()

# Vamos usar o evento '<<Modified>>' para detectar quando o texto for alterado
texto2.bind('<KeyRelease>', printar_texto)  # Aqui estamos associando a função com o KeyRelease.

botao = tk.Button(text='cliquei aqui', command=pesquisa)
botao.pack()

janela.mainloop()
