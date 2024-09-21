meus_dados = {"Nome": "Manuela Carolina", "idade": "18", "Cidade": "Salvador"} #Essa é uma lista com alguns dos meus dados.

meus_dados["Curso"] = "Engenharia de software" #para adicionar mais informações em um dicionario n podemos usar o append como usamos na lista então para adiconar o curso que eu estudo eu tive que fazer isso que esta na linha de codigo acima, coloquei o nome do dicionario, dentro do colchetes eu coloco a chave(key) que quero adicionar, a chave é como se fosse a categoria, que nesse caso é "curso", e o  valor que vai ter dentro dessa categoria é "engenharia de software"
print(meus_dados)

del meus_dados["Cidade"] #Dessa forma que deletamos uma chave(key) de um dicionario, nesse caso eu quis deletar a categoria "cidade" que é uma key
print(meus_dados)

meus_dados.update({"idade": "19"}) #Nessa linha de codigo eu atualizei um valor de uma chave(key), eu quia alterar minha idade então fiz isso.
print(meus_dados)