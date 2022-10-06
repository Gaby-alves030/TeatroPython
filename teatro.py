teatro = []
for i in range(20):
    teatro.append([])
    for j in range(20):
        teatro[i].append('N')

vals = {'L':0, 'R':0, 'C':0}
ini = False
pNum = -1
preco = 0
tot = 0
perc = 0
lin = 0
cNum = 0
cadLin = 0
cadCol = 0

def reset():
    global teatro, vals, ini, pNum, preco, tot, perc, lin, cNum

    teatro = []
    for i in range(20):
        teatro.append([])
        for j in range(20):
            teatro[i].append('N')

    vals = {'L':0, 'R':0, 'C':0}
    ini = False
    pNum = -1
    preco = 0
    tot = 0
    perc = 0
    lin = 0
    cNum = 0
    cadLin = 0
    cadCol = 0

def calcCad():
    global teatro, vals, tot, perc

    for i in teatro:
        if i[0] == 'N':
            continue

        for j in i:
            if j == 'N':
                continue

            vals[j] += 1
    
    perc = (((vals["R"] + vals["C"]) / (vals["L"] + vals["R"] + vals["C"])) * 100)

    print(f'\nCadeiras livres: {vals["L"]} | Cadeiras reservada: {vals["R"]} | Cadeiras compradas {vals["C"]}')
    print(f'Total arrecadado:R${tot:.2f} | Porcentagem do teatro ocupada: {perc:.0f}%')


def encerrar():
    global perc

    if perc > 50:
        conf = int(input(f"""\nO teatro já está com mais de 50% de lotação.
Deseja encerrar a venda de ingreços? [1-sim] [2-não]
R: """))
        if conf == 1:
            calcCad()
            print('\nEncerrando peça')
            reset()
        else:
            print('Cancelando')
    else:
        input(f"""\nNão é possivel encerrar a peça agora, pois o teatro está apenas com {perc:.0f}% de lotação, então não atingiu a lotação minima de 50%.
Digite qualquer coisa para continuar: """)

def parcial():
    global preco
    calcCad()
    print(f'\nPreço de reserva: {preco * 0.3}, preco total: {preco}')
    input('\nDigite qualquer coisa para continuar: ')

def select(func):
    global cadLin, cadCol, lin, teatro, cNum

    cadLin = 0
    cadCol = 0

    while cadLin == 0:
        cadLin = int(input(f'\nQual o número da linha da cadeira que você deseja {func}: '))
        if cadLin > lin:
            print(f'número inválido, insira um número de 1 a {lin}')
            continue

    printTeatro(False, cadLin)

    while cadCol == 0:
        cadCol = int(input(f'\nQual o número da cadeira que você deseja {func}: '))
        if cadCol > cNum // lin + (1 if cadLin < cNum % lin else 0):
            print(f'número inválido, insira um número de 1 a {cNum // lin + (1 if cadLin < cNum % lin else 0)}')
            continue
    
    if teatro[cadLin - 1][cadCol - 1] == 'C':
        C()
    else:
        R = teatro[cadLin - 1][cadCol - 1] == 'R'
        exec(f'{func}({R})')
        
def printTeatro(conf = False, lin = -1):
    global teatro, perc

    linp = 0

    print('\n   \t', end='')
    for i in range(1, len(teatro[0]) + 1):
        if teatro[0][i - 1] == 'N':
            continue

        print((' '  if i < 10 else '') + f'{i}', end=' ')

    print('')
    for i in teatro:
        if i[0] == 'N':
            continue

        linp += 1
        if linp != lin and lin != -1:
            continue

        print(f'{linp}:\t', end='')
        for j in i:
            if j == 'N':
                continue
            print('|' + j, end='|')
        print('')
    print('L - livre, R - reservada, C - comprada')
    if conf:
        input('\nDigite qualquer coisa para continuar: ')

def C():
    input("""\nInfelizmente a cadeira que você solicitou está comprada >_<.
Digite qualquer coisa para continuar: """)

def reservar(reser):
    global tot, teatro, cadLin, cadCol, preco

    if reser:
        input(f"""\nEita O_O, parece que está cadeira já está reservada.
Digite qualquer coisa para continuar: """)
        return 0

    conf = int(input(f"""\nIsso lhe custara 30% do preço do ingreço (R${(preco * 0.3):.2f})
Tem certeza que deseja reservar essa cadeira?.
[1-sim] [2-não]
R: """))

    if conf == 1:
        teatro[cadLin - 1][cadCol - 1] = 'R'
        print('\nCadeira reservada com sucesso')
        tot += preco * 0.3
    else:
        print('\nCancelando')

def comprar(reser):
    global tot, teatro, cadLin, cadCol, preco

    if reser:
        txt = f"""\nOlha só (◕.◕), parece que este lugar já estava reservado ^_^, então isso só lhe custara 70% de um ingreço (R${(preco * 0.7):.2f}) \o/
Tem certeza que deseja comprar essa cadeira?.
[1-sim] [2-não]
R: """
        tot += preco * 0.7
    else:
        txt = f"""\nIsso lhe custara um ingreço (R${preco:.2f})
Tem certeza que deseja comprar essa cadeira?.
[1-sim] [2-não]
R: """
        tot += preco

    conf = int(input(txt))

    if conf == 1:
        teatro[cadLin - 1][cadCol - 1] = 'C'
        print('\nCadeira comprada com sucesso')
    else:
        print('\nCancelando')

def liberar(reser):
    global tot, teatro, cadLin, cadCol, preco

    if reser == False:
        input(f"""\nEsta cadeira não esta reservada, então ela não pode ser liberada OwO.
Digite qualquer coisa para continuar: """)
        return 0

    conf = int(input(f"""\nTem certeza que deseja liberar a cadeira selecionada? (linha: {cadLin}, número: {cadCol})
Nós devolveremos seus R${(preco * 0.3):.2f}, porém esta cadeira não estará mais reservada.
[1-sim] [2-não]
R: """))

    if conf == 1:
        teatro[cadLin - 1][cadCol - 1] = 'L'
        print('\nCadeira liberada com sucesso')
        tot -= preco * 0.3
    else:
        print('\nCancelando')

def setup():
    global pNum, cNum, lin, teatro, ini, preco

    if ini:
        input(f'\nO teatro já esta aberto e está exibindo a peça de número {pNum}, não é possivel abrir outra peça\nDigite qualquer coisa para continuar: ')
        return 0

    while pNum == -1:
        try:
            pNum = int(input('\nInsira o número da peça que será exibida: '))
        except:
            print('Por favor, insira o número identificador da peça que será exibida')

    ini = True

    while cNum == 0 or lin == 0:
        try:
            if lin == 0:
                lin = int(input('\ninsira o número de linhas de cadeiras para a peça: '))
            if cNum == 0:
                cNum = int(input('\ninsira o número de colunas de cadeiras para a peça: '))
            if lin > 20 or lin < 1:
                lin = 0
                raise Exception('número de linhas inválido')
            if cNum > lin * 20 or cNum < lin:
                cNum = 0
                raise Exception('número de colunas inválido')
        except:
            print("\nPor favor insira um número inteiro condizente com os valores pedidos.\nLinhas de 1 a 20.\nNúmero de cadeiras, pelo menos uma por linha e no máximo 20 por linha.\n")
        
    exc = cNum % lin
    for i in range(lin):
        for j in range(cNum // lin):
            teatro[i][j] = 'L'
            if exc > 0 and j == cNum // lin - 1:
                teatro[i][j + 1] = 'L'
                exc -= 1

    print('\nTamanho da peça definido. Fomato:')
    printTeatro(True)

    preco = -1
    while preco == -1:
        try:
            preco = float(input('\nInsira o preço do ingresso: '))
            if preco < 0:
                raise Exception('Preço inválido')
        except:
            print('Por favor insira um número inteiro ou decimal maior ou igual a 0')

    print(f'\nPreço do ingreço definido. Preço: R${preco:.2f}')
    input('\nDigite qualquer coisa para continuar: ')

while True:
    fun = int(input("""\nO que você deseja fazer:
    1 - iniciar um teatro
    2 - listar posições de cadeiras
    3 - reservar poltrona
    4 - comprar cadeira
    5 - liberar cadeira
    6 - encerrar teatro
    7 - exibir parciais
    0 - parar programa
R: """))

    if fun != 1 and fun != 0:
        if ini == True:
            if fun == 2:
                printTeatro(True)
            elif fun == 3:
                select('reservar')
            elif fun == 4:
                select('comprar')
            elif fun == 5:
                select('liberar')
            elif fun == 6:
                encerrar()
            elif fun == 7:
                parcial()
        else:
            input('\nNenhum teatro iniciado, para fazer a função desejada inicie um teatro\nDigite qualquer coisa para continuar: ')
    elif fun == 1:
        setup()
    elif fun == 0:
        conf = int(input("\nEncerrar o programa resultara na perda dos dados atuais.\nTem certeza de que quer fazer isso? [1 - sim] [2 - não]\nR: "))
        if conf == 1:
            break
        else: 
            print('\nCancelando')
    else:
        input('\nFunção não conhecida\nDigite qualquer coisa para continuar: ')
print('\nEncerrando programa, até mais.')