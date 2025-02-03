import pandas as pd
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk

def carregar_planilha(caminho):
    # Carrega a planilha
    df = pd.read_excel(caminho, sheet_name='base')
    return df

def fornecedores_com_follow_up(df):
    # Filtra fornecedores com itens para follow-up dentro do prazo de 10 dias
    df['Data de Remessa'] = pd.to_datetime(df['Data de Remessa'], errors='coerce')
    hoje = datetime.today()
    prazo_limite = hoje + timedelta(days=10)
    df_filtrado = df[(df['Data de Remessa'] <= prazo_limite) & (df['Data de Remessa'] >= hoje)]
    return df_filtrado['Fornecedor'].unique()

janela = tk.Tk()

caminho_arquivo = "base teste.xlsx"
df = carregar_planilha(caminho_arquivo)

fornecedores = fornecedores_com_follow_up(df)
fornecedores = fornecedores.tolist()

forn = ttk.Combobox(janela,values=fornecedores,width=100)
forn.grid(column=0,row=0)

janela.mainloop()