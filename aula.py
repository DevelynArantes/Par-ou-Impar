resposta = 's'     

while resposta == 's':

    nome = int(input("Digite um número par: "))

    if nome % 2 == 0:
        print ("Parabéns! Você acertou")

    else:
        print ("Você errou!")

        resposta = input("Deseja continuar? [s]im ou [n]ao  ").lower()

print("Você saiu do programa")