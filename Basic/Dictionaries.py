estados = {
    'SP': 'São Paulo',
    'RJ' : 'Rio de Janeiro',
    'MG': 'Minas Gerais'
}

cidades = {
    'São Paulo' : ['Campinas','São Paulo', 'Santo André'],
    'Rio de Janeiro': ['Rio de Janeiro', 'Niterói', 'Petrópolis'],
    'Minas Gerais': ['Belo Horizonte', 'Uberlândia', 'Juiz de Fora']
}


for estado, nome_estado in estados.items():
    print(f"Cidades em {nome_estado}:")
    
    for  cidade in cidades[nome_estado]:
        print(f" - {cidade}")
        
        
        
#Agrupar Pessoa por cidade
pessoas = [
    {'nome': 'João', 'cidade': 'São Paulo'},
    {'nome': 'Maria', 'cidade': 'Rio de Janeiro'},
    {'nome': 'Pedro', 'cidade': 'São Paulo'},
    {'nome': 'Ana', 'cidade': 'Belo Horizonte'},
    {'nome': 'Lucas', 'cidade': 'Rio de Janeiro'}
]

pessoas_por_cidade = {}

for pessoa in pessoas:
    cidade = pessoa['cidade']
    
    if cidade in pessoas_por_cidade:
        pessoas_por_cidade[cidade].append(pessoa['nome'])
    else:
        pessoas_por_cidade[cidade] = [pessoa['nome']]

print('\n')
print(pessoas_por_cidade)