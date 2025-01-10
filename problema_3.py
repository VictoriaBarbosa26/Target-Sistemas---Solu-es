# Solução 3

import json

faturamento_json = '''
{
  "faturamento_diario": [1500, 2000, 0, 2300, 1800, 0, 2500, 2200, 0, 2400, 2100, 2200, 0, 2300, 1800, 0, 2500]
}
'''

# Carrega os dados JSON
data = json.loads(faturamento_json)
faturamento_diario = data['faturamento_diario']

# Calcula o menor, maior e a média mensal ignorando os valores 0
faturamento_valido = [f for f in faturamento_diario if f > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)
media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

# Conta os dias que superaram a média
dias_acima_da_media = len([f for f in faturamento_valido if f > media_faturamento])

# Exibe os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias acima da média mensal: {dias_acima_da_media} dias")
