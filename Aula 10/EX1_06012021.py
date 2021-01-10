# Resolução do exercício 1 do slide da aula do dia 06/01/2021...

def reverse_num(numero):
    return int(numero[::-1])

num=str(input('Digite um número:\n'))
print(f'O reverso de {num} é {reverse_num(num)}')
