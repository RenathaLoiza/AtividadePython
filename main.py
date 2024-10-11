print("Progrma simples")
#Programa simples que solicita um nome para o usuario e faz um calculo para saber sua idade.
nome = input("Digite seu nome? ")
anoDeNascimento = int.Parse(input("Qual seu ano de nascimento"))
anoAtual = int.Parse(input("Qual é o ano atual"))
idade = anoAtual - anoDeNascimento
print(f"Seu nome é {nome}")
print(f"E sua idade é {idade}")