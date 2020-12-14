#Resolução do exercicio proposto no final do slide 11 da aula do dia 14/12/2020...

numeros = []
while True:
    n=float(input("Digite um número: \n"))
    if n>=0:
        numeros.append(n)
    elif n<0:
        break

C1=list(filter(lambda x: 0<=x<=25, numeros)) #Primeira condição
print(f"\nDos números que você digitou, estão no intervalo [0-25]: {C1}")

C2=list(filter(lambda x: 26<=x<=50, numeros)) #Segunda condição
print(f"\nDos números que você digitou, estão no intervalo [26-50]: {C2}")

C3=list(filter(lambda x: 51<=x<=75, numeros)) #Terceira condição
print(f"\nDos números que você digitou, estão no intervalo [51-75]: {C3}")

C4=list(filter(lambda x: 76<=x<=100, numeros)) #Quarta condição
print(f"\nDos números que você digitou, estão no intervalo [76-100]: {C4}")
