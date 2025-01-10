# Solução 2

# Função para gerar a sequência de Fibonacci até um determinado número
def fibonacci(numero):
    fib = [0, 1]
    while fib[-1] < numero:
        fib.append(fib[-1] + fib[-2])
    return fib

# Função para verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(numero):
    fib = fibonacci(numero)
    if numero in fib:
        return f"O número {numero} pertence à sequência de Fibonacci!"
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci!"

# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número: "))

# Chama a função que verifica se o número pertence à sequência de Fibonacci e imprime o resultado
print(pertence_fibonacci(numero))
