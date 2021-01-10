# Resolução do exercício 2 do slide da aula do dia 06/01/2021...

def describe_num(numero):
    descricao = {}
    for letter in numero:
        descricao[letter] = numero.count(letter)
    return descricao

num = str(input("Digite um número:\n"))
for idx, val in describe_num(num).items():
    print(f'Seu numero apresenta {val} vezes o número {idx}.')