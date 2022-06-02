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
    OK = '\033[0;32m' #Verde
    WARNING = '\033[93m' #Amarelo
    FAIL = '\033[1;31m' #Vermelho
    RESET = '\033[0m' #Resetar cores

##
# Adição
def adicao ():
    while True:
        try:
            print('\n{}Informe o 1° valor: {}'.format(bcolors.WARNING,bcolors.RESET))
            num1 = float(input())
            print('\n{}Informe agora o 2° valor: {}'.format(bcolors.WARNING, bcolors.RESET))
            num2 = float(input())
            tot = round(num1 + num2, 4); # 4 casas decimais
            print('{}total = {}{}'.format(bcolors.OK,tot,bcolors.RESET))
            #print(type(tot))
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
            print('\n{}Informe o 1° valor: {}'.format(bcolors.WARNING,bcolors.RESET))
            num1 = float(input())
            print('\n{}Informe agora o 2° valor: {}'.format(bcolors.WARNING, bcolors.RESET))
            num2 = float(input())
            tot = round(num1 - num2, 4)
            print('{}total = {}{}'.format(bcolors.OK,tot,bcolors.RESET))
            print('total = {}'.format(tot))
            #print(type(tot))
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
            print('\n{}Informe o 1° valor: {}'.format(bcolors.WARNING,bcolors.RESET))
            num1 = float(input())
            print('\n{}Informe agora o 2° valor: {}'.format(bcolors.WARNING, bcolors.RESET))
            num2 = float(input())
            #num2 = float()
            tot = round(num1 * num2,4)
            print('{}total = {}{}'.format(bcolors.OK,tot,bcolors.RESET))
            #print(type(tot))
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
            print('\n{}Informe o 1° valor: {}'.format(bcolors.WARNING,bcolors.RESET))
            num1 = float(input())
            print('\n{}Informe agora o 2° valor: {}'.format(bcolors.WARNING, bcolors.RESET))
            num2 = float(input())
            #tot = num1 % num2 <-- Verifica se o numero é par ou impar
            tot = round(num1 / num2,4)
            print('{}total = {}{}'.format(bcolors.OK,tot,bcolors.RESET))
            #print(type(tot))
            input()
            break
        except ValueError:
            print('\n{}Você precisa digitar um número\n{}'.format(bcolors.FAIL,bcolors.RESET))
        return(tot)
##
# Menu principal
while telaaberta == True:
    def MenuPrincipal():
        inpA = str('+')
        inpS = str('-')
        inpM = str('*')
        inpD = str('/')
        escolha = str(input('''Qual operação deseja fazer?
        Adição (+)
        Subtração (-)
        Multiplcação (*)
        Divisão (/)
        ~~ Qualquer outra tecla para ENCERRAR
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
