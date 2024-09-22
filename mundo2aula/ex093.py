
dic = dict()
nome = input('Nome do Jogador: ')
partidas = int(input(f'Quantos partidas {nome} jogou?: '))
lista = []
for gols in range(1, partidas + 1):
    n = int(input('Quantos Gols na partida?: '))
    lista.append(n)
total = sum(lista)
dic['nome'] = nome
dic['gols'] = lista
dic['total'] = total

print('-=' * 20)
print(dic)
print('-=' * 20)

for k, v in dic.items():
    print(f'O Campo {k} tem o valor {v}')
print('-=' * 20)

print(f'O jogador {dic['nome']} jogou {partidas} partidas ')
for a, i in enumerate(lista):
    print(f'     => Na partida {a}, fez {i} gols')

print(f'foi um total de {total} gols')