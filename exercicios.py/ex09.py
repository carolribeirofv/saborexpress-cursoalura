import os #biblioteca para fazer a funcionalidade que faz o programar limpar o terminal

def programa():
    try:
        numero = int(input('Digite um número: '))
        print(numero) 

    except ValueError: 
        print('Digite um valor valido')
        input('aperte enter para voltar ao inicio do programa')
        main() #volta ao inicio do programa

    except:
        print('Erro inesperado')
        input('\n Aperte enter para voltar ao inicio do programa')
        main() #volta ao inicio do programa

    finally: #o finally vai sempre aparecer/acontecer independente do programa funcionar ou não 
        print('sempre executa')

 
    


def main():
    os.system('cls') #limpa o terminal
    programa()


if __name__ == '__main__':
    main()