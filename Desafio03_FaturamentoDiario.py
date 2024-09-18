'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

import pandas as pd


def analisa_faturamento_diario(arquivo_json):
    """Analisa o faturamento diario de uma distribuidora a partir de um arquivo JSON
    e retorna uma tupla com o menor valor de faturamento não nulo e o maior valor de
    faturamento e os dias em que o faturamento ficou acima da média
    """
    # Lê o arquivo JSON
    df = pd.read_json(arquivo_json)

    # Define a coluna 'dia' como índice
    df.set_index('dia', inplace=True)

    # Verifica o tipo de dado da coluna 'valor' e converte par numérico se necessário
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

    # Remove linhas com valores nulos da coluna 'valor'
    df = df.dropna(subset=['valor'])

    # Remove linha com valor 0 se houver
    df = df[df['valor'] != 0]

    # Calcula a média mensal
    media_mensal = df['valor'].mean()

    # Encontra o maior e o menor valor
    menor_valor = df['valor'].min()
    maior_valor = df['valor'].max()

    #Conta os dias acima da média(conta o numero de "Trues" retornados)
    dias_acima_media = (df['valor'] > media_mensal).sum()

    return menor_valor, maior_valor, media_mensal, dias_acima_media


# Aplicando a Função:
arquivo = 'dados.json'
menor, maior, media, dias_acima = analisa_faturamento_diario(arquivo)

print("--" * 30)
print('$$  A N A L I S E  D E  F A T U R A M E N T O  $$'.center(60))
print("--" * 30)
print(f"Menor valor diário no mês: R$ {menor:.2f}")
print(f"Maior valor diário no mês: R$ {maior:.2f}")
print(f"Média Mensal: R$ {media:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima}")
print("--" * 30)
