import os
from classes import *
import time


# GLOBALS
NETWORK_SIZE = 10


def clear():
    os.system('cls')


def main():
    Network_Generator.generate_user_info(NETWORK_SIZE)
    Network_Generator.generate_users()
    Network_Generator.show_user()
    Network_Generator.generate_user_friends()
    Network_Generator.print_connections()


if __name__ == '__main__':
    clear()
    main()
    input("Press enter to quit")
