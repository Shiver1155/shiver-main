disc = {'nome' : str(input('Digite um nome')), 'media' : int(input('Digite a media'))}
if disc['media'] < 5:
    disc['situacao'] = 'reprovado'

elif disc['media'] >= 5:
    disc['situacao'] = 'aprovado'

for k, v in disc.items():
    print(f'   -{k} igual {v}')