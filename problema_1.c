// Solução 1

#include <stdio.h>

int main() { // Função principal onde o código será executado
    int INDICE = 13, SOMA = 0, K = 0;
    
    while (K < INDICE) {
        K = K + 1;
        SOMA = SOMA + K;
    }
    
    printf("O valor da soma é: %d\n", SOMA);
    
    return 0; // Finaliza o programa, retornando 0 (indicando que o programa terminou corretamente)
}

// Resultado final 91.