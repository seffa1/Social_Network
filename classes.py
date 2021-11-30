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
        self.friends = {}

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
    user_dict = {}  # user.email : user
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

    @classmethod
    def generate_user_friends(cls, connectedness: int):

        print('\nGenerating friend network...')
        for user_email in cls.user_dict:
            user = cls.user_dict[user_email]
            number_of_friends = random.randint(1, len(cls.user_dict) // connectedness)  # at most you can be friends with a 1/3 of total users

            for i in range(0, number_of_friends):
                # Two users are going to end up each connecting to the other, resulting in two connections
                # This should only be one connection, with one weight between the two
                # We need to solve this issue:

                # This makes us choose a user who is not already our friend
                # while user not in friend.friends.values():
                friend = random.choice(list(cls.user_dict.values()))


                likeness = random.randint(0, 9)
                user.add_friend(friend, likeness)

    @classmethod
    def print_connections(cls):
        input("\nPress enter to print connections...")

        for user in cls.user_dict.values():
            print(f'Friends of {user.email}')
            for friend in user.friends:
                print(f'---> Weight: {user.friends[friend]}  {friend}')
            print('-------------')
            # Print total connections here
            print('-------------')

    @classmethod
    def count_duplicates(cls):
        # Its currently not working
        input("Press enter to count duplicates")
        print("Counting duplicate connections...")
        count = 0
        for user in cls.user_dict.values():
            for friend_email in user.friends:
                friend = cls.user_dict[friend_email]
                if user.email in friend.friends:
                    count += 1
        print(f'{count} duplicate connections found.')



# https://www.geeksforgeeks.org/visualize-graphs-in-python/
class Network_Visualizer:
    def __init__(self):
        self.connections

