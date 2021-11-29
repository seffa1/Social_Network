import os
from classes import *
import time


# GLOBALS
NETWORK_SIZE = 300

# 1 is very connected, 100 is not so connected
# Exp: 10 means a user can have a most 1/10th of the total network as friends
CONNECTEDNESS = 1


def clear():
    os.system('cls')


def main():
    Network_Generator.generate_user_info(NETWORK_SIZE)
    Network_Generator.generate_users()
    Network_Generator.show_user()
    Network_Generator.generate_user_friends(CONNECTEDNESS)
    Network_Generator.print_connections()


if __name__ == '__main__':
    clear()
    main()
    input("Press enter to quit")
