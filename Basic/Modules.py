import datetime

import math_functions
import data_utils

resultadoSoma = math_functions.soma(8, 20)

print("===== Soma =====")
print(resultadoSoma)

data1 = datetime.date(2023, 4, 30)
data2 = datetime.date(2023, 4, 1)
diferenca = data_utils.calcular_diferenca_dias(data1, data2)

print("===== Diferenca Data =====")
print(diferenca, "Dias ") # exibe 29