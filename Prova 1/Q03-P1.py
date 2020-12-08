#Resolução da 3 questão da prova 1...

from time import sleep
def lista_cont_1():
    contatos_1 = []
    while choice:=str(input("Deseja adicionar um contato?[Y][N]\n")).upper().strip() == "Y":
        novo_contato = str(input("Digite o nome do novo contato a ser adicionado:\n")).capitalize()
        contatos_1.append(novo_contato)

    return contatos_1
#Abre-se a oportunidade de se colocar quantos contatos se queira, inclusive os 10 que são pedidos pela questão

def lista_cont_2():
    contatos_2 = []
    while choice := str(input("Deseja adicionar um contato?[Y][N]\n")).upper().strip() == "Y":
        novo_contato = str(input("Digite o nome do novo contato a ser adicionado:\n")).capitalize()
        contatos_2.append(novo_contato)

    return contatos_2
#Faz-se o mesmo para o segundo usuário

user_1 = lista_cont_1()
print("\n Em seguida para o usuário 2...")
sleep(3)
user_2 = lista_cont_2()
comum = []

for contato in user_1:
    if user_2.count(contato)!=0:
        comum.append(contato)

print(f"Os contatos em comum são {comum}")


"""
#Forma alternativa utilizando o conceito de conjuntos...

from time import sleep
def set_cont_1():
    contatos_1 = set()
    while choice:=str(input("Deseja adicionar um contato?[Y][N]\n")).upper().strip() == "Y":
        novo_contato = str(input("Digite o nome do novo contato a ser adicionado:\n")).capitalize()
        contatos_1.add(novo_contato)

    return contatos_1
#Abre-se a oportunidade de se colocar quantos contatos se queira, inclusive os 10 que são pedidos pela questão

def set_cont_2():
    contatos_2 = set()
    while choice := str(input("Deseja adicionar um contato?[Y][N]\n")).upper().strip() == "Y":
        novo_contato = str(input("Digite o nome do novo contato a ser adicionado:\n")).capitalize()
        contatos_2.add(novo_contato)

    return contatos_2
#Faz-se o mesmo para o segundo usuário

user_1 = set_cont_1()
print("\n  Em seguida para o usuário 2...\n")
sleep(3)
user_2 = set_cont_2()
comum = user_1.intersection(user_2)

print(f"\nOs contatos em comum são {comum}")
"""