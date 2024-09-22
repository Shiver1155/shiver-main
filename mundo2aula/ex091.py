from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(0,6),
        'jogador2': randint(0,6),
        'jogador3': randint(0,6),
        'jogador4': randint(0,6)}

ranking = dict()

for k, v in jogo.items():
    print(f'{k} igual {v}')
    #sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=-' * 10)
print('ranking dos jogadores')
for a, i in enumerate(ranking):
    print(f'    {a+1} {i[0]} {i[1]}')
    #sleep(0.5)
print('-=-' * 10)

resultado = ranking[0]
print(f'{resultado[0]} Ganhou')
    