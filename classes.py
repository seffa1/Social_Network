import os
import random
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def clear():
    os.system('cls')


class User:
    user_ID = 0

    def __init__(self, name: str, email: str, age: int, gender: str):
        self.email = email
        self.age = age
        self.name = name
        self.gender = gender
        self.friends = {}  # email: weight

        User.user_ID += 1
        self.user_ID = User.user_ID

    def add_friend(self, friend, weight):  # weight represents how much you interact with that friend
        self.friends[friend.email] = weight

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')
        print(f'Gender: {self.gender}')

    def show_friends(self):
        clear()
        print(f'Friends of {self.name}:')
        for friend in self.friends:
            print(friend.name)

    def show_recommended_friends(self):
        pass

    def __repr__(self):
        return f'User ID: {self.user_ID}  Email: {self.email}'


class Network_Generator:
    user_dict = {}  # user.email : user object
    name_list = deque()
    email_list = deque()
    age_list = deque()
    gender_list = deque()

    @classmethod
    def generate_user_info(cls, user_amount):
        print(f''
              f'Generating info for {user_amount} users...')
        n = 0

        # Generates the names, age, and gender for the users from a text file of names
        with open('names.txt', 'r') as name_file:
            for name in name_file.readlines():
                cls.name_list.append(str(name)[0:-1])  # gets ride of the '\n'

                # Adds age and gender to the list
                cls.age_list.append(random.randint(14, 90))
                cls.gender_list.append(random.choice(['m', 'f']))
                n += 1
                if n >= user_amount:
                    break

        # Generates the email list
        for name in cls.name_list:
            # Builds a random email address for each person and adds it to the list
            email = ''
            email += str(name)[0]
            with open('names.txt', 'r') as name_file:
                random_name = random.choice(list(name_file))
            email += str(random_name)[0:-1]  # gets ride of the '\n'
            email += str(random.randint(0, 99))
            email += '@gmail.com'
            cls.email_list.append(email)
        print('Done')

    @classmethod
    def add_user(cls, user):
        cls.user_dict[user.email] = user

    @classmethod
    def generate_users(cls):
        # Its unlikely but technically possible to have two users with the same email generated
        # In that case the second one would overwrite the first

        print('\nGenerating user accounts with user info....')
        while len(cls.name_list) > 0:
            name = cls.name_list.pop()
            email = cls.email_list.pop()
            age = cls.age_list.pop()
            gender = cls.gender_list.pop()
            user = User(name, email, age, gender)
            cls.add_user(user)

        print('Done')

    @classmethod
    def show_user(cls):
        print('\nPrinting user list...')
        for user in cls.user_dict:
            print(f'ID: {cls.user_dict[user].user_ID}   Email: {user}')
        print('----------------------\n')


    # This method needs re-written
    # It should be chosing two friends at random, if they dont have a connection, make a connection with a weight
    # Then add each other to each other's friends list
    # This way there is one edge with one weight instead of two
    @classmethod
    def generate_user_friends(cls, connectedness: int):
        print('Generating friend network...')
        for user_email in cls.user_dict:
            user = cls.user_dict[user_email]
            number_of_friends = random.randint(1, len(cls.user_dict) // connectedness)  # at most you can be friends with a 1/3 of total users
            for i in range(0, number_of_friends):
                friend = random.choice(list(cls.user_dict.values()))
                likeness = random.randint(0, 9)
                user.add_friend(friend, likeness)

    @classmethod
    def print_connections(cls):
        input("\nPress enter to print connections...")
        for user in cls.user_dict.values():
            print(f'Friends of User ID:{user.user_ID} - {user.email}')
            for friend in user.friends:
                print(f'---> Weight: {user.friends[friend]} - ID: {cls.user_dict[friend].user_ID} - {friend}')
            print('')
        print('----------------------\n')

    @classmethod
    def count_connections(cls):
        print("Counting duplicate connections...")
        duplicate_count = 0
        connection_count = 0
        for user in cls.user_dict.values():
            for friend_email in user.friends:
                connection_count += 1
                friend = cls.user_dict[friend_email]
                if user.email in friend.friends:
                    duplicate_count += 1
                    print(f"Duplicate: {user.user_ID} and {friend.user_ID}")
        print(f'Total Connections: {connection_count}')
        print(f'Duplicate Connections: {duplicate_count}')
        print('----------------------\n')


# https://www.geeksforgeeks.org/visualize-graphs-in-python/
class Network_Visualizer:
    def __init__(self):
        self.connections

