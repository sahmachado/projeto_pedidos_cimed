import pandas as pd
from datetime import datetime, timedelta

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

def filtrar_materiais_por_fornecedor(df, fornecedor):
    # Filtra os materiais com base no fornecedor selecionado e prazo de entrega
    df['Data de Remessa'] = pd.to_datetime(df['Data de Remessa'], errors='coerce')
    hoje = datetime.today()
    prazo_limite = hoje + timedelta(days=10)
    df_filtrado = df[(df['Fornecedor'] == fornecedor) & (df['Data de Remessa'] <= prazo_limite) & (df['Data de Remessa'] >= hoje)]
    return df_filtrado

def gerar_texto_follow_up(df_filtrado):
    texto = ""
    for _, row in df_filtrado.iterrows():
        pedido = row['Pedido']
        item = row['Item']
        material = row['Material']
        texto += f'{pedido}: Item {item} - {material}\n'
    return texto

if __name__ == "__main__":
    caminho_arquivo = "base teste.xlsx"
    df = carregar_planilha(caminho_arquivo)
    
    fornecedores = fornecedores_com_follow_up(df)
    print("Fornecedores com itens para follow-up:")
    for fornecedor in fornecedores:
        print(fornecedor)
    
    fornecedor_desejado = input("Digite o nome do fornecedor para ver os materiais: ")
    df_filtrado = filtrar_materiais_por_fornecedor(df, fornecedor_desejado)
    
    if df_filtrado.empty:
        print("Nenhum material encontrado para follow-up deste fornecedor.")
    else:
        texto_final = gerar_texto_follow_up(df_filtrado)
        print("Materiais para follow-up:\n")
        print(texto_final)
