# Solução 5

# Função que inverte uma string
def inverter_string(s):
    resultado = ""
    # Laço 'for' que percorre a string 's' de trás para frente
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

# Solicita ao usuário que digite uma string
texto = input("Digite uma string para inverter: ")

# Chama a função 'inverter_string' passando a string fornecida pelo usuário
# E imprime o resultado (a string invertida)
print("Texto invertido:", inverter_string(texto))
