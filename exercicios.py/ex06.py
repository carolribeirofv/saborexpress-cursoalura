# Exercicio: Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for numero in range (1, 11):
    if numero % 2 != 0:
            soma_impares = soma_impares + numero
print('A soma de todos os números impares de 1 a 10 é igual a: {} ' .format(soma_impares))
