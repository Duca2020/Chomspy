#Resolução da 1 questão da prova 1...

peso = float(input("Digite o valor do seu peso (Kg):\n"))
altura = float(input("Digite o valor da sua altura (m):\n"))

while peso<=0 or altura <=0:
    print("Valor inacetável, por favor digite novamente!")
    peso = float(input("Digite o valor do seu peso (Kg):\n"))
    altura = float(input("Digite o valor da sua altura (m):\n"))

imc = peso/altura**2

if imc<20.7:
    print(f"Seu IMC é de {imc:.2f}, logo você está abaixo do peso.")
elif 20.7<=imc<26.4:
    print(f"Seu IMC é de {imc:.2f}, logo você está com peso normal")
elif 26.4<=imc<27.8:
    print(f"Seu IMC é de {imc:.2f}, logo você está marginalmente acima do peso")
elif 27.8<=imc<31.1:
    print(f"Seu IMC é de {imc:.2f}, logo você está acima do peso ideal")
else:
    print(f"Seu IMC é de {imc:.2f}, logo você está obeso")
