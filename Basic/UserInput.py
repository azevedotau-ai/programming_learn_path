import sys
import argparse

#User Input Usando a Funcao input
nome = input("Digite o Teu Nome: ")

#User input usando a biblioteca sys
print("Digite a tua Idade: ")
idade = sys.stdin.readline()

#User input usando NamedArgument
parser = argparse.ArgumentParser()
parser.add_argument("endereco", help="")
args = parser.parse_args()


print(f"Ola {nome} a tua idade é: {idade} e teu Endereço é :{args.endereco}")