lista = []
while True:
    name = str(input('Enter a name'))
    note1 = int(input('enter a note 1'))
    
    while True:
            if note1 < 0 or note1 > 10:
                print('notas permitido [0 a 10]')
                note1 = int(input('enter a note 1'))
            else:
                break
            
    note2 = int(input('enter a note 2'))
    while True:
        if note2 < 0 or note2 > 10:
            print('notas permitido [0 a 10]')
            note2 = int(input('enter a note 2'))
        else:
            break
            
    media = (note1 + note2) / 2
    lista.append([name, [note1, note2], media])
    
    n = str(input('[S] break')).upper()
    if n == 'S':
        break
        
for i, a in enumerate(lista):
    print(f' {i:<4} {a[0]:<5} {a[2]:>8}')
    
while True:
    n1 = int(input('Digite nota ou 999 para sair'))
    if n1 == 999:
        break
        
    elif n1 <= len(lista):
        print(f'nota de {lista[n1][0]} sao {lista[n1][1]}')