#Resolução do exercício proposto no final do slide 6...

from random import randint
from time import sleep

opcoes=['Pedra','Papel','Tesoura']
print("Vamos jogar jokenpô?\n ...")
sleep(2)
while True:
    escolha_computador = opcoes[randint(0, 2)]
    escolha_usuario = opcoes[int(input("Qual a sua escolha?\n  0-Pedra \n  1-Papel\n  2-Tesoura\n"))]
    sleep(2)
    if escolha_usuario==escolha_computador:
        print(f"Empate. Eu escolhi {escolha_computador} e você também.")

    elif escolha_computador==opcoes[0] and escolha_usuario==opcoes[2] or escolha_computador==opcoes[1] and escolha_usuario==opcoes[0] or escolha_computador==opcoes[2] and escolha_usuario==opcoes[1]:
        print(f"Eu ganhei! Eu escolhi {escolha_computador} e você escolheu {escolha_usuario}.")

    else:
        print(f"Você ganhou! Eu escolhi {escolha_computador} e você escolheu {escolha_usuario}.")

    if revanche:=str(input("Quer jogar de novo?(Y/N)\n")).upper() == 'Y':
        continue
    elif revanche == 'N':
        break
    else:
        print("Comando inválido!")
        raise NameError
