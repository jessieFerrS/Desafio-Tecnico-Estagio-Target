'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. '''

# Dicionario para armazenar os faturamentos mensais por estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36687.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculando o valor total mensal
valor_total_mensal_distribuidora = sum(faturamento_estados.values())

# Calculando e imprimindo os percentuais de cada estado
for estado, valor in faturamento_estados.items():
    percentual = (valor / valor_total_mensal_distribuidora) * 100
    print(f"{estado}: {percentual:.2f}%")
