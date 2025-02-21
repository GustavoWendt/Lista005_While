#EXE 003 - Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
#Depois que o loop for interrompido, exiba o total.
num1=float(input("Digite um número: "))
num2=float(input("Digite um número: "))
soma=num1+num2
print("A soma desses dois númeroa é: ", soma)
resposta=input("Deseja adicionar mais um número a soma?(s/n): ")
while resposta =='s':
 num=float(input("Digite um número: "))
 soma+=num
 resposta=input("Deseja adicionar mais um número a soma?(s/n): ")
print("A soma dos números é: ",soma)
print("Gustavo Wendt")
