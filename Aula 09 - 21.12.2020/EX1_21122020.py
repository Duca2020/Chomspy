#Resolução do primeiro exercício do último slide da aula do dia 21/12/2020...

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho','Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

try:
    dados = str(input("Digite sua data de nascimento (dd/mm/aaaa):\n")).split('/')
    if dados[0].isnumeric() and dados[1].isnumeric() and dados[2].isnumeric():
        print(f"Você nasceu em {dados[0]} de {meses[int(dados[1])-1]} de {dados[2]}")
except:
    print("Erro, tente novamente!")
