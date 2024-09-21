# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
soma = 0
numeros = [12, 56, 31, 93, 75,  24]
for num in numeros:
    try:
        soma = soma + num

    except:
        print('Houve um erro')

print('A soma de todos os números da lista é igual a: {}' .format(soma))