#Resolução do exercício 2 do slide 7...

from copy import copy

try:
    n=int(input("Digite um número:\n"))
    fatorial=1
    recomeços=copy(n)
    if n>=0:
        while n>1:
            fatorial*=n
            n-=1

        print(f"O fatorial de {recomeços} é {fatorial}.")

    else:
        print("Digite um valor válido!")

except:
    pass
#E se digitar 0????
