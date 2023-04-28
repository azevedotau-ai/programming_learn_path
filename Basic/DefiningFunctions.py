#Function sem argumentos
def cumprimentar():
    print("Hello World !")
    

#Function com argumentos default
def saurdar(nome, message="Hello World"):
    print(message + " , " + nome)
    
#Function com dois argumentos basicos e mais de um returnos
def devidir(a, b):
    quociente = a // b
    resto = a % b
    
    return quociente, resto

#Function recursiva
def factorial(num):
    
    if num == 0:
        return 1
    return num * factorial(num - 1)


#Chamada das functions

cumprimentar()
saurdar("Azevedo")
q, r  = devidir(10, 3)
fat = factorial(8)

print(q, r)
print(fat)