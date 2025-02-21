#EXE 006 - Peça ao usuário para inserir um número entre 15 e 20.
#Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
#Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
#Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado".
numero=-1
while numero <15 or numero >20:
    numero=int(input("Digite um número entre 15 e 20: "))
    
    if numero <15:
     print("Muito baixo: ")

    elif numero >20:
     print("Muito alto: ")

    else:
     print("Muito obrigado")
print("Gustavo Wendt")

