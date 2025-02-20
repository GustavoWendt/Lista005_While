#EXE 001 . - Faça um programa que leia os números digitados pelo usuario, a cada número digitado ele deve ser somado ao anterior 
# digitado e a cada soma exibida na tela, quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.

soma=0

while soma <50:
   num=float(input("Digite um número: "))
   soma +=num
print(soma)
print("Gustavo Wendt")
