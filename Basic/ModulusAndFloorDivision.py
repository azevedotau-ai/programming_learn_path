numero = 8

if numero % 2 == 0:
    print(f"O numero {numero} é par")
else:
    print(f"O numero {numero} é impar")
    

tempo_em_segundo = 6550
minutos = tempo_em_segundo // 60
segundos = tempo_em_segundo % 60

print(minutos, "Minutos e", segundos, "Segundos")


num = 4
eh_primo = True

for i in range(2, num):
    if num % i == 0:
        eh_primo = False
        break;


if eh_primo:
    print(num,"É primo")
else:
    print(num, "Não é primo")