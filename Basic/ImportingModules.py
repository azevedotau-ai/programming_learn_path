import math
import random
import datetime

#Usando a bibliote math para calcular uma raiz quadrada
raiz = math.sqrt(25)
print(raiz)


#Usando a biblioteca random para gerar número alearorios

randomX = random.randint(1,10)
randomY = random.randint(1,10)

print(randomX, " - ", randomY )

#Usando a biblioteca datetime para trabalhar com horario

hoje = datetime.date.today()

print(hoje.strftime("%d-%m-%Y"))