#Variavel Global
x = 25 # Isso é uma variavel global e pode ser usada em qual parte do programa


#Function com variable local
def minhaFunction():
    y = 10 #Isso é uma função local definida dentro da function
    x = 30
    print("Minha Variavel local: ", y)
    print("Minha Variavel global: ", x)


minhaFunction()    
print(x)    

