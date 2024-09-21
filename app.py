import os 

#nessa linha de codigo abaixo temos uma lista de restaurantes que dentro tempos dicionarios, cada dicionario possue informações de um restaurante especifico.
restaurantes = [
                {'nome':'Pizza suprema', 'categoria': 'italiana', 'ativo': False}, 
                {'nome': 'the suhiman', 'categoria': 'japonesa', 'ativo': False},
                {'nome': 'pedaço da bahia', 'categoria': 'baiana', 'ativo': True}] 

def nome_do_programa():
    print('Sabor Express\n')
 #Vamos criar um menu para cadastrar restaurantes nesse app parecido com ifood

def opcoes_do_programa():
    print('1. Cadastrar Resteurante')
    print('2. Listar resteurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n ')

def cadastrar_novo_restaurante():
    os.system('cls')
    exibir_subtitulo('Cadastrando restaurante')
    nome_restaurante = input('Digite o nome do seu restaurante:  ')
    restaurantes.append(nome_restaurante) #essa linha de codigo adiciona o novo nome do restaurante naquela lista de restaurantes.
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}') #aqui o usuario vai escrever o nome da categoria que o restaurante que ele quer cadastrar faz parte.
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria,'ativo': False } #aqui é um dicionario com todas as informações que precisamos sobre o restaurante, no caso os dados do restaurante.
    restaurantes.append(dados_restaurante) #aqui estamos adicionando o dicionario de dados do restaurante dentro da lista de restaurantes.
    print('\nO restaurante {} foi cadastrado com sucesso' .format(nome_restaurante))
    voltar_ao_menu_principal()

def opcao_invalida():
    print('Opção Invalida')
    voltar_ao_menu_principal()

def finalizar_app():
    os.system('cls') #essa biblioteca com essa funcão limpa o terminal, então quando a opção 4 for a escolhida, ele vai mostar a mensagem com o terminal limpo 
    exibir_subtitulo('Finalizando app  ')

def listar_restaurantes():
    os.system('cls')
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'status'}' )
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado' #nessa linha de codigo fizemos que inves de aparecer o nome 'false(desativo)' ou 'true(ativado)' quando peço para listar restaurantes, realmente apareça 'ativado' e 'desativado
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def alternar_estado_do_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False 

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante ['ativo'] = not restaurante ['ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            voltar_ao_menu_principal()

    if not restaurante_encontrado:
        print('o restaurante não foi encontrado')
        voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções acima:'))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
            opcao_invalida()

def main():
    os.system('cls')
    nome_do_programa()
    opcoes_do_programa()
    escolher_opcao()

def voltar_ao_menu_principal(): #essa função faz o usuario voltar ao menu principal cliclando na tecla enter, e toda vez que a gente quiser que essa função aconteça basta colocar onde estamos precisando dela.
    input('\nAperte enter para voltar ao menu principal')
    main()

def exibir_subtitulo(texto): #essa função é usada para exibir um subtitulo, então podemos usar ela e colocar o subtitulo que quisermos em alguma parte.
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    

if __name__ == '__main__':
    main()
