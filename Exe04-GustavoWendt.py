#EXE 004 - Faça um programa que peça o nome do convidado que o usuário deseja convidar para uma festa. Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem.
#Em seguida, pergunte se ele quer convidar outra pessoa.
#Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa.
convidados=0
nome=input("Digite o nome do convidado(a): ")
convidados+=1
print("O convidado(a) {} foi foi adicionado com sucesso: ".format(nome))
resposta=input("Deseja adicionar mais um convidado(a)? (s/n): ")
while resposta =='s':
 nome=input("Digite o nome do convidado(a): : ")
 print("O convidado(a) {} foi foi adicionado com sucesso: ".format(nome))
 convidados+=1
 resposta=input("Deseja adicionar mais um convidado(a)? (s/n): ")
print("O número total de convidados é: ",convidados)
print("Gustavo Wendt")
