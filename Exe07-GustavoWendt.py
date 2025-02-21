#EXE 007 . Escreva um programa que permaneça em laço lendo números inteiros. 
#O laço termina quando for digitado 0 (zero).
#Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
#Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
#Ao final exiba a lista e a quantidade de elementos que ela contém.
numero=-1
numeros=[]
elementos=0
while numero !=0:
    numero=int(input("Digite um número: "))
    if numero not in numeros:
     elementos+=1
     numeros.append(numero)
    else:
       print("Esse número já esta na lista!")
print(numeros)
print("A lista possui {} items: ".format(elementos))
print("Gustavo Wendt")
