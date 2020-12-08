#Resolução da 2 questão da prova 1...

def ver_bissexto(ano):
    if ano%4==0 and ano%100!=0 or ano%400==0 and ano%100!=0:
        print(f"O ano {ano} é bissexto.\n")
    else:
        print(f"O ano {ano} não é bissexto.\n")

while n:=str(input("Deseja consultar se um dado ano é bissexto?[Y][N]\n")).upper().strip() == "Y":
    ano = int(input("Digite o ano desejado para consulta:\n"))
    ver_bissexto(ano)

