#   4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#   • SP – R$67.836,43
#   • RJ – R$36.678,66
#   • MG – R$29.229,88
#   • ES – R$27.165,48
#   • Outros – R$19.849,53

#   Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

# Definindo os valores
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

# Calculando a soma total
SOMA = SP + RJ + MG + ES + Outros

# Calculando e exibindo a representação percentual de cada estado
print(f"O estado de São Paulo teve a representação percentual de {round((SP / SOMA) * 100, 2)}% do valor total mensal da distribuidora.")
print(f"O estado do Rio de Janeiro teve a representação percentual de {round((RJ / SOMA) * 100, 2)}% do valor total mensal da distribuidora.")
print(f"O estado de Minas Gerais teve a representação percentual de {round((MG / SOMA) * 100, 2)}% do valor total mensal da distribuidora.")
print(f"O estado do Espírito Santo teve a representação percentual de {round((ES / SOMA) * 100, 2)}% do valor total mensal da distribuidora.")
print(f"Outros estados tiveram a representação percentual de {round((Outros / SOMA) * 100, 2)}% do valor total mensal da distribuidora.")