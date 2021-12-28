import os
import random

jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = 'n'
matriz = [
   [' ', ' ', ' '],
   [' ', ' ', ' '],
   [' ', ' ', ' ']
]


def tabuleiro():
   global matriz
   global jogadas
   os.system("cls")
   print('   0   1   2')
   print('0:  ' + matriz[0][0] + ' | ' + matriz[0][1] + ' | ' + matriz[0][2])
   print('   -----------')
   print('1:  ' + matriz[1][0] + ' | ' + matriz[1][1] + ' | ' + matriz[1][2])
   print('   -----------')
   print('2:  ' + matriz[2][0] + ' | ' + matriz[2][1] + ' | ' + matriz[2][2])
   print(f'jogadas: str(\033[32m{jogadas}\033[m)')
   os.system("cls")
def jogadorJoga():
   global  jogadas
   global quemJoga
   global maxJogadas
   if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input('linha..: '))
            c = int(input('coluna..: '))
            while matriz[l][c] != ' ':
                l = int(input('linha..: '))
                c = int(input('coluna..: '))
            matriz[l][c] = 'X'             #marca a jogada
            jogadas += 1
            quemJoga = 1
        except:
           print('Linha ou coluna invalida')
def cpuJoga():
   global jogadas
   global quemJoga
   global maxJogadas
   if quemJoga == 1 and jogadas < maxJogadas:
       l = random.randrange(0, 3)
       c = random.randrange(0, 3)
       while matriz[l][c] != ' ':
           l = random.randrange(0, 3)
           c = random.randrange(0, 3)
       matriz[l][c] = 'O'
       jogadas += 1
       quemJoga = 2
def verificarVitoria():
    global matriz
    vitoria = 'n'
    simbolos = ['X', 'O']
    for s in simbolos:
        vitoria = 'n'
        il = ic = 0     #linhas
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if matriz[il][ic] == s:
                    soma +=1
                ic += 1
            if soma == 3:
                vitoria = s
                break
        if vitoria != 'n':
            break
        il += 1
#colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            ic = 0
            while il < 3:
                if matriz[il][ic] == s:
                    soma +=1
                il += 1
            if soma == 3:
                vitoria = s
                break
        if vitoria != 'n':
            break
        ic += 1
        #dagonal 1
        soma = 0
        idiag = 0
        while idiag < 3:
            if matriz[idiag][idiag] == s:
                soma += 1
            idiag += 1
        if soma == 3:
            vitoria = s
            break
        #diagonal 2
        soma = 0
        idgl = 0
        idgc = 2
        while idgc >= 0:
            if matriz[idgl][idgc]== s:
                soma += 1
            idgl += 1
            idgc -= 1
        if soma == 3:
            vitoria = s
            break
    return  vitoria
def redefinir():
    global matriz
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    vit = 'n'
    matriz = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    while jogarNovamente == 's':
        while True:
            tabuleiro()
            jogadorJoga()
            cpuJoga()
            tabuleiro()
            vit = verificarVitoria()
            if vit != 'n' or jogadas >= maxJogadas:
                break
        print('\033[31mFIM DE JOGO\033[m')
        if vit == 'X' or vit == 'O':
            print('resultado: jogador' + vit + ' venceu')
        else:
            print('resultado Empate')
            jogarNovamente = input('\033[36mJogar novamente? [s/n]:\033[m')
            redefinir()
