#Ressolução do exercício 2 do último slide da aula 05
#Aqui iremos apresentar de acordo com os recursos apresentados em aula,
#sem deixar de trazer algumas novidade

valores = []
while (n:=len(valores) < 3):
    try:
        novo_valor = float(input("Digite um valor: \n"))
        if novo_valor not in valores:
            valores.append(novo_valor)

        else:
            print("Digite um valor diferente!\n")

    except ValueError:
       print ("Você não digitou um valor aceitável!\n")

maior = valores[0]
menor = valores[0] #Ambas atribuições foram arbitrárias
outro = valores[0]
for num in valores:
    if num > maior:
        maior = num

    elif num < menor:
        menor = num

    elif num is not maior or num is not menor:
        outro = num

val_decrescentes = [maior, outro, menor]
print(f"Os valores escolhidos foram {valores[0]}, {valores[1]}, {valores[2]}.\nEm ordem decrescente temos {val_decrescentes}")
#A função sorted() poderia ter sido usada com argumento reverse = True
