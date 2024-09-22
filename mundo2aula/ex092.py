from datetime import date

disc = dict()


nome = str(input('Nome: '))
Idade = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de Trabalho (0 nao tem): '))
Contratacao = 0 if ctps == 0 else int(input('Ano de Contratacao: '))

hoje = date.today()
soma_idade = hoje.year - Idade
soma_contribuicao = hoje.year - Contratacao
soma_aposentadoria = (soma_idade + soma_contribuicao + 35) - soma_contribuicao


disc['nome'] = nome
disc['Idade'] = soma_idade
disc['ctps'] = ctps
if ctps != 0:
    disc['Contratacao'] = Contratacao
    disc['aposentadoria'] = soma_aposentadoria

for chaves, valor in disc.items():
    print(f'{chaves} tem valor {valor}')
