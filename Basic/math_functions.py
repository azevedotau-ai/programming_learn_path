#Function para calcular soma entre dois numeros
def soma(a, b):
    return a + b

#Function para calcular subtracao entre dois numeros
def sub(a, b):
    return a - b

#Function para calcular divisao entre dois numeros
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: O Divisor nao pode ser igual a Zero")
    return a / b


#Function para calcular a multiplicacao entre dois numeros
def mult(a, b):
    return a * b


