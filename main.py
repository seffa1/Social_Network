import os
from classes import *
import time


def clear():
    os.system('cls')


# GLOBALS
NETWORK_SIZE = 0
MAX_FRIENDS = 0


# This will be the menu that you interact with
class Terminal:
    pass


def initialize():
    clear()
    print("Welcome to bookface, configure network...")
    print("Select network size:")
    print('1 ---> small')
    print('2 ---> medium')
    print('3 ---> large')

    options = ['1', '2', '3']

    a = ''

    while a not in options:
        a = input("--->")

    if a == '1':
        NETWORK_SIZE = 10
    elif a == '2':
        NETWORK_SIZE = 100
    else:
        NETWORK_SIZE = 1000

    print(f'\nSelect max friend count:')
    print('1 ---> 10% of total users')
    print('2 ---> 50% of total users')
    print('3 ---> 100% of total users')

    a = ''

    while a not in options:
        a = input("--->")

    if a == '1':
        MAX_FRIENDS = NETWORK_SIZE // 10
    elif a == '2':
        MAX_FRIENDS = NETWORK_SIZE // 2
    else:
        MAX_FRIENDS = NETWORK_SIZE

    print('\n-------------------------')
    print(f'PARAMETERS SELECTED')
    print(f'Network Size: {NETWORK_SIZE}')
    print(f'Max Friend Count: {MAX_FRIENDS}')
    print('\n-------------------------')
    input("Press enter to generate the network")
    clear()
    Network_Generator.generate_user_info(NETWORK_SIZE)
    Network_Generator.generate_users()
    Network_Generator.generate_connections(MAX_FRIENDS)
    input('\nPress Enter to Continue')

def terminal():
    while True:
        clear()
        options = ['1', '2', '3', 'X', 'x']

        print('Select Action:')
        print('1 ---> Show Users')
        print('2 ---> Print Connections')
        print('3 ---> Find Path Between Users')
        print('X ---> Exit\n')

        a = ''
        while a not in options:
            a = input('--->')

        if a == '1':
            Network_Generator.show_user()
            input('Press enter to continue')
        elif a == '2':
            Network_Generator.print_connections()
            input('Press enter to continue')
        elif a == '3':
            pass
            input('Press enter to continue')
        else:
            break


def main():
    initialize()
    terminal()


if __name__ == '__main__':
    clear()
    main()
    input("Press enter to quit")
