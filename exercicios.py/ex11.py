pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
nome = input("Digite o nome que você quer verificar se tem no dicionario: ")
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")