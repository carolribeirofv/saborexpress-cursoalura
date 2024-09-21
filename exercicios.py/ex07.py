# Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input('Digite um número para ver sua tabuada'))
for c in range(1, 11):
   print( f"{numero} x {c} = {numero * c }")
  