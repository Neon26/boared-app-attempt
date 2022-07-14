import os
from colorama import Fore
from colorama import Style
from colorama import init

init()


def print_blue(s):
    print(Fore.BLUE, Style.BRIGHT,s,Style.RESET_ALL)


def print_red(s):
    print(Fore.RED, Style.BRIGHT,s,Style.RESET_ALL)


def print_yellow(s):
    print(Fore.YELLOW, Style.BRIGHT,s,Style.RESET_ALL)

def print_green(s):
    print(Fore.GREEN, Style.BRIGHT,s,Style.RESET_ALL)

def input_blue(s):
    print(Fore.BLUE, Style.BRIGHT, end='')
    response = input(s)
    print(Style.RESET_ALL)
    return response

def input_red(s):
    print(Fore.RED, Style.BRIGHT, end='')
    response = input(s)
    print(Style.RESET_ALL)
    return response

def input_yellow(s):
    print(Fore.YELLOW, Style.BRIGHT, end='')
    response = input(s)
    print(Style.RESET_ALL)
    return response

def input_green(s):
    print(Fore.GREEN, Style.BRIGHT, end='')
    response = input(s)
    print(Style.RESET_ALL)
    return response
    