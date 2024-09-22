
lista = list()
cont = 0
while True:
    dic = dict()
    # cadastro de usuario
    dic['nome'] = nome = str(input('Nome: '))


    while True:
        dic['sexo'] = sexo = str(input('Sexo: ')).upper()
        if sexo in ['M', 'F']:
            break
        else:
            print('Digite apenas [M ou F]. ')
        

    while True:
        try:
            dic['idade'] = idade = int(input('Idade: '))
            dic['idade'] = idade
            break
        except ValueError:
            print('Digite apenas numeros')
    cont += 1
    lista.append(dic)
    # finalizar cadastro
    n = input('Deseja Sair? [S/N]').upper()
    if n == 'S':
        break


soma_idade = sum(pessoa['idade'] for pessoa in lista)
soma_media = soma_idade / len(lista) if lista else 0

print(f'A) Ao todo temos {cont} pessoas cadastradas ')
print(f'B) A media de idade e de {soma_media} anos')

print(f'C) As mulheres cadastradas foram ', end='')
for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print()

print('D) Pessoas com idade acima da média:')
for pessoa in lista:
    if pessoa['idade'] > soma_media:
        print(f"nome {pessoa['nome']}: sexo {pessoa['sexo']}: idade {pessoa['idade']}" )