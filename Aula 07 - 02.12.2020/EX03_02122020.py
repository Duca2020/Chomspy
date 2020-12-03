#Resolução do exercício 3 do slide 7...

from math import floor

print("\033[0:33mVerificador de números primos\033[m")

try:
    while n:=int(input("Digite um número (ENTER para sair):\n")):
        isprime = True
        for divisor in range(2,floor(n/2)): #Para procurar os fatores, basta ir até a metade do número
            if n%divisor==0:
                isprime=False
                break
        if isprime==True:
            print(f"O número {n} é primo.\n")
        else:
            print(f"O número {n} não é primo.\n")

except:
    pass

