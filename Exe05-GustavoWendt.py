#EXE 005 - Crie uma variável chamada “adivinha” e defina o valor como 50. 
#Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
#Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".
adivinha=50
tentativas=0
palpite=-1
while palpite !=adivinha:
    palpite=int(input("De o seu palpite!: "))
    tentativas+=1
    if palpite <adivinha:
     print("O número é mais alto: ")

    elif palpite >adivinha:
     print("O número é mais baixo: ")

    else:
     print("Parabéns você acertou depois de {} tentativas: ".format(tentativas))
print("Gustavo Wendt")
