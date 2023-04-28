import argparse

parser = argparse.ArgumentParser(description="Meu Programa")
parser.add_argument("--nome", required=True, help="Nome Pessoa")
parser.add_argument("--idade", required=True, type=int, help="Tua Idade")
parser.add_argument("--endereco", help="Endereço Do User")

args = parser.parse_args()

print(f"Meu Nome: {args.nome}")
print(f"Minha Idade: {args.nome}")

if args.endereco:
    print(f"Endereço: {args.endereco}")