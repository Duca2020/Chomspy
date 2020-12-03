#Resolução do exercício 1 do slide 7...
#Serão utilizadas ferramentas trabalhadas e outras que dialogam com o conteúdo...
#OBS: Escolher valor alfabetico ou 0 leva a considerações não numéricas

somatorio=0
quantidadade=0
try:
    while n:=float(input("Digite um valor (ENTER para sair):\n")):
        somatorio+=n
        quantidadade+=1
except:
    pass

media=somatorio/(quantidadade)
print(f"A media dos valores que você digitou é {media}.")



"""
somatorio=[]
try:
    while n:=float(input("Digite um valor (0 para sair):\n")):
        somatorio.append(n)
except:
    pass

media=sum(somatorio)/len(somatorio)
print(f"A media dos valores que você digitou é {media}.")
"""
