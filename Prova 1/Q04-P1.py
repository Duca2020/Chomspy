"""O desenrolar desta questão abrange vários tópicos essenciais de C.S., dentre eles List Comprehension, Conjuntos e
Combinatória, para a primeira parte do problema é interessante saber com quantos casos estamos lidando, para tanto,
lançamos mão do uso de 'combinações' da matemática, pela qual postula-se que para uma escolha em que a ordem das
entidades pode ser desprezada tem-se que C_n,k = n!/((n-k)!*k!), além disso é importante notar que se a ordem não
importa, então basta organizarmos os elementos para que se verifique a existência ou não dele em situações anteriores,
nesse sentido temos..."""

#Resolução da 4 questão da prova 1...
from random import randint
from time import sleep

n=1
sorteados = []
while n<=(10*59*58): #60!/((60-3)!*3!)
    sorteio = [randint(1,60), randint(1,60), randint(1,60)]
    organizado = sorted(sorteio)

    while organizado in sorteados:
        sorteio = [randint(1,60), randint(1,60), randint(1,60)]
        organizado = sorted(sorteio)

    sorteados.append(organizado)
    n+=1

for i in sorted(sorteados):
    print(f"({i[0]},{i[1]},{i[2]})")
sleep(2)
print(f"Foram sorteadas {len(sorteados)} ternas.") #Prova de que todas as 10*59*58 combinações foram feitas.