#   3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#   O menor valor de faturamento ocorrido em um dia do mês;
#   O maior valor de faturamento ocorrido em um dia do mês;
#   Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#   IMPORTANTE:
#   a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#   b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# função menor valor
def menor(faturamento):
    menorValor = faturamento[0]['valor']

    for i in faturamento:
        if i['valor'] <= menorValor:
            menorValor = i['valor']
    return menorValor

# função maior valor
def maior(faturamento):
    maiorValor = faturamento[0]['valor']

    for i in faturamento:
        if i['valor'] >= maiorValor:
            maiorValor = i['valor']
    return maiorValor

# função media de faturamento
def media(faturamento):
    somatorio = 0
    for i in faturamento:
        somatorio += i['valor']
    return somatorio/len(faturamento)


# função número de dias maior que a média
def numDiasMaior(faturamento):
    somatorio = 0
    for i in faturamento:
        if i['valor'] > media(faturamento):
            somatorio+=1
    return somatorio

# Lendo arquivo
with open('dados.json', 'r') as file:
    faturamento = json.load(file)


# Exibindo resultados
print("O menor faturamento em um mês foi de: R$" + str(menor(faturamento)))
print("O maior faturamento em um mês foi de: R$" + str(maior(faturamento)))
print("O número de dias em que o faturamento superou a média foi de: " + str(numDiasMaior(faturamento)))
