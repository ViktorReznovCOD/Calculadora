'''
@author: Felipe Araujo Camelo
Calculadora Básica (16.05.2022)
Sobre: Calculadora simples, que efetua as 4 operações básicas através do terminal.
'''
from logging import WARNING
import sys
import colorama
from colorama import Fore, Style
telaaberta = True

# Define cores padrão de saída no terminal:
class bcolors:
    OK = '\033[92m' #Verde
    WARNING = '\033[93m' #Amarelo
    FAIL = '\033[91m' #Vermelho
    RESET = '\033[0m' #Resetar cores

##
# Adição
def adicao ():
    while True:
        try:
            print('\n{}Informe o 1° valor: {}'.format(bcolors.WARNING,bcolors.RESET))
            num1 = int(input())
            print('\nInforme agora o 2° valor'.format(bcolors.WARNING, bcolors.RESET))
            num2 = int(input())
            tot = num1 + num2;
            print('total = {}'.format(tot))
            print(type(tot))
            input()
            break
        except ValueError:
            print('\n{}Você precisa digitar um número\n{}'.format(bcolors.FAIL,bcolors.RESET))
    return(tot)
##
# Subtração
def subtracao ():
    while True:
        try:     
            num1 = int(input('Informe o primeiro valor da operação: '))
            num2 = int(input('Agora inform o segundo: '))
            tot = num1 - num2
            print(type(tot))
            print('total = {}'.format(tot))
            print(type(tot))
            input()
            break
        except ValueError:
            print('\n{}Você precisa digitar um número\n{}'.format(bcolors.FAIL,bcolors.RESET))
    return(tot)
##
# Multiplicação
def multiplicacao ():
    while True:
        try:
            num1 = int(input('Informe o primeiro valor da operação: '))
            num2 = int(input('Agora inform o segundo: '))
            tot = num1 * num2
            print('total = {}'.format(tot))
            print(type(tot))
            input()
            break
        except ValueError:
            print('\n{}Você precisa digitar um número\n{}'.format(bcolors.FAIL,bcolors.RESET))
        return(tot)
##
# Divisão
def divisao ():
    while True:
        try:
            num1 = float(input('Informe o primeiro valor da operação: '))
            num2= float(input('Digite o segundo: '))
            #tot = num1 % num2 <-- Verifica se o numero é par ou impar
            tot = num1 / num2
            print('total = {}'.format(tot))
            print(type(tot))
            input()
            break
        except ValueError:
            print('\n{}Você precisa digitar um número\n{}'.format(bcolors.FAIL,bcolors.RESET))
        return(tot)
##
# Menu principal
while telaaberta == True:
    def MenuPrincipal():
        inpA = str('a')
        inpS = str('s')
        inpM = str('m')
        inpD = str('d')
        escolha = str(input('''Qual operação deseja fazer?
        (a) Adição +
        (s) Subtração -
        (m) Multiplcação *
        (d) Divisão /
        (q) Qualquer outra tecla para ENCERRAR
        '''))
        if escolha == inpA:
            adicao()
        elif escolha == inpS:
            subtracao()
        elif escolha == inpM:
            multiplicacao()
        elif escolha == inpD:
            divisao()
        else:
            sys.exit()
 
    MenuPrincipal()
