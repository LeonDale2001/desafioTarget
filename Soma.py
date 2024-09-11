#   1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
#   Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
#   Imprimir(SOMA);
#   Ao final do processamento, qual será o valor da variável SOMA?

soma = 0

# Loop para somar os números de 0 a 12
for k in range(13):
    soma += k

# Exibindo o resultado
print(soma)