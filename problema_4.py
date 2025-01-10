# Solução 4

# Dados do faturamento por estado
faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o valor total do faturamento
faturamento_total = sum(faturamento_estado.values())

# Calcula e exibe o percentual de representação de cada estado
for estado, faturamento in faturamento_estado.items():
    percentual = (faturamento / faturamento_total) * 100
    print(f"Percentual de {estado}: {percentual:.2f}%")
