#Resolução do segundo exercício do último slide da aula 21/12/2020...

def boneco(erros):
    if erros==1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print()
    elif erros==2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|    | ")
        print("|      ")
        print()
    elif erros==3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /| ")
        print("|    | ")
        print("|      ")
        print()
    elif erros==4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\")
        print("|    | ")
        print("|      ")
        print()
    elif erros==5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\")
        print("|    | ")
        print("|   /  ")
        print()

    elif erros==6:
        print("Rest in Peace")

palavras = ['python', 'numpy', 'pandas']
escondidas = [['_','_','_','_','_','_'], ['_','_','_','_','_'], ['_','_','_','_','_','_']]
erros = 0


while pergunta:=(str(input("\nGUESS THE WORD, você quer jogar? (S/N)\n"))).upper() == 'S':
    escolha = int(input("Digite um valor entre 0-2:\n"))
    escolhida = palavras[escolha]
    while erros<6  :
        tentativa = str(input("\nEscolha uma letra\n"))

        for i in range(len(escolhida)):
            if tentativa == escolhida[i]:
                escondidas[escolha][i] = tentativa
        if tentativa not in escondidas[escolha]:
            erros+=1
            if erros<6:
                print(f'Você errou, mas ainda tem {6-erros} chances')
            else:
                print("Você não tem mais tentativas restantes.")
            boneco(erros)
        for i in escondidas[escolha]:
            print(i, end='')
        if '_' not in escondidas[escolha]:
            print('\nParabéns, você acertou a palavra!')
            print()
            break