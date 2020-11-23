#Resolução do exercício 1 do último slide da aula 05
#Trabalharemos com as ferramentas de agilidade disponibilizadas pela singuagem, ainda que apresentem
#grau de dificuldade o(n)

val_escolhidos = []
escolhas = 1
while escolhas < 4:
    try:
        novo_valor = float(input("Digite um número: \n"))
        val_escolhidos.append(novo_valor)
        escolhas += 1

    except ValueError:
       print ("Você não digitou um valor aceitável!\n")

val_organizados = sorted(val_escolhidos)
print(f"\nOs valores escolhidos foram {val_escolhidos[0]}, {val_escolhidos[1]} e {val_escolhidos[2]}.\nEm ordem temos: {val_organizados}")
