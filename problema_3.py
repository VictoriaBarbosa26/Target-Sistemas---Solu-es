import json
import xml.etree.ElementTree as ET

# Função para carregar os dados do JSON
def carregar_dados_json():
    with open('dados.json', 'r') as file:  # Nome do arquivo JSON na mesma pasta
        return json.load(file)

# Função para carregar os dados do XML
def carregar_dados_xml():
    tree = ET.parse('dados(2).xml')  # Nome do arquivo XML na mesma pasta
    root = tree.getroot()
    return [{"dia": int(row.find("dia").text), "valor": float(row.find("valor").text)} for row in root.findall("row")]

# Função para calcular as métricas de faturamento
def calcular_metricas(faturamento_diario):
    # Filtra os valores de faturamento válidos (maiores que 0)
    faturamento_valido = [f['valor'] for f in faturamento_diario if f['valor'] > 0]

    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    # Calcula a média de faturamento
    media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

    # Conta os dias com faturamento superior à média
    dias_acima_da_media = len([f for f in faturamento_valido if f > media_faturamento])

    return menor_faturamento, maior_faturamento, media_faturamento, dias_acima_da_media

# Carregar os dados (JSON ou XML)
faturamento_diario_json = carregar_dados_json()
faturamento_diario_xml = carregar_dados_xml()

# Calcular as métricas para os dados JSON
menor_faturamento_json, maior_faturamento_json, media_faturamento_json, dias_acima_da_media_json = calcular_metricas(faturamento_diario_json)
print(f"Resultado para dados.json:")
print(f"Menor faturamento: R${menor_faturamento_json:.2f}")
print(f"Maior faturamento: R${maior_faturamento_json:.2f}")
print(f"Dias acima da média mensal: {dias_acima_da_media_json} dias")

# Calcular as métricas para os dados XML
menor_faturamento_xml, maior_faturamento_xml, media_faturamento_xml, dias_acima_da_media_xml = calcular_metricas(faturamento_diario_xml)
print(f"\nResultado para dados(2).xml:")
print(f"Menor faturamento: R${menor_faturamento_xml:.2f}")
print(f"Maior faturamento: R${maior_faturamento_xml:.2f}")
print(f"Dias acima da média mensal: {dias_acima_da_media_xml} dias")
