#Passando Argumentos Simples Posicionais em uma função
def soma(a, b):
    return a + b

print("Soma = ", soma(8, 20))

#Passando argumento nomeados em uma função
def juntar_nomes(sobrenome, nome, meio=""):
    return f"{nome} {meio} {sobrenome}"

nome = juntar_nomes(sobrenome="Tau", nome="Azevedo", meio="Coragem")
print("Nome Completo: ", nome)

#Passando argumentos padrao em uma facao
def calcular_imposto(valor, taxa = 0.1):
    return taxa * valor

resultado1 = calcular_imposto(330000)
resultado2 = calcular_imposto(900000, 0.15)
print("Imposto 1 = ", resultado1, " Imposto 2 = ", resultado2)

#Passar Lista de argumentos variaveis
def imprimir_argumentos(*args):
    for arg in args:
        print(arg)

imprimir_argumentos("Hello", "World", 25, 8.5, False)

#jdbc:postgresql://localhost:5432/estudo 